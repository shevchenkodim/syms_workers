from django.db import models


class MainCarouselModel(models.Model):
    """ Main carousel slider model """
    order_id = models.IntegerField(default=0, verbose_name='Order id')
    item_alt = models.CharField(max_length=100, blank=True, verbose_name='Image description')
    item_image = models.ImageField(upload_to='slider_main')

    class Meta:
        db_table = 'frontend_main_carousel'
        ordering = ['order_id']

    def delete(self, *args, **kwargs):
        self.item_image.delete()
        super(MainCarouselModel, self).delete(*args, **kwargs)
