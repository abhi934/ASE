import math


class SYM:
    def __init__(self, s=None, n=None):
        self.txt = s or " "
        self.at = n or 0
        self.n = 0
        self.has_dict = {}
        self.mode = None
        self.most = 0

    def add(self, x):
        if x != "?":
            self.n += 1
            self.has_dict[x] = 1 + (self.has_dict.get(x, 0) or 0)
            if self.has_dict[x] > self.most:
                self.most, self.mode = self.has_dict[x], x

    def mid(self):
        return self.mode

    def div(self):
        entropy = 0
        for _, v in self.has_dict.items():
            entropy -= v / self.n * math.log(v / self.n, 2)
        return entropy

    def small(self):
        return 0


