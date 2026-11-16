# https://github.com/gaurichirumamilla/lab11--Partner1-GC---Partner2-BN-
# Partner 1: Gauri Chirumamilla
# Partner 2: Brayden Nickum
import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)

    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(3, 5), -2)
        self.assertEqual(subtract(0, 0), 0)

    ######## Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(mul(3,5),15)
        self.assertEqual(mul(10,2),20)
        self.assertNotEqual(mul(3,5),0)

    def test_divide(self): # 3 assertions
        self.assertAlmostEqual(div(5, 12), 2.4)
        self.assertEqual(div(2, 10), 5)
        self.assertNotEqual(div(4, 8), 0)

    ######## Partner 2
    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            div(0, 5)

    def test_logarithm(self):
        self.assertAlmostEqual(logarithm(2, 8), 0.3333333)
        self.assertAlmostEqual(logarithm(10, 100), 0.5)
        self.assertAlmostEqual(logarithm(5, 5), 1.0)

    def test_log_invalid_base(self):
        with self.assertRaises(ZeroDivisionError):
            logarithm(1, 10)
        with self.assertRaises(ZeroDivisionError):
            logarithm(0, 10)
        with self.assertRaises(ZeroDivisionError):
            logarithm(2, -8)
    
    ######## Partner 1
    def test_log_invalid_argument(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm("hi", 5)

    def test_hypotenuse(self): # 3 assertions
        self.assertEqual(hypotenuse(3, 4), 5)
        self.assertAlmostEqual(hypotenuse(10, 2), 10.1980390)
        self.assertNotEqual(hypotenuse(7, 9), 10)

    def test_sqrt(self): # 3 assertions
        with self.assertRaises(ValueError):
            square_root(-4)
        self.assertEqual(square_root(4), 2)
        self.assertEqual(square_root(9), 3)

# Do not touch this
if __name__ == "__main__":
    unittest.main()