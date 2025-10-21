import uuid

class Product:
    def __init__(self, name: str, price: float):
        self.id = uuid.uuid4()
        self.name = name
        self.price = price
