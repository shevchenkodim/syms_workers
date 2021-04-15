import logging
from common.models import User
from api.helpers import json_response
from rest_framework.views import APIView
from rest_framework.status import HTTP_200_OK
from rest_framework.permissions import AllowAny
from broker.services.custom_jwt_auth.jwt import jwt_auth
from common.tools import clean_phone, check_phone, check_email

logger = logging.getLogger('syms_marketplace.auth')

first, second = "FIRST", "SECOND"


class BaseAuth(APIView):
    """ Client Base Auth """
    permission_classes = (AllowAny, )

    @staticmethod
    def post(request):
        data = request.data
        step = data.get('step', first)
        state = {"phone": get_state(True, True, data.get("phone", None))}
        if step == first:
            phone = data.get("phone", None)
            if phone:
                phone = clean_phone(phone)
                if check_phone(phone):
                    # auth_otp = GenerateOtpCode.get_random()
                    auth_otp = 1111
                    try:
                        User.objects.get(phone=phone)
                        state["phone"]["editable"] = False
                        state["password"] = get_state(True, True, "")
                        state["otpCode"] = get_state(True, True, auth_otp)
                    except User.DoesNotExist:
                        state["phone"]["show"] = True
                        state["phone"]["editable"] = True
                        state["email"] = get_state(True, True, "")
                        state["password"] = get_state(True, True, "")
                        state["lastName"] = get_state(True, True, "")
                        state["firstName"] = get_state(True, True, "")
                        state["otpCode"] = get_state(True, False, auth_otp)
                    state["step"] = second
                    return json_response(True, state, HTTP_200_OK)
                else:
                    errors = {"message": "Вкажіть вірний номер телефону"}
                    return json_response(False, {**state, "errors": errors}, HTTP_200_OK)
            else:
                errors = {"message": "Будь ласка введіть номер телефону"}
                return json_response(False, {**state, "errors": errors}, HTTP_200_OK)
        elif step == second:
            phone = data.get("phone", None)
            if phone:
                phone = clean_phone(phone)
                try:
                    client = User.objects.get(phone=phone)
                    password = data.get("password")
                    if not client.check_password(password):
                        errors = {"message": "Пароль невірний"}
                        state["phone"] = get_state(True, False, data.get("phone", None))
                        state["otpCode"] = get_state(True, False, 1111)
                        state["password"] = get_state(True, True, "")
                        logger.info(f"Користувач [{client.email}, {client.phone}] Пароль невірний!")
                        return json_response(False, {**state, "errors": errors}, HTTP_200_OK)

                    response = jwt_auth.get_token(user=client)
                    logger.info(f"Користувач [{client.email}, {client.phone}] Успішно зробив вхід до системи!")
                    return json_response(True, response, HTTP_200_OK)
                except User.DoesNotExist:
                    first_name = data.get("first_name")
                    last_name = data.get("last_name")
                    password = data.get("password")
                    email = data.get("email")
                    if User.has_email(email):
                        errors = {"message": "Такий email вже використовується"}
                        return json_response(True, {"errors": errors}, HTTP_200_OK)
                    if not check_email(email):
                        errors = {"message": "Email має невірний формат"}
                        return json_response(True, {"errors": errors}, HTTP_200_OK)
                    if not first_name or not last_name:
                        errors = {"message": "Потрібно ввести прізвище та ім'я"}
                        return json_response(True, {"errors": errors}, HTTP_200_OK)
                    if not password or len(password) < 8:
                        errors = {"message": "Пароль має бути не менше 8 символів"}
                        return json_response(True, {"errors": errors}, HTTP_200_OK)
                    client = User.objects.create_user(
                        email=email,
                        phone=phone,
                        first_name=first_name,
                        last_name=last_name,
                        password=password
                    )

                    response = jwt_auth.get_token(user=client)

                    logger.info(f"Користувач [{client.email}, {client.phone}] Успішно зробив вхід до системи!")
                    return json_response(True, response, HTTP_200_OK)

        return json_response(True, state, HTTP_200_OK)


def get_state(show: bool, editable: bool, value) -> dict:
    """ Helper function for returned state """
    return {"show": show, "editable": editable, "value": value}
