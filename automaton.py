from primitives.field import *
from primitives.cell import *
from random import *

from tools.generator import generate_field


class Automaton:
    def __init__(self, field: Field):
        self.field = field
        self.field_height = field.height
        self.field_width = field.width
        # self.iteration_figures = iteration_figures

    @staticmethod
    def get_next_state(field, y, x):
        if field.get(y, x) == Cell.ALWAYS_ALIVE or field.get(y, x) == Cell.ALWAYS_DEAD:
            return field.get(y, x)

        count = field.get_neighbors_count(y, x)
        if count < 2 or count > 3:
            return Cell.DEAD
        if count == 2:
            return field.get(y, x)
        if count == 3:
            return Cell.ALIVE

    def generate_first_generation(self):
        for i in range(self.field_height):
            for j in range(self.field_width):
                self.field.set(i, j, Cell.ALIVE if randint(0, 1) == 1 else Cell.DEAD)

    def set_next_generation(self):
        self.field = self.compute_next_generation(self.field)

    def compute_next_generation(self, field):
        temp_field = Field(self.field_height, self.field_width)

        for i in range(field.height):
            for j in range(field.width):
                temp_field.set(i, j, self.get_next_state(field, i, j))

        return temp_field

    @property
    def get_previous_field(self):
        for i in generate_field(self.field_height, self.field_width):
            if self.compute_next_generation(i) == self.field:
                return i

        return False

    def set_previous_position(self):
        previous = self.get_previous_field

        if previous:
            self.field = previous
        else:
            print('can\'t found previous generation')
            raise ValueError('can\'t found previous generation')
