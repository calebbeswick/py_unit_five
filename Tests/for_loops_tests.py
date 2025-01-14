import unittest
from for_loops import count
from multiplication import multiplication_table
from fibonacci import fibonacci
from multiples import get_sum


class MyTestCase(unittest.TestCase):
    def test_count(self):
        self.assertEqual("0 1 2 3 4 5 6 ", count(0, 6))
        self.assertEqual("10 9 8 7 6 ", count(10, 6))
        self.assertEqual("3 ", count(3, 3))

    def test_multiplication_tables(self):
        self.assertEqual("0 6 12 18 24 30 36 42 48 54 60 66 ", multiplication_table(6))
        self.assertEqual("0 2 4 6 8 10 12 14 16 18 20 22 ", multiplication_table(2))
        self.assertEqual("0 5 10 15 20 25 30 35 40 45 50 55 ", multiplication_table(5))
        # Create two additional tests underneath this line

    def test_fibonacci(self):
        self.assertEqual("1 1 2 3 5 ", fibonacci(5))
        self.assertEqual("1 ", fibonacci(1))
        self.assertEqual("1 1 ", fibonacci(2))
        # Create two additional tests underneath this line

    def test_multiples(self):
        self.assertEqual(233168, get_sum(1000))


if __name__ == '__main__':
    unittest.main()
