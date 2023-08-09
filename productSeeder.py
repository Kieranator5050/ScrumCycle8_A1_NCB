import random, string

"""MOCK DATA"""
class Product:
    @staticmethod
    def getProductByID(products: list, id: int):
        for product in products:
            if product.id == id:
                return product
        return None
        
    def __init__(self, _id, _title, _img, _desc, _price):
        self.id = _id
        self.title = _title
        self.img = _img
        self.description = _desc
        self.price = _price

def generateProducts():
    products = []
    for i in range(6):
        products.append(
            Product(
                i, 
                f'Item {i}',
                i,
                ''.join(random.choices(string.ascii_letters + string.digits, k=random.randint(10, 200))),
                (i+1)*100)
            )  
    return products