import unittest
from lib.is_panagram import is_panagram


class MyTestCase(unittest.TestCase):
    def test_is_panagram(self):
        is_panagram_obj = is_panagram("AbCdEfghijklmnopqrsdfsdffs*(*^(*^24stuvwxyz")
        self.assertTrue(is_panagram_obj.do_function())

    def test_is_not_panagram(self):
        is_panagram_obj = is_panagram("AbCdfghijklmnopqrsdfsdffs*(*^(*^24stuvwxyz")
        self.assertFalse(is_panagram_obj.do_function())


if __name__ == '__main__':
    unittest.main()
