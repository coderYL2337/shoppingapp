# shopping_cart.py
class ShoppingCart:
    def __init__(self):
        self.items = {}
        self.total = 0

    def add_item(self, item, price, quantity=1):
        if item in self.items:
            self.items[item]['quantity'] += quantity
        else:
            self.items[item] = {'price': price, 'quantity': quantity}
        self.update_total()

    def update_total(self):
        self.total = sum(
            item['price'] * item['quantity'] 
            for item in self.items.values()
        )

    def get_receipt(self):
        receipt = []
        for item, details in self.items.items():
            line = f"{item}: ${details['price']} x {details['quantity']} = ${details['price'] * details['quantity']}"
            receipt.append(line)
        receipt.append(f"Total: ${self.total}")
        return "\n".join(receipt)

# Example usage
if __name__ == "__main__":
    cart = ShoppingCart()
    cart.add_item("Apple", 0.50, 3)
    cart.add_item("Banana", 0.30, 2)
    print(cart.get_receipt())

