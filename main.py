from core.cart import ShoppingCart
from core.product import Product


if __name__ == "__main__":
     cart = ShoppingCart(sales_tax=12.5)
     dove_soap = Product(name="Dove Soap", price=39.99)
     axeo_deos = Product(name="Axe Deo", price=99.99)
     cart.add_item(dove_soap, quantity=2)
     cart.add_item(axeo_deos, quantity=2)
     cart.view_cart_summary()
