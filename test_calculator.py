import unittest
import calculator

class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calculator.add(1, 2), 3)
        self.assertEqual(calculator.add(-1, 1), 0)

    def test_sub(self):
        self.assertEqual(calculator.sub(2, 1), 1)
        self.assertEqual(calculator.sub(-1, -1), 0)

    def test_mul(self):
        self.assertEqual(calculator.mul(3, 5), 15)
        self.assertEqual(calculator.mul(1, 5), 5)

    def test_div(self):
        self.assertEqual(calculator.div(2, 1), 2)
        self.assertEqual(calculator.div(10, 5), 5)
    
    def test_mod(self):
        self.assertEqual(calculator.mod(10, 9), 1)
        self.assertEqual(calculator.mod(7, 3), 1)
    
    def test_exp(self):
        self.assertEqual(calculator.exp(4, 2), 16)
        self.assertEqual(calculator.exp(-1, -1), 0)

    def test_flrdiv(self):
        self.assertEqual(calculator.flrdiv(20, 6), 3)
        self.assertEqual(calculator.flrdiv(10, 3), 3)

    def test_sqrt(self):
        self.assertEqual(calculator.sqrt(4), 2.0)
        self.assertEqual(calculator.sqrt(16), 4.0)

    def test_fact(self):
        self.assertEqual(calculator.fact(1), 1)
        self.assertEqual(calculator.fact(2), 2)

if __name__ == '__main__':
    unittest.main()