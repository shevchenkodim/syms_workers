from common.analytics.product_analytic import ProductAnalytic
from common.models import User
from django.contrib import admin
from common.cart.cart_item import CartItems
from common.access.access import AccessRole, UserRole
from common.dictionaries.dictionaries import BrandDict, UnitDict, DictDeliveryMethods, DictGuarantee, DictPaymentMethods
from common.frontend.sliders.main_slider import MainCarouselModel
from common.products.categories.categories import CategoryModel
from common.products.characteristic.characteristic import CharacteristicHandbookDict, CharacteristicAttributes, \
    CharacteristicProduct
from common.products.comments.comments import ProductComment
from common.products.product.product import Product
from common.products.product.product_description import ProductDescription
from common.products.product.product_image import ProductImage
from common.seller.seller import SellerModel, SellerDeliveryMethods, SellerGuarantee, SellerPaymentMethods


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'phone', 'first_name', 'last_name', 'is_active', 'date_joined')


admin.site.register(UserRole)
admin.site.register(AccessRole)

# Cart
admin.site.register(CartItems)

# Dicts
admin.site.register(UnitDict)
admin.site.register(BrandDict)
admin.site.register(CharacteristicHandbookDict)
admin.site.register(DictDeliveryMethods)
admin.site.register(DictGuarantee)
admin.site.register(DictPaymentMethods)

# Frontend
admin.site.register(MainCarouselModel)

# Products
admin.site.register(CategoryModel)
admin.site.register(CharacteristicAttributes)
admin.site.register(CharacteristicProduct)
admin.site.register(ProductComment)
admin.site.register(Product)
admin.site.register(ProductDescription)
admin.site.register(ProductImage)

# Seller
admin.site.register(SellerModel)
admin.site.register(SellerDeliveryMethods)
admin.site.register(SellerGuarantee)
admin.site.register(SellerPaymentMethods)

# Analytics
admin.site.register(ProductAnalytic)
