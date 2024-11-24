# shopping_cart.py
class ShoppingCart:
    def __init__(self):
        self.items = {}
        self.total = 0
        self.discount = 0

    def add_item(self, item, price, quantity=1):
        if item in self.items:
            self.items[item]['quantity'] += quantity
        else:
            self.items[item] = {'price': price, 'quantity': quantity}
        self.update_total()

    def apply_discount(self, percentage):
        if not 0 <= percentage <= 100:
            raise ValueError("Discount must be between 0 and 100")
        self.discount = percentage
        self.update_total()

    def update_total(self):
        subtotal = sum(
            item['price'] * item['quantity'] 
            for item in self.items.values()
        )
        self.total = subtotal * (1 - self.discount / 100)

    def get_receipt(self):
        receipt = []
        for item, details in self.items.items():
            line = f"{item}: ${details['price']} x {details['quantity']} = ${details['price'] * details['quantity']}"
            receipt.append(line)
        if self.discount > 0:
            receipt.append(f"Discount applied: {self.discount}%")
        receipt.append(f"Total: ${self.total:.2f}")
        return "\n".join(receipt)

