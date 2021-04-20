from rest_framework import generics, permissions
from common.frontend.sliders.main_slider import MainCarouselModel
from common.serializers.frontend_serializers import MainCarouselSerializer


class MainSliderImagesViewSet(generics.ListAPIView):
    """ ViewSet for viewing categories. """
    queryset = MainCarouselModel.objects.filter().order_by('order_id')[:10]
    serializer_class = MainCarouselSerializer
    permission_classes = [permissions.AllowAny]
