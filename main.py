from core.cart import ShoppingCart
from core.product import Product


if __name__ == "__main__":
     cart = ShoppingCart()
     dove_soap = Product(name="Dove Soap", price=39.99)
     cart.add_item(dove_soap, quantity=5)
     cart.view_cart_summary()
