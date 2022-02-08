class remove_at_index(object):
    def __init__(self, arr, index):
        self.arr = eval(arr)
        self.index = eval(index)

    def do_function(self):
        return self.arr[:self.index-1] + self.arr[self.index:]