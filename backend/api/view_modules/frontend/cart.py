from common.cart.cart import client_cart
from common.cart.cart_item import CartItems
from rest_framework.response import Response
from rest_framework import viewsets, permissions

from common.dictionaries.dictionaries import DictDeliveryMethods
from common.products.product.product import Product
from django.core.exceptions import ObjectDoesNotExist
from common.seller.seller import SellerDeliveryMethods
from rest_framework_simplejwt.authentication import JWTAuthentication


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

    def delete(self, request):
        try:
            item_dbs = CartItems.objects.filter(client=request.user, id=request.data.get('id', 0))
            if item_dbs.exists():
                client_cart.remove_items(request, [item_dbs[0].product.product_id])
        except Exception as e:
            return Response({"error": e.__str__()}, status=400)
        return Response({}, status=200)

    def put(self, request):
        for item in request.data.get('cart_items', []):
            try:
                item_db = CartItems.objects.get(client=request.user, id=item.get('id', 0))
                item_db.count = item.get('quantity', 1)
                item_db.delivery_method = DictDeliveryMethods.objects.get(id=item.get('delivery_method', 0))
                item_db.save()
            except (CartItems.DoesNotExist, DictDeliveryMethods.DoesNotExist):
                continue
        return Response({}, status=200)
