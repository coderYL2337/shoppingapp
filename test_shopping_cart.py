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

if __name__ == '__main__':
    unittest.main()