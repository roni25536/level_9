from string import ascii_lowercase
class is_panagram(object):

    def __init__(self, s):
        self.s = s

    def do_function(self):
        return set(self.s.lower()) >= set(ascii_lowercase)

