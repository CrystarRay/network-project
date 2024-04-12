from flask import Flask, render_template, request, redirect, url_for
from cart import ShoppingCart

app = Flask(__name__)
cart = ShoppingCart()


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/add', methods=['POST'])
def add_to_cart():
    item_name = request.form['item']
    if item_name == "Apple":
        price = 0.99
    elif item_name == "Banana":
        price = 0.59
    elif item_name == "Carrot":
        price = 0.30
    else:
        # Handle the case where the item is not recognized
        return "Item not found", 404

    cart.add_item(item_name, price)
    return redirect(url_for('home'))  # or show_cart


@app.route('/cart')
def show_cart():
    items = cart.get_items()
    total_price = cart.get_total_price()
    return render_template('cart.html', items=items, total_price=total_price)


@app.route('/checkout', methods=['GET', 'POST'])
def checkout():
    total_price = cart.get_total_price()
    if request.method == 'POST':
        cart.clear_cart()
        return render_template('success.html', total_price=total_price)

    return render_template('checkout.html',total_price=total_price)


@app.route('/checkout_success')
def checkout_success():
    total_price = cart.get_total_price()
    cart.clear_cart()  # Clear the cart after successful checkout
    return render_template('success.html', total_price=total_price)


@app.route('/remove_item', methods=['POST'])
def remove_item():
    item_name = request.form['item_name']
    cart.remove_item(item_name)
    return redirect(url_for('show_cart'))


if __name__ == '__main__':
    app.run(debug=True)
