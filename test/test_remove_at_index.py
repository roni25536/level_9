import unittest

from lib.remove_at_index import remove_at_index


class MyTestCase(unittest.TestCase):

    def test_remove_at_index_first(self):
        remove_at_index_obj = remove_at_index("[12,56,23,98,54]", "1")
        res = [56, 23, 98, 54]
        self.assertEqual(res, remove_at_index_obj.do_function())

    def test_remove_at_index_last(self):
        remove_at_index_obj = remove_at_index("[12,56,23,98,54]", "5")
        res = [12, 56, 23, 98]
        self.assertEqual(res, remove_at_index_obj.do_function())

    def test_remove_at_index_middle(self):
        remove_at_index_obj = remove_at_index("[12,56,23,98,54]", "3")
        res = [12, 56, 98, 54]
        self.assertEqual(res, remove_at_index_obj.do_function())


if __name__ == '__main__':
    unittest.main()
