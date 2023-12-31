from flask import Flask, render_template, redirect
from datetime import datetime
from .scripts.productSeeder import generateProducts, Product

app = Flask(__name__)  

"""Global Variables"""
product_list = generateProducts()

""" 
Context processor
- Injects variable into every template
"""
@app.context_processor
def inject_date():
    return dict(date=datetime.now())

"""
Routes
"""
# Home Route
@app.route("/")
def home():
    return render_template('home.html')

# Products View
@app.route("/products")
def products():
    return render_template('products.html', products=product_list)

# Product Detail View
@app.route("/products/<product_id>")
def product_detail(product_id):
    product = Product.getProductByID(product_list, int(product_id))
    if product:
        return render_template('product_detail.html', product=product)
    else:
        return redirect('/products')