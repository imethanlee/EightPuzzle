class Puzzle:
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    dir = ["u", "d", "l", "r"]
    TARGET = 247893796
    N = 3

    def __init__(self):
        self.x = [0 for i in range(9)]
        self.space = -1
        self.id = 0
        self.path = ""
        self.depth = 0

    def init(self, x_in, path):
        for i in range(9):
            self.x[i] = x_in[i]
            if self.x[i] == 0:
                self.space = i
        self.path = path
        self.get_id()

    def is_target(self):
        if self.id == Puzzle.TARGET:
            return True
        else:
            return False

    def swap(self, space, target):
        t1, t2 = self.x[space], self.x[target]
        self.x[space] = t2
        self.x[target] = t1
        self.space = target
        self.get_id()

    def get_id(self):
        self.id = 0
        for i in range(9):
            self.id = self.id + self.x[i] * pow(9, i)

    def __lt__(self, other):
        return self.f() < other.f()

    def f(self):
        misplace = 0
        if self.x[0] != 1:
            misplace = misplace + 1
        if self.x[1] != 2:
            misplace = misplace + 1
        if self.x[2] != 3:
            misplace = misplace + 1
        if self.x[3] != 8:
            misplace = misplace + 1
        if self.x[4] != 0:
            misplace = misplace + 1
        if self.x[5] != 4:
            misplace = misplace + 1
        if self.x[6] != 7:
            misplace = misplace + 1
        if self.x[7] != 6:
            misplace = misplace + 1
        if self.x[8] != 5:
            misplace = misplace + 1
        return misplace + self.depth

    def set_depth(self, depth):
        self.depth = depth

