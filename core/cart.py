from core.product import Product
from utils.util import round_value

class ShoppingCart:
     def __init__(self, sales_tax: float = 0):
          """
          Initialize an empty shopping cart.
          """
          self.items = []
          self.sales_tax = sales_tax

     def add_item(self, item: Product, quantity: int = 1) -> None:
          """
          Add a product to the shopping cart along with the desired quantity.

          Args:
               item (Product): The product to add.
               quantity (int, optional): Number of items to add. Defaults to 1.

          Returns:
               None
          """
          # If quantity is zero or negative it does not add item to cart
          if(quantity < 1):
               return
          
          # Check if product already exists in the cart, if so, just update the quantity
          for cart_item in self.items:
               if cart_item['id'] == item.id:
                    cart_item['quantity'] += quantity
                    break
          else:
               self.items.append({
                    'id': item.id,
                    'name': item.name,
                    'price': item.price,
                    'quantity': quantity
               })

     def remove_item(self, item: Product) -> None:
          """
          Remove a product from the cart by matching its product id.

          Args:
               item (Product): The product to remove.

          Returns:
               None
          """
          self.items = [cart_item for cart_item in self.items if cart_item['id'] != item.id]

     def get_total_sum(self) -> float:
          """
          Calculate the total sum of the cart, including sales tax.

          Returns:
               float: The total price of all items in the cart including sales tax.
          """
          return sum(item['price'] * item['quantity'] for item in self.items) + self.get_total_sales_tax()

     def get_items(self) -> list:
          """
          Retrieve the list of all items in the cart.

          Returns:
               list: A list of dictionaries representing cart items.
          """
          return self.items

     def get_total_sales_tax(self) -> float:
          """
          Calculate the total sales tax of the cart.

          Returns:
               float: The total sales tax of the cart.
          """
          for item in self.items:
               tax_amount = round_value(item['price'] *item['quantity'] *(self.sales_tax / 100))
               item['tax_amount'] = tax_amount
          return sum(item['tax_amount'] for item in self.items)

     def get_count(self) -> int:
          """
          Calculate the total quantity of items in the cart.

          Returns:
               int: The total number of all items in the cart.
          """
          return sum(item['quantity'] for item in self.items)
     
     def view_cart_items(self) -> None:
          """
          Print all items in the cart with quantity, name, and price.

          Returns:
               None
          """
          for item in self.items:
               print(f"({item['quantity']}) {item['name']} - {round_value(item['price'])} each")
     
     def view_cart_summary(self) -> None:
          """
          Print a summary of the cart including item count and total value.

          Returns:
               None
          """
          print(f"Cart count: {self.get_count()} total items")
          print(f"Total Sales tax: {self.get_total_sales_tax()}")
          self.view_cart_items()
          print(f"Cart total: {self.get_total_sum()}")
          
          

