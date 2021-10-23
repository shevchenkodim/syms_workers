from django.db.models import Q
from common.cart.cart_item import CartItems
from rest_framework.response import Response
from rest_framework import viewsets, permissions
from common.products.product.product import Product
from rest_framework.pagination import LimitOffsetPagination
from common.products.comments.comments import ProductComment
from common.products.product.product_image import ProductImage
from rest_framework_simplejwt.authentication import JWTAuthentication
from common.serializers.product_serializers import ProductModelSerializer


class SearchViewSet(viewsets.ViewSet):
    """ ViewSet for viewing search products. """
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def list(self, request):
        qs_serializer = []
        pagination_class = LimitOffsetPagination()

        value = request.GET.get('value')
        if value:
            dbs = Product.available.filter(
                Q(
                    Q(product_id=value) |
                    Q(code__icontains=value) |
                    Q(name__icontains=value) |
                    Q(brand__value__icontains=value) |
                    Q(seller__name__icontains=value)
                )
            ).order_by('-created_at')
        else:
            dbs = Product.available.all().order_by('-created_at')

        pag_count = dbs.count()
        for p in pagination_class.paginate_queryset(dbs, request):
            im_path = ''
            image_qs = ProductImage.objects.filter(product_id__id=p.product_id)
            if image_qs.exists():
                im_path = image_qs[0].image.url

            qs_serializer.append({
                **ProductModelSerializer(p).data,
                'image': im_path,
                'image_height': 350,
                'is_available': p.is_available_product,
                'comment_count': ProductComment.get_comment_count(p),
                'average_star_rating': ProductComment.get_average_star_rating(p),
                'exists_in_cart': CartItems.objects.filter(client=request.user, product=p).exists(),
                'exists_in_favorites': False
            })
        return Response({"rows": qs_serializer, "params": {"count": pag_count}})
