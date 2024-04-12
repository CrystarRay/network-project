class ShoppingCart:
    def __init__(self):
        self.items = {}

    def add_item(self, name, price):
        # If the item already exists, increment its quantity
        if name in self.items:
            self.items[name]['quantity'] += 1
        else:
            # Otherwise, add the item with quantity 1
            self.items[name] = {'price': price, 'quantity': 1}

    def remove_item(self, name):
        if name in self.items:
            if self.items[name]['quantity'] > 1:
                self.items[name]['quantity'] -= 1
            else:
                del self.items[name]

    def get_total_price(self):
        return sum(item['price'] * item['quantity'] for item in self.items.values())

    def get_items(self):
        # Convert the items dictionary to a list of item details
        return [{'name': name, 'price': details['price'], 'quantity': details['quantity']} for name, details in self.items.items()]

    def clear_cart(self):
        self.items.clear()