from flask import Flask, render_template, redirect
from datetime import datetime
import random, string

app = Flask(__name__)

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


""" 
Context processor
- Injects variable into every template
"""
@app.context_processor
def inject_date():
    return dict(date=datetime.now())

@app.route("/")
def home():
    return render_template('home.html')


@app.route("/products")
def product():
    return render_template('products.html', products=products)


@app.route("/products/<product_id>")
def product_detail(product_id):
    product = Product.getProductByID(products, int(product_id))
    if product:
        return render_template('product_detail.html', product=product)
    else:
        return redirect('/products')