import unittest

from day0.code import read_string_and_reverse


class MyTestCase(unittest.TestCase):
    def test_should_reverse_one_string(self):
        self.assertEqual(read_string_and_reverse('ABC'), 'CBA')

    def test_should_reverse_one_letter(self):
        self.assertEqual(read_string_and_reverse('A'), 'A')

    def test_should_reverse_a_string(self):
        self.assertEqual(read_string_and_reverse('Bubu Zuzu'), 'ubuB uzuZ')

    def test_should_not_crash_for_numbers(self):
        self.assertEqual(read_string_and_reverse(12345673), '37654321')


if __name__ == '__main__':
    unittest.main()
