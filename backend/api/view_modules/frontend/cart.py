from django.core.exceptions import ObjectDoesNotExist

from common.cart.cart import client_cart
from rest_framework.response import Response
from rest_framework import viewsets, permissions
from rest_framework_simplejwt.authentication import JWTAuthentication

from common.dictionaries.dictionaries import DictDeliveryMethods
from common.products.product.product import Product
from common.seller.seller import SellerDeliveryMethods


class CartViewSet(viewsets.ViewSet):
    """ ViewSet for viewing cart. """
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def list(self, request):
        return Response(client_cart.get_cart_json(request))

    def post(self, request):
        try:
            product_db = Product.objects.get(product_id=request.data["product_id"])
        except (ObjectDoesNotExist, KeyError):
            return Response({}, status=404)

        delivery_method = None
        qs = SellerDeliveryMethods.objects.filter(seller=product_db.seller)
        if qs.exists():
            delivery_method = qs[0].delivery_methods

        client_cart.add_item(request, product_db, 1, delivery_method)

        return Response({}, status=201)

    def remove(self, request):
        print(request.data)
        return Response({}, status=200)
