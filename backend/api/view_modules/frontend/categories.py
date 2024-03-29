from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from rest_framework import viewsets, generics, permissions
from common.products.categories.categories import CategoryModel
from rest_framework_simplejwt.authentication import JWTAuthentication
from common.serializers.frontend_serializers import CategoryModelSerializer


class CategoriesViewSet(viewsets.ViewSet):
    """ ViewSet for viewing categories. """
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def list(self, request):
        qs_serializer = []
        for item in CategoryModel.objects.filter(is_active=True, parent__isnull=True):
            item_data = {**CategoryModelSerializer(item).data, 'children': []}
            for c_item in CategoryModel.objects.filter(is_active=True, parent_id=item.id):
                item_data['children'].append(CategoryModelSerializer(c_item).data)
            qs_serializer.append(item_data)
        return Response(qs_serializer)

    def retrieve(self, request, pk=None):
        queryset = CategoryModel.objects.filter(is_active=True)
        slider = get_object_or_404(queryset, code_name=pk)
        serializer = CategoryModelSerializer(slider)
        return Response(serializer.data)
