from num import NUM
from sym import SYM

class COLS:
    def _init_(self, row):
        self.x = {}
        self.y = {}
        self.all = []
        self.klass = None
        self.names = row.cells

        for at, txt in enumerate(row.cells):
            col = (txt.find("^[A-Z]") and NUM or SYM)(txt, at)
            self.all.append(col)
            if not txt.find("X$"):
                if txt.find("!$"):
                    self.klass = col
                (txt.find("[!+-]$") and self.y or self.x)[at] = col

    def add(self, row):
        for _, cols in [(self.x, self.y)]:
            for _, col in enumerate(cols):
                col.add(row.cells[col.at])
        return row
