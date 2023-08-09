from flask import Flask, render_template
from flask_assets import Environment, Bundle
from datetime import datetime

app = Flask(__name__)

"""Register Scss"""
assets = Environment(app)
assets.url = app.static_url_path
scss = Bundle('style.scss', filters='pyscss', output='style.css')
assets.register('scss', scss)

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