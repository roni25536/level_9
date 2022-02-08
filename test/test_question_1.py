import unittest
from lib.question_1 import question_1


class MyTestCase(unittest.TestCase):
    def test_question_1(self):
        question_1_obj = question_1()
        self.assertEqual(question_1_obj.do_function(), 4)


if __name__ == '__main__':
    unittest.main()
