from common.models import User
from rest_framework.response import Response
from rest_framework import permissions, viewsets
from rest_framework.generics import get_object_or_404
from common.serializers.user_serializers import UserSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication


class UserViewSet(viewsets.ViewSet):
    """ ViewSet for get users detail """
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def list(self, request):
        queryset = User.objects.filter().order_by('last_name', 'first_name')
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk="self"):
        pk = request.user.pk if pk == "self" else pk
        queryset = User.objects.all()
        slider = get_object_or_404(queryset, pk=pk)
        serializer = UserSerializer(slider)
        return Response(serializer.data)

    def put(self, request, pk="self"):
        req_data = request.data
        pk = request.user.pk if pk == "self" else pk
        try:
            user_db = User.objects.get(pk=pk)
            user_db.first_name = req_data["first_name"]
            user_db.last_name = req_data["last_name"]

            if "file" in request.FILES:
                user_db.image = request.FILES.get("file")

            if req_data["need_update_password"] == 'true':
                pas = req_data["password"]
                if len(pas) < 5:
                    pas = "admin"
                user_db.set_password(pas)

            user_db.save()
        except Exception as e:
            return Response({"error": e.__str__()}, status=200)

        return Response({}, status=200)
