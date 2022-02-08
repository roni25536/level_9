class second_biggest_number(object):
    def __init__(self, arr):
        self.arr = eval(arr)

    def do_function(self):
        return sorted(self.arr)[-2]