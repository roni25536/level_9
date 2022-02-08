class is_monotonic(object):
    def __init__(self, arr):
        self.arr = eval(arr)

    def do_function(self):
        return all(self.arr[i] <= self.arr[i+1] for i in range(len(self.arr)-1))