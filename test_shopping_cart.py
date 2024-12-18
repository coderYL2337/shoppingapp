# test_shopping_cart.py

import unittest
from shopping_cart import ShoppingCart

class TestShoppingCart(unittest.TestCase):
    def setUp(self):
        self.cart = ShoppingCart()

    def test_add_item(self):
        self.cart.add_item("Apple", 0.50, 3)
        self.assertEqual(self.cart.items["Apple"]["quantity"], 3)
        self.assertEqual(self.cart.items["Apple"]["price"], 0.50)

    def test_update_total(self):
        self.cart.add_item("Apple", 0.50, 3)
        self.cart.add_item("Banana", 0.30, 2)
        self.assertEqual(self.cart.total, 2.10)
    
    def test_apply_discount(self):
        self.cart.add_item("Apple", 1.00, 2)
        self.cart.apply_discount(20)
        self.assertEqual(self.cart.total, 1.60)

    def test_invalid_discount(self):
        with self.assertRaises(ValueError):
            self.cart.apply_discount(150)
    
    def test_checkout(self):
        self.cart.add_item("Apple", 0.50, 3)
        self.cart.checkout()
        self.assertEqual(len(self.cart.purchase_history), 1)
        self.assertEqual(self.cart.items, {})

    def test_purchase_history(self):
        self.cart.add_item("Apple", 0.50, 3)
        self.cart.apply_discount(10)
        self.cart.checkout()
        history = self.cart.get_purchase_history()
        self.assertIn("Purchase #1:", history)
        self.assertIn("Apple: $0.5 x 3", history)
        self.assertIn("Discount applied: 10%", history)

if __name__ == '__main__':
    unittest.main()