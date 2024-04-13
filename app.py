from flask import Flask, render_template, request, redirect, url_for
from cart import ShoppingCart
import time

app = Flask(__name__)
cart = ShoppingCart()

@app.route('/')
def home():
    start_time = time.time()
    result = render_template('home.html')
    end_time = time.time()
    print(f"Time for GET /: {end_time - start_time:.6f} seconds")
    return result

@app.route('/add', methods=['POST'])
def add_to_cart():
    start_time = time.time()
    item_name = request.form['item']
    if item_name == "Apple":
        price = 0.99
    elif item_name == "Banana":
        price = 0.59
    elif item_name == "Carrot":
        price = 0.30
    elif item_name == "Orange":
        price = 1.50
    elif item_name == "Watermelon":
        price = 3.00
    else:
        # Handle the case where the item is not recognized
        return "Item not found", 404

    cart.add_item(item_name, price)
    end_time = time.time()
    print(f"Time for POST /add: {end_time - start_time:.6f} seconds")
    return redirect(url_for('home'))  # or show_cart

@app.route('/cart')
def show_cart():
    start_time = time.time()
    items = cart.get_items()
    total_price = cart.get_total_price()
    result = render_template('cart.html', items=items, total_price=total_price)
    end_time = time.time()
    print(f"Time for GET /cart: {end_time - start_time:.6f} seconds")
    return result

@app.route('/checkout', methods=['GET', 'POST'])
def checkout():
    start_time = time.time()
    total_price = cart.get_total_price()
    if request.method == 'POST':
        cart.clear_cart()
        result = render_template('success.html', total_price=total_price)
    else:
        result = render_template('checkout.html',total_price=total_price)
    end_time = time.time()
    print(f"Time for {request.method} /checkout: {end_time - start_time:.6f} seconds")
    return result

@app.route('/checkout_success')
def checkout_success():
    start_time = time.time()
    total_price = cart.get_total_price()
    cart.clear_cart()  # Clear the cart after successful checkout
    result = render_template('success.html', total_price=total_price)
    end_time = time.time()
    print(f"Time for GET /checkout_success: {end_time - start_time:.6f} seconds")
    return result

@app.route('/remove_item', methods=['POST'])
def remove_item():
    start_time = time.time()
    item_name = request.form['item_name']
    cart.remove_item(item_name)
    end_time = time.time()
    print(f"Time for POST /remove_item: {end_time - start_time:.6f} seconds")
    return redirect(url_for('show_cart'))

if __name__ == '__main__':
    app.run(debug=True)
