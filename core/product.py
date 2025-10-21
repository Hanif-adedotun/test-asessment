import uuid

class Product:
    def __init__(self, name: str, price: float):
        if len(name) < 1:
            raise ValueError("Product name must have at least one character.")
        if price < 0:
            raise ValueError("Product price must be positive.")
        self.id = uuid.uuid4()
        self.name = name
        self.price = price
