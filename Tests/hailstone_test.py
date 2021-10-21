import unittest
from hailstone import sequence


class MyTestCase(unittest.TestCase):

    def test_hailstone(self):
        self.assertEqual(10, sequence(13))
        self.assertEqual(11, sequence(26))
        self.assertEqual(112, sequence(1000))
        # Create two additional tests underneath this line


if __name__ == '__main__':
    unittest.main()
