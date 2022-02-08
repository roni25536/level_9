import unittest
from lib.is_prime import is_prime


class MyTestCase(unittest.TestCase):
    def test_is_prime_0(self):
        is_prime_obj = is_prime("0")
        self.assertFalse(is_prime_obj.do_function())

    def test_is_prime_1(self):
        is_prime_obj = is_prime("1")
        self.assertFalse(is_prime_obj.do_function())

    def test_is_prime(self):
        is_prime_obj = is_prime("19")
        self.assertTrue(is_prime_obj.do_function())

    def test_not_is_prime(self):
        is_prime_obj = is_prime("42")
        self.assertFalse(is_prime_obj.do_function())


if __name__ == '__main__':
    unittest.main()
