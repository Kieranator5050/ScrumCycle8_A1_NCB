from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<p>Home</p>"


@app.route("/products")
def product():
    return "<p>Products</p>"


@app.route("/products/<product_id>")
def product_detail(product_id):
    return f'<p>Product {product_id} Detail</p>'