import unittest

from day3.code import get_number_of_trees
from day3.code import create_array_from_input


class MyTestCase(unittest.TestCase):
    def test_should_return_correct_value_for_test_data(self):
        self.assertEqual(get_number_of_trees(create_array_from_input(open('input_test.txt', 'r').readlines())), 7)

    def test_should_return_correct_value_for_real_data(self):
        self.assertEqual(get_number_of_trees(create_array_from_input(open('input_real.txt', 'r').readlines())), 252)


if __name__ == '__main__':
    unittest.main()
