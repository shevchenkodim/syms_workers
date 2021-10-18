from rest_framework.generics import get_object_or_404

from api.helpers import validate_price
from rest_framework.response import Response
from rest_framework import viewsets, permissions

from common.products.characteristic.characteristic import CharacteristicProduct
from common.products.product.product import Product
from rest_framework.pagination import LimitOffsetPagination
from common.products.comments.comments import ProductComment
from common.products.product.product_description import ProductDescription
from common.products.product.product_image import ProductImage
from rest_framework_simplejwt.authentication import JWTAuthentication
from common.serializers.product_serializers import ProductModelSerializer

ORDERING_MAPS = {
    "Від дешевших": "price",
    "Від дорогих": "-price",
    "Новинки": "-created_at"
}


class NoveltiesViewSet(viewsets.ViewSet):
    """ ViewSet for viewing categories. """
    count = 8
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def list(self, request):
        qs_serializer = []
        for p in Product.available.all()[:self.count]:
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


class ProductsViewSet(viewsets.ViewSet):
    """ ViewSet for viewing products. """
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def retrieve(self, request, pk=None):
        queryset = Product.objects.all()
        product_db = get_object_or_404(queryset, code=pk)
        serializer = ProductModelSerializer(product_db)

        return Response({
            **serializer.data,
            'image_height': 350,
            'is_available': product_db.is_available_product,
            'comment_count': ProductComment.get_comment_count(product_db),
            'images': ProductImage.get_images_by_product(product_db.product_id),
            'average_star_rating': ProductComment.get_average_star_rating(product_db),
            'product_descriptions': ProductDescription.get_description_by_product(product_db.product_id),
            'characteristic_list': CharacteristicProduct.get_characteristic_by_product(product_db.product_id)
        })

    def list(self, request):
        qs_serializer = []
        pagination_class = LimitOffsetPagination()

        f_data = {"category_id": 0}
        if "category_id" in request.GET:
            f_data = {"category_id": request.GET["category_id"]}

        price_from = validate_price(request.GET.get("price_from", 0))
        if price_from:
            f_data = {**f_data, "price__gte": price_from}

        price_to = validate_price(request.GET.get("price_to", 999999))
        if price_to:
            f_data = {**f_data, "price__lte": price_to}

        brand = request.GET.get("brand", "")
        if brand:
            f_data = {**f_data, "brand__value": brand}

        ordering = request.GET.get("ordering", "Новинки")
        if ordering:
            ordering = ORDERING_MAPS.get(ordering, '-created_at')

        dbs = Product.available.filter(**f_data).order_by(ordering)

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
                'average_star_rating': ProductComment.get_average_star_rating(p)
            })
        return Response({"rows": qs_serializer, "params": {"count": pag_count}})
