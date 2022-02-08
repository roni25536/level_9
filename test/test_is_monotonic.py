import unittest
from lib.is_monotonic import is_monotonic


class MyTestCase(unittest.TestCase):
    def test_is_monotonic(self):
        is_monotonic_obj = is_monotonic("[2,16,54,456]")
        self.assertTrue(is_monotonic_obj.do_function())

    def test_is_monotonic_with_even(self):
        is_monotonic_obj = is_monotonic("[2,2,16,54,54,54,456]")
        self.assertTrue(is_monotonic_obj.do_function())

    def test_is_not_monotonic(self):
        is_monotonic_obj = is_monotonic("[2,2,16,54,540,54,456]")
        self.assertFalse(is_monotonic_obj.do_function())


if __name__ == '__main__':
    unittest.main()
