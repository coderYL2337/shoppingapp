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

if __name__ == '__main__':
    unittest.main()