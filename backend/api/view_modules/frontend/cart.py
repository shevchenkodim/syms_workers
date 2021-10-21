from common.cart.cart import client_cart
from rest_framework.response import Response
from rest_framework import viewsets, permissions
from rest_framework_simplejwt.authentication import JWTAuthentication


class CartViewSet(viewsets.ViewSet):
    """ ViewSet for viewing cart. """
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def list(self, request):
        return Response(client_cart.get_cart_json(request))
