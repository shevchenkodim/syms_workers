from rest_framework.response import Response
from rest_framework import permissions, viewsets
from rest_framework.generics import get_object_or_404
from common.frontend.sliders.main_slider import MainCarouselModel
from common.serializers.frontend_serializers import MainCarouselSerializer


class MainSliderImagesViewSet(viewsets.ViewSet):
    """ ViewSet for viewing categories. """
    permission_classes = [permissions.AllowAny]

    def list(self, request):
        queryset = MainCarouselModel.objects.filter().order_by('order_id')[:10]
        serializer = MainCarouselSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = MainCarouselModel.objects.all()
        slider = get_object_or_404(queryset, pk=pk)
        serializer = MainCarouselSerializer(slider)
        return Response(serializer.data)
