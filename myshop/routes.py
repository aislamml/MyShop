from myshop import app
from flask import render_template
from myshop.models import Product


@app.route('/')
def index():
    products = Product.query.all()
    return render_template('index.html', products = products)

@app.route('/shop')
def shop():
    return render_template('shop.html')

@app.route('/product-details')
def product_details():
    return render_template('product-details.html')

@app.route('/checkout')
def checkout():
    return render_template('checkout.html')

@app.route('/cart')
def cart():
    return render_template('cart.html')