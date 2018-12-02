from primitives.cell import *


class Field:
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.field = []
        for i in range(height):
            self.field.append([Cell.DEAD] * width)

    def get(self, y, x):
        x = x % self.width
        y = y % self.height
        return self.field[y][x]

    def set(self, y, x, state):
        self.field[y % self.height][x % self.width] = state

    def get_neighbors_count(self, y, x):
        count = 0
        x = x % self.width
        y = y % self.height
        for i in range(y - 1, y + 2):
            for j in range(x - 1, x + 2):
                if i == y and j == x:
                    continue
                if self.get(i % self.height, j % self.width) == Cell.ALIVE \
                        or self.get(i % self.height, j % self.width) == Cell.ALWAYS_ALIVE:
                    count += 1
        return count

    def __eq__(self, other):
        if not isinstance(other, Field):
            return False
        if self.height != other.height or self.width != other.width:
            return False

        for i in range(self.width):
            for j in range(self.height):
                if self.get(i, j) != other.get(i, j):
                    return False
        return True
