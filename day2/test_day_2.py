import unittest

from day2.code import get_valid_sets


class MyTestCase(unittest.TestCase):
    def test_should_return_correct_value_for_test_data(self):
        self.assertEqual(get_valid_sets(open('input_test.txt', 'r').readlines()), 1)

    def test_should_return_correct_value_for_real_data(self):
        self.assertEqual(get_valid_sets(open('input_real.txt', 'r').readlines()), 294)


if __name__ == '__main__':
    unittest.main()
