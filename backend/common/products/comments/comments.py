from django.db import models
from django.db.models import Avg
from django.conf import settings
from common.products.product.product import Product
from common.tools import from_db_to_datetime


class ProductComment(models.Model):
    """ Product comment model """
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Owner')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Product')
    text = models.TextField(verbose_name='Comment')
    likes_count = models.IntegerField(default=0, verbose_name='Likes')
    dislikes_count = models.IntegerField(default=0, verbose_name='Dislikes')
    rating_stars = models.IntegerField(default=0, verbose_name='Rating stars')
    date_time_add = models.DateTimeField(auto_now_add=True, verbose_name='Date created')
    reply_to = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Reply to')

    def __str__(self):
        return self.text

    class Meta:
        db_table = 'product_comment'
        ordering = ['date_time_add']

    @staticmethod
    def get_comment_count(product):
        """ Get comment count for product """
        return ProductComment.objects.filter(product_id__product_id=product.product_id).count()

    @staticmethod
    def get_average_star_rating(product):
        """ Get average star rating for product """
        result = ProductComment.objects.filter(product_id__product_id=product.product_id).aggregate(Avg('rating_stars'))
        result_number = 0
        if result.get('rating_stars__avg'):
            result_number = int(result.get('rating_stars__avg'))
        return result_number

    def do_json(self):
        return {
            "id": self.id,
            "owner": {
                "full_name": f"{self.owner.last_name} {self.owner.first_name}",
                "image": self.owner.image.url
            },
            "text": self.text,
            "likes_count": self.likes_count,
            "dislikes_count": self.dislikes_count,
            "rating_stars": self.rating_stars,
            "date_time_add": from_db_to_datetime(self.date_time_add, seconds=False)
        }
