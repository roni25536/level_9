from sys import argv

from lib.is_monotonic import is_monotonic
from lib.is_panagram import is_panagram
from lib.is_prime import is_prime
from lib.question_1 import question_1
from lib.question_2 import question_2
from lib.remove_at_index import remove_at_index
from lib.second_biggest_number import second_biggest_number

if __name__ == '__main__':

    if argv[1] == 'removeAtIndex':
        obj = remove_at_index(argv[2], argv[3])
    elif argv[1] == 'is_prime':
        obj = is_prime(argv[2])
    elif argv[1] == 'is_monotonic':
        obj = is_monotonic(argv[2])
    elif argv[1] == 'second_biggest_number':
        obj = second_biggest_number(argv[2])
    elif argv[1] == 'is_panagram':
        obj = is_panagram(argv[2])
    elif argv[1] == 'question_1':
        obj = question_1()
    elif argv[1] == 'question_2':
        obj = question_2()
    print(obj.do_function())
