import unittest

from day1.code import get_pair_that_adds_to_2020
from day1.code import get_triple_that_adds_to_2020


class MyTestCase(unittest.TestCase):
    def test_should_return_correct_pair_value_for_test_data(self):
        self.assertEqual(get_pair_that_adds_to_2020(open('input_test.txt', 'r').readlines()), 514579)

    def test_should_return_correct_triple_value_for_test_data(self):
        self.assertEqual(get_triple_that_adds_to_2020(open('input_test.txt', 'r').readlines()), 241861950)


if __name__ == '__main__':
    unittest.main()
