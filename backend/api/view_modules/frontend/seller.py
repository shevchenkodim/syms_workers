from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from rest_framework import viewsets, generics, permissions
from rest_framework_simplejwt.authentication import JWTAuthentication
from common.serializers.seller_serializers import SellerModelSerializer
from common.seller.seller import SellerModel, SellerDeliveryMethods, SellerGuarantee, SellerPaymentMethods


class SellerViewSet(viewsets.ViewSet):
    """ ViewSet for viewing sellers. """
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def retrieve(self, request, pk=None):
        queryset = SellerModel.objects.all()
        s_db = get_object_or_404(queryset, code_name=pk)
        serializer = SellerModelSerializer(s_db)
        return Response({
            **serializer.data,
            "blocks": [
                {
                    "title": "Способи оплати",
                    "bg_class": "green",
                    "items": [x.payment_methods.do_json() for x in SellerPaymentMethods.objects.filter(seller=s_db)],
                },
                {
                    "title": "Гарантія",
                    "bg_class": "warning",
                    "items": [x.guarantee.do_json() for x in SellerGuarantee.objects.filter(seller=s_db)],
                },
                {
                    "title": "Доступні способи доставки",
                    "bg_class": "info",
                    "items": [x.delivery_methods.do_json() for x in SellerDeliveryMethods.objects.filter(seller=s_db)],
                }
            ]
        })
