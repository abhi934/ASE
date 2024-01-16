class NUM:
    def __init__(self, s=None, n=None):
        self.txt = s or " "
        self.at = n or 0
        self.n = 0
        self.mu = 0
        self.m2 = 0
        self.hi = -1E30
        self.lo = 1E30
        self.heaven = (s or "").find("-$") and 0 or 1

    def add(self, x):
        if x != "?":
            self.n += 1
            d = x - self.mu
            self.mu += d / self.n
            self.m2 += d * (x - self.mu)
            self.lo = min(x, self.lo)
            self.hi = max(x, self.hi)

    def mid(self):
        return self.mu

    def div(self):
        return self.n < 2 and 0 or (self.m2 / (self.n - 1)) ** 0.5

    def norm(self, x):
        return x == "?" and x or (x - self.lo) / (self.hi - self.lo + 1E-30)

