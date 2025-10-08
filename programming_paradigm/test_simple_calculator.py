import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    """Test class for SimpleCalculator methods."""

    def setUp(self):
        """Set up a SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_add(self):
        """Test the addition method with various inputs."""
        # Test positive numbers
        self.assertEqual(self.calc.add(2, 3), 5)
        # Test negative numbers
        self.assertEqual(self.calc.add(-1, -1), -2)
        # Test positive and negative
        self.assertEqual(self.calc.add(-1, 1), 0)
        # Test with zero
        self.assertEqual(self.calc.add(0, 5), 5)
        self.assertEqual(self.calc.add(5, 0), 5)
        # Test decimal numbers
        self.assertEqual(self.calc.add(2.5, 3.5), 6.0)

    def test_subtract(self):
        """Test the subtraction method with various inputs."""
        # Test positive numbers
        self.assertEqual(self.calc.subtract(5, 3), 2)
        # Test negative result
        self.assertEqual(self.calc.subtract(3, 5), -2)
        # Test negative numbers
        self.assertEqual(self.calc.subtract(-1, -1), 0)
        # Test with zero
        self.assertEqual(self.calc.subtract(5, 0), 5)
        self.assertEqual(self.calc.subtract(0, 5), -5)
        # Test decimal numbers
        self.assertEqual(self.calc.subtract(5.5, 2.5), 3.0)

    def test_multiply(self):
        """Test the multiplication method with various inputs."""
        # Test positive numbers
        self.assertEqual(self.calc.multiply(2, 3), 6)
        # Test negative numbers
        self.assertEqual(self.calc.multiply(-2, -3), 6)
        # Test positive and negative
        self.assertEqual(self.calc.multiply(-2, 3), -6)
        # Test with zero
        self.assertEqual(self.calc.multiply(5, 0), 0)
        self.assertEqual(self.calc.multiply(0, 5), 0)
        # Test decimal numbers
        self.assertEqual(self.calc.multiply(2.5, 2), 5.0)

    def test_divide(self):
        """Test the division method with various inputs."""
        # Test positive numbers
        self.assertEqual(self.calc.divide(6, 3), 2.0)
        # Test negative numbers
        self.assertEqual(self.calc.divide(-6, -3), 2.0)
        # Test positive and negative
        self.assertEqual(self.calc.divide(-6, 3), -2.0)
        # Test with zero numerator
        self.assertEqual(self.calc.divide(0, 5), 0.0)
        # Test division by zero
        self.assertIsNone(self.calc.divide(5, 0))
        # Test decimal numbers
        self.assertEqual(self.calc.divide(5.0, 2.0), 2.5)

if __name__ == "__main__":
    unittest.main()