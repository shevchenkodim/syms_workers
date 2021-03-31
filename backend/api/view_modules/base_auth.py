import logging
from django.contrib.auth import login
from django.urls import reverse
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from broker.utils.verification.verification import check_phone, clean_phone, check_email
from common.access.access import UserRole, AccessRole
from common.geo.user_location_history import UserLocationHistoryModel
from common.models import User
from broker.utils.otp_code.otp_code import GenerateOtpCode

logger = logging.getLogger('syms_marketplace.auth')

first, second = "FIRST", "SECOND"


class BaseAuth(APIView):
    """ Client Base Auth """

    @staticmethod
    def post(request):
        data = request.data
        step = data.get('step', first)
        if step == first:
            phone = data.get("phone", None)
            if phone:
                phone = clean_phone(phone)
                if check_phone(phone):
                    auth_otp = '1111'
                    try:
                        client = User.objects.get(phone=phone)
                        state = {"phone": True, "phone_editable": False,
                                 "otp": True, "otp_editable": False,
                                 "password": True, "password_editable": True}
                        parameters = {"otp_code": auth_otp}
                        return Response({"state": state, "parameters": parameters}, status=status.HTTP_200_OK)
                    except User.DoesNotExist:
                        state = {"phone": True, "phone_editable": False,
                                 "otp": True, "otp_editable": False,
                                 "password": True, "password_editable": True,
                                 "first_name": True, "first_name_editable": True,
                                 "last_name": True, "last_name_editable": True,
                                 "email": True, "email_editable": True}
                        parameters = {"otp_code": auth_otp}
                        return Response({"state": state, "parameters": parameters}, status=status.HTTP_200_OK)
                else:
                    errors = {"message": "Вкажіть вірний номер телефону"}
                    state = {"phone": True, "phone_editable": True}
                    return Response({"errors": errors, "state": state}, status=status.HTTP_200_OK)
            else:
                errors = {"message": "Будь ласка введіть номер телефону"}
                state = {"phone": True, "phone_editable": True}
                return Response({"errors": errors, "state": state}, status=status.HTTP_200_OK)
        elif step == second:
            phone = data.get("phone", None)
            if phone:
                phone = clean_phone(phone)
                try:
                    client = User.objects.get(phone=phone)
                    password = data.get("password")
                    if not client.check_password(password):
                        errors = {"message": "Пароль невірний"}
                        state = {"show_phone": True, "phone_editable": False,
                                 "show_otp": True, "otp_editable": False,
                                 "show_password": True, "step": second,
                                 "password_enabled": True}

                        logger.info(f"Користувач [{client.email}, {client.phone}] Пароль невірний!")

                        return Response({"errors": errors, "state": state}, status=status.HTTP_200_OK)

                    login(request, client)

                    logger.info(f"Користувач [{client.email}, {client.phone}] Успішно зробив вхід до системи!")
                    return Response({"status": "ok", "redirect": reverse('client:index')}, status=status.HTTP_200_OK)
                except User.DoesNotExist:
                    first_name = data.get("first_name")
                    last_name = data.get("last_name")
                    password = data.get("password")
                    email = data.get("email")
                    if User.has_email(email):
                        errors = {"message": "Такий email вже використовується"}
                        return Response({"errors": errors}, status=status.HTTP_200_OK)
                    if not check_email(email):
                        errors = {"message": "Email має невірний формат"}
                        return Response({"errors": errors}, status=status.HTTP_200_OK)
                    if not first_name or not last_name:
                        errors = {"message": "Потрібно ввести прізвище та ім'я"}
                        return Response({"errors": errors}, status=status.HTTP_200_OK)
                    if not password or len(password) < 8:
                        errors = {"message": "Пароль має бути не менше 8 символів"}
                        return Response({"errors": errors}, status=status.HTTP_200_OK)
                    client = User.objects.create_user(
                        email=email,
                        phone=phone,
                        first_name=first_name,
                        last_name=last_name,
                        password=password
                    )
                    UserRole.objects.create(
                        role=AccessRole.objects.get_or_create(role='Клієнт', code_role='client')[0],
                        user=client
                    )
                    login(request, client)
                    logger.info(f"Користувач [{client.email}, {client.phone}] Успішно зробив вхід до системи!")
                    return Response({"status": "ok", "redirect": reverse('client:index')}, status=status.HTTP_200_OK)
        else:
            state = {"phone": True, "phone_editable": True}
        return Response({"state": state}, status=status.HTTP_200_OK)
