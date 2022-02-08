from math import sqrt

class is_prime(object):
    def __init__(self, n):
        self.n = eval(n)

    def do_function(self):
        return self.n > 1 and all(self.n % i != 0 for i in range(2, int(sqrt(self.n)) + 1))
