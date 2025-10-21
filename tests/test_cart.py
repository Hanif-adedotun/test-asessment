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
    assert cart.get_total_sum() == 1250000.0

def test_sales_tax_calculation():
    cart = ShoppingCart(sales_tax=10)  # 10% sales tax
    prod1 = Product(name="Perfume", price=50.00)
    prod2 = Product(name="Body Wash", price=25.00)

    cart.add_item(prod1, quantity=2)  # 2 * 50 = 100
    cart.add_item(prod2, quantity=1)  # 1 * 25 = 25

    # Subtotal: 125, Sales tax: 12.5, Total: 137.5
    assert cart.get_total_sales_tax() == 12.5
    assert cart.get_total_sum() == 137.5

    # Ensure tax_amount fields are set and correct
    for item in cart.get_items():
        if item['name'] == "Perfume":
            assert item['tax_amount'] == 10.0  # 100 * 0.1
        elif item['name'] == "Body Wash":
            assert item['tax_amount'] == 2.5  # 25 * 0.1

def test_sales_tax_with_zero_tax():
    cart = ShoppingCart(sales_tax=0)
    prod = Product(name="Shampoo", price=30.0)
    cart.add_item(prod, quantity=3)

    assert cart.get_total_sales_tax() == 0.0
    assert cart.get_total_sum() == 90.0

def test_sales_tax_rounding():
    cart = ShoppingCart(sales_tax=7.25)
    prod = Product(name="Conditioner", price=19.99)
    
    cart.add_item(prod, quantity=3)
    expected_tax = round(59.97 * 0.0725, 2)
    
    assert cart.get_total_sales_tax() == expected_tax

def test_sales_tax_on_empty_cart():
    cart = ShoppingCart(sales_tax=20)
    
    assert cart.get_total_sales_tax() == 0.0
    assert cart.get_total_sum() == 0.0

