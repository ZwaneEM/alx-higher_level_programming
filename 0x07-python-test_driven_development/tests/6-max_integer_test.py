#!/usr/bin/python3

from max_integer import max_integer
import unittest

class Test_case(unittest.TestCase):

    def test_max_integer_normal_case(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)


if __name__ == '__main__':

    unittest.main(argv=['first-arg-is-ignored'], exit=False)
