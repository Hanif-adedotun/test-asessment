import pytest
from core.product import Product

def test_product_creation_valid():
    product = Product(name="Toothbrush", price=3.99)
    
    assert product.name == "Toothbrush"
    assert product.price == 3.99
    assert hasattr(product, 'id')

def test_product_creation_empty_name_raises():
    with pytest.raises(ValueError) as excinfo:
        Product(name="", price=5)
    assert "Product name must have at least one character." in str(excinfo.value)

def test_product_creation_nonempty_name():
    product = Product(name="A", price=9.99)
    assert product.name == "A"

def test_product_id_is_unique():
    product1 = Product(name="A", price=1)
    product2 = Product(name="A", price=1)
    assert product1.id != product2.id

def test_product_price_negative():
     with pytest.raises(ValueError) as excinfo:
          Product(name="NegativePrice", price=-10.5)
     assert "Product price must be positive" in str(excinfo.value)

