from django.db import models
from django.conf import settings
from common.seller.seller import SellerModel
from common.products.product.product import Product


class ProductAnalytic(models.Model):
    client = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Client')
    seller = models.ForeignKey(SellerModel, on_delete=models.CASCADE, verbose_name='Seller')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Product')
    view_count = models.IntegerField(default=0)
    buy_count = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=15, decimal_places=2, default=0.00, verbose_name='Price')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Date created')

    class Meta:
        db_table = 'product_analytic'

    def __str__(self):
        return self.pk.__str__()

    @staticmethod
    def do_update(user, product, field='view_count'):
        qs = ProductAnalytic.objects.filter(client=user, seller=product.seller, product=product)
        if qs.exists():
            item = qs[0]
        else:
            item = ProductAnalytic.objects.create(client=user, seller=product.seller, product=product,
                                                  price=product.price)

        setattr(item, field, getattr(item, field, 0) + 1)

        item.save()
