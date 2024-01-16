import csv
from row import ROW
from cols import COLS

class DATA:
    def _init_(self, src, fun=None):
        self.rows = []
        self.cols = None

        if isinstance(src, str):
            with open(src, 'r') as file:
                csv_reader = csv.reader(file)
                for _, row_data in enumerate(csv_reader):
                    row = ROW(row_data)
                    self.add(row, fun)
        else:
            for _, row_data in enumerate(src or []):
                row = ROW(row_data)
                self.add(row, fun)

    def add(self, row, fun=None):
        if self.cols:
            if fun:
                fun(self, row)
            self.rows.append(self.cols.add(row))
        else:
            self.cols = COLS(row)

    def mid(self, cols=None, u=None):
        u = []
        for _, col in enumerate(cols or self.cols.all):
            u.append(col.mid())
        return ROW(u)

    def div(self, cols=None, u=None):
        u = []
        for _, col in enumerate(cols or self.cols.all):
            u.append(col.div())
        return ROW(u)
