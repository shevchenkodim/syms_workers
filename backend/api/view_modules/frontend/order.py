import pytz

from common.cart.cart import client_cart
from common.cart.cart_item import CartItems
from rest_framework.response import Response
from rest_framework import viewsets, permissions

from common.dictionaries.dictionaries import DictDeliveryMethods
from common.orders.orders import Order, OrderItems
from common.products.product.product import Product
from django.core.exceptions import ObjectDoesNotExist
from common.seller.seller import SellerDeliveryMethods
from rest_framework_simplejwt.authentication import JWTAuthentication

from core.settings import TIME_ZONE


class OrderViewSet(viewsets.ViewSet):
    """ ViewSet for order. """
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def list(self, request):
        resp = []
        order_qs = Order.objects.filter(client=request.user).order_by('-created_at')[:10]
        for order_db in order_qs:
            nw_datetime_obj = pytz.timezone(TIME_ZONE)
            local_time = order_db.created_at.astimezone(nw_datetime_obj)
            resp.append({
                "id": order_db.id,
                "total_amount": order_db.total_amount,
                "created_at": local_time.strftime("%d.%m.%Y %H:%M"),
                "products": [f"{x.product.name}[{x.count}]" for x in OrderItems.objects.filter(order=order_db)]
            })
        return Response(resp)

    def post(self, request):

        items_qs = CartItems.objects.filter(client=request.user)
        if len(items_qs) < 1:
            return Response({}, status=404)

        Order.create_order(request.user, items_qs)

        return Response({}, status=201)
