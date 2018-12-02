import unittest

from automaton import Automaton
from primitives.field import Field, Cell


class AutomatonTests(unittest.TestCase):

    def test_get_next_state_cell_always_alive_return_cell_alive(self):
        field = Field(8, 8)
        field.set(5, 7, Cell.ALWAYS_ALIVE)
        automaton = Automaton(field)

        sut = automaton.get_next_state(field, 5, 7)

        self.assertEqual(sut, Cell.ALWAYS_ALIVE)

    def test_get_next_state_cell_always_dead_return_cell_dead(self):
        field = Field(8, 8)
        field.set(5, 7, Cell.ALWAYS_DEAD)
        automaton = Automaton(field)

        sut = automaton.get_next_state(field, 5, 7)

        self.assertEqual(sut, Cell.ALWAYS_DEAD)

    def test_get_next_state_cell_alive_with_1_alive_neighbors_return_cell_dead(self):
        field = Field(8, 8)
        field.set(5, 7, Cell.ALWAYS_ALIVE)
        field.set(6, 6, Cell.ALIVE)
        automaton = Automaton(field)

        sut = automaton.get_next_state(field, 6, 6)

        self.assertEqual(sut, Cell.DEAD)

    def test_get_next_state_cell_alive_with_2_alive_neighbors_return_unchange_state(self):
        field = Field(8, 8)
        field.set(5, 7, Cell.ALWAYS_ALIVE)
        field.set(7, 7, Cell.ALIVE)
        field.set(6, 6, Cell.ALIVE)
        automaton = Automaton(field)

        sut = automaton.get_next_state(field, 6, 6)

        self.assertEqual(sut, Cell.ALIVE)

    def test_get_next_state_cell_dead_with_2_alive_neighbors_return_unchange_state(self):
        field = Field(8, 8)
        field.set(5, 7, Cell.ALWAYS_ALIVE)
        field.set(7, 7, Cell.ALIVE)
        automaton = Automaton(field)

        sut = automaton.get_next_state(field, 6, 6)

        self.assertEqual(sut, Cell.DEAD)

    def test_get_next_state_cell_dead_with_3_alive_neighbors_return_cell_alive(self):
        field = Field(8, 8)
        field.set(5, 7, Cell.ALWAYS_ALIVE)
        field.set(7, 7, Cell.ALIVE)
        field.set(7, 6, Cell.ALIVE)
        automaton = Automaton(field)

        sut = automaton.get_next_state(field, 6, 6)

        self.assertEqual(sut, Cell.ALIVE)

    def test_get_next_state_cell_alive_with_4_alive_neighbors_return_cell_dead(self):
        field = Field(8, 8)
        field.set(5, 7, Cell.ALWAYS_ALIVE)
        field.set(5, 5, Cell.ALIVE)
        field.set(6, 7, Cell.ALIVE)
        field.set(7, 5, Cell.ALIVE)
        field.set(6, 6, Cell.ALIVE)
        automaton = Automaton(field)

        sut = automaton.get_next_state(field, 6, 6)

        self.assertEqual(sut, Cell.DEAD)

    def test_compute_next_generation_glider_should_set_next_generation_of_glider(self):
        field = Field(8, 8)
        field.set(0, 1, Cell.ALIVE)
        field.set(1, 2, Cell.ALIVE)
        field.set(2, 2, Cell.ALIVE)
        field.set(2, 1, Cell.ALIVE)
        field.set(2, 0, Cell.ALIVE)
        automaton = Automaton(field)

        next_state_field = Field(8, 8)
        next_state_field.set(1, 0, Cell.ALIVE)
        next_state_field.set(1, 2, Cell.ALIVE)
        next_state_field.set(2, 2, Cell.ALIVE)
        next_state_field.set(2, 1, Cell.ALIVE)
        next_state_field.set(3, 1, Cell.ALIVE)

        automaton.set_next_generation()

        self.assertEqual(automaton.field, next_state_field)
