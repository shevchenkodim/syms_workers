from rest_framework.response import Response
from rest_framework import viewsets, permissions
from common.products.product.product import Product
from common.products.comments.comments import ProductComment
from common.products.product.product_image import ProductImage
from common.serializers.product_serializers import ProductModelSerializer


class NoveltiesViewSet(viewsets.ViewSet):
    """ ViewSet for viewing categories. """
    count = 8
    permission_classes = [permissions.AllowAny]

    def list(self, request):
        qs_serializer = []
        for p in Product.objects.filter(is_active=True, is_available=True, quantity__gt=0)[:self.count]:
            image_path = ''
            image_qs = ProductImage.objects.filter(product_id__id=p.product_id)
            if image_qs.exists():
                image_path = image_qs[0].image.url

            qs_serializer.append({
                **ProductModelSerializer(p).data,
                'image': image_path,
                'image_height': 350,
                'is_available': p.is_available_product,
                'comment_count': ProductComment.get_comment_count(p),
                'average_star_rating': ProductComment.get_average_star_rating(p)
            })
        return Response(qs_serializer)
