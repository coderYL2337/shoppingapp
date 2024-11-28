# shopping_cart.py
class ShoppingCart:
    def __init__(self):
        self.items = {}
        self.total = 0
        self.discount = 0
        self.purchase_history = []  # New: Track purchase history

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

    def checkout(self):
        """New method: Record purchase in history and clear cart"""
        if self.items:
            purchase = {
                'items': self.items.copy(),
                'total': self.total,
                'discount_applied': self.discount
            }
            self.purchase_history.append(purchase)
            self.items = {}
            self.total = 0
            self.discount = 0
            return "Checkout successful!"
        return "Cart is empty!"

    def get_purchase_history(self):
        """New method: Return formatted purchase history"""
        if not self.purchase_history:
            return "No purchase history available."
        
        history = []
        for i, purchase in enumerate(self.purchase_history, 1):
            history.append(f"\nPurchase #{i}:")
            for item, details in purchase['items'].items():
                history.append(
                    f"  {item}: ${details['price']} x {details['quantity']} = ${details['price'] * details['quantity']}"
                )
            if purchase['discount_applied']:
                history.append(f"  Discount applied: {purchase['discount_applied']}%")
            history.append(f"  Total: ${purchase['total']:.2f}")
        return "\n".join(history)

    def get_receipt(self):
        receipt = []
        for item, details in self.items.items():
            line = f"{item}: ${details['price']} x {details['quantity']} = ${details['price'] * details['quantity']}"
            receipt.append(line)
        if self.discount > 0:
            receipt.append(f"Discount applied: {self.discount}%")
        receipt.append(f"Total: ${self.total:.2f}")
        return "\n".join(receipt)
    def get_return(self):
                return=[]
                return ".join(return)
            
