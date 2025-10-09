import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
        """Create a calculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test add with positives, negatives, zeros, floats and large ints."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(0, 0), 0)
        self.assertAlmostEqual(self.calc.add(2.5, 0.75), 3.25)
        self.assertEqual(self.calc.add(10**18, 1), 10**18 + 1)

    def test_subtraction(self):
        """Test subtract with mixed signs, zero and floats."""
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(-1, -1), 0)
        self.assertEqual(self.calc.subtract(0, 5), -5)
        self.assertAlmostEqual(self.calc.subtract(5.5, 2.2), 3.3)

    def test_multiplication(self):
        """Test multiply including zero and negative values."""
        self.assertEqual(self.calc.multiply(3, 4), 12)
        self.assertEqual(self.calc.multiply(-2, 3), -6)
        self.assertEqual(self.calc.multiply(0, 100), 0)
        self.assertAlmostEqual(self.calc.multiply(2.5, 2), 5.0)

    def test_division(self):
        """Test divide for integers and floats, including negative results."""
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertAlmostEqual(self.calc.divide(7, 2), 3.5)
        self.assertEqual(self.calc.divide(-9, 3), -3)
        self.assertAlmostEqual(self.calc.divide(1, 3), 1/3)

    def test_division_by_zero(self):
        """Division by zero should return None (per implementation)."""
        self.assertIsNone(self.calc.divide(5, 0))
        self.assertIsNone(self.calc.divide(5, 0.0))

    def test_type_errors(self):
        """Operations with incompatible types should raise TypeError."""
        with self.assertRaises(TypeError):
            self.calc.add("2", 3)
        with self.assertRaises(TypeError):
            self.calc.subtract("a", "b")
        with self.assertRaises(TypeError):
            self.calc.multiply("a", 2)
        with self.assertRaises(TypeError):
            self.calc.divide("a", 1)

    def test_edge_cases(self):
        """Additional edge cases: very large multiplications and dividing large ints."""
        self.assertEqual(self.calc.multiply(10**12, 10**6), 10**18)
        self.assertAlmostEqual(self.calc.divide(10**18, 1), 10**18)

if __name__ == '__main__':
    unittest.main()