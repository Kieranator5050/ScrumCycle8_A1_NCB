from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)


"""MOCK DATA"""

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
    return render_template('products.html')


@app.route("/products/<product_id>")
def product_detail(product_id):
    return render_template('product_detail.html')