import pytest
from core.product import Product
from core.cart import ShoppingCart

def test_add_single_product():
    cart = ShoppingCart()
    product = Product(name="Shampoo", price=12.99)
    
    cart.add_item(product)
    items = cart.get_items()
    
    assert len(items) == 1
    assert items[0]['name'] == "Shampoo"
    assert items[0]['quantity'] == 1
    assert items[0]['price'] == 12.99

def test_add_multiple_different_products():
    cart = ShoppingCart()
    prod1 = Product(name="Soap", price=5.50)
    prod2 = Product(name="Lotion", price=14.75)
    
    cart.add_item(prod1)
    cart.add_item(prod2, quantity=2)
    items = cart.get_items()
    
    assert len(items) == 2
    assert items[0]['quantity'] == 1
    assert items[1]['quantity'] == 2

def test_add_same_product_updates_quantity():
    cart = ShoppingCart()
    prod = Product(name="Soap", price=5.50)
    
    cart.add_item(prod, quantity=2)
    cart.add_item(prod, quantity=3)
    items = cart.get_items()
    
    assert len(items) == 1
    assert items[0]['quantity'] == 5

def test_remove_product_from_cart():
    cart = ShoppingCart()
    prod1 = Product(name="Soap", price=5.50)
    prod2 = Product(name="Lotion", price=14.75)
    
    cart.add_item(prod1)
    cart.add_item(prod2)
    cart.remove_item(prod1)
    items = cart.get_items()
    
    assert len(items) == 1
    assert items[0]['name'] == "Lotion"

def test_add_zero_quantity_does_not_add():
    cart = ShoppingCart()
    prod = Product(name="Soap", price=5.50)
    cart.add_item(prod, quantity=0)
    
    items = cart.get_items()
    
    assert cart.get_count() == 0
    assert len(items) == 0
    with pytest.raises(IndexError):
        _ = items[0]['quantity']

def test_cart_total_sum_and_count():
    cart = ShoppingCart()
    prod1 = Product(name="Soap", price=3.50)
    prod2 = Product(name="Lotion", price=2.25)
    
    cart.add_item(prod1, quantity=3) 
    cart.add_item(prod2, quantity=4) 
    
    assert cart.get_total_sum() == 19.5
    assert cart.get_count() == 7

def test_add_large_quantity():
    cart = ShoppingCart()
    prod = Product(name="Bulk Soap", price=1.25)
    cart.add_item(prod, quantity=1000000)
    
    items = cart.get_items()
    
    assert len(items) == 1
    assert items[0]['quantity'] == 1000000
    assert cart.get_total_sum() == 1250.0

def test_product_with_negative_price():
    cart = ShoppingCart()
    prod = Product(name="Promo Item", price=-5.00)
    cart.add_item(prod, quantity=2)
    
    items = cart.get_items()
    
    assert items[0]['price'] == -5.00
    assert cart.get_total_sum() == -10.0

