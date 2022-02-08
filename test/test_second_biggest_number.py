import unittest
from lib.second_biggest_number import second_biggest_number


class MyTestCase(unittest.TestCase):
    def test_second_biggest_number(self):
        second_biggest_number_obj = second_biggest_number("[52,12,45,23,12,76]")
        number = 52
        self.assertEqual(number, second_biggest_number_obj.do_function())

    def test_second_biggest_number_two_numbers(self):
        second_biggest_number_obj = second_biggest_number("[52,12]")
        number = 12
        self.assertEqual(number, second_biggest_number_obj.do_function())


if __name__ == '__main__':
    unittest.main()
