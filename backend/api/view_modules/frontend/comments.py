from rest_framework.response import Response
from rest_framework import viewsets, permissions
from common.products.product.product import Product
from rest_framework.pagination import LimitOffsetPagination
from common.products.comments.comments import ProductComment
from rest_framework_simplejwt.authentication import JWTAuthentication


class CommentViewSet(viewsets.ViewSet):
    """ ViewSet for viewing comments. """
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def list(self, request):
        qs_serializer = []
        pagination_class = LimitOffsetPagination()

        try:
            product_db = Product.objects.get(product_id=request.GET.get("product_id", ""))
        except Product.DoesNotExist:
            return Response({}, status=404)

        dbs = ProductComment.objects.filter(product=product_db).order_by('-date_time_add')

        pag_count = dbs.count()
        for p in pagination_class.paginate_queryset(dbs, request):
            qs_serializer.append(p.do_json())
        return Response({"rows": qs_serializer, "params": {"count": pag_count}})
