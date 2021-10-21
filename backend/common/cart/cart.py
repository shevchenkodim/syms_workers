from decimal import Decimal

from common.cart.cart_item import CartItems


class Cart(object):

    def __init__(self):
        """ Initialize the cart """
        pass

    def add_item(self, request, product, count, delivery_method):
        """  Add a product to the cart"""
        if not CartItems.client_has_cart_item(product, request.user):
            CartItems.objects.create(
                delivery_method=delivery_method,
                client=request.user,
                product=product,
                count=count
            )

    def get_cart_json(self, request):
        """ Get cart json data """
        return {
            'count': CartItems.get_len_items(request.user),
            'items': [x.get_item_json() for x in CartItems.objects.filter(client=request.user)]
        }

    def get_total_price(self, request):
        """ Return total price in the cart """
        total = Decimal(0.0)
        for x in CartItems.objects.filter(client=request.user):
            item = x.get_item_json()
            total += Decimal(item['price']) * item['quantity']
        return total

    def remove_items(self, request, products: list):
        """ Remove a product from the cart """
        CartItems.objects.filter(client=request.user, product__product_id__in=products).delete()
        return True

    def clear_all(self, request):
        """ Remove all from cart """
        CartItems.objects.filter(client=request.user).delete()


client_cart = Cart()
