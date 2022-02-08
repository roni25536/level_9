import unittest
from lib.question_2 import question_2


class MyTestCase(unittest.TestCase):
    def test_question_2(self):
        question_2_obj = question_2()
        self.assertEqual(question_2_obj.do_function(), 1)

if __name__ == '__main__':
    unittest.main()
