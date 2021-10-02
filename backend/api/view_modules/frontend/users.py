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

