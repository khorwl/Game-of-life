import unittest
from primitives.field import Field, Cell


class FieldTests(unittest.TestCase):
    def test_get_getting_cell_with_right_cords_should_get_cell_right(self):
        field = Field(10, 10)
        field.set(5, 5, Cell.ALWAYS_DEAD)

        sut = field.get(5, 5)

        self.assertEqual(sut, Cell.ALWAYS_DEAD)

    def test_get_getting_cell_with_out_of_range_cords_should_get_right_by_moduled_cords(self):
        field = Field(10, 10)
        field.set(6, 6, Cell.ALWAYS_ALIVE)

        sut = field.get(116, 16)

        self.assertEqual(sut, Cell.ALWAYS_ALIVE)

    def test_set_setting_cell_with_right_cords_should_set_cell_right(self):
        field = Field(10, 10)

        field.set(5, 5, Cell.ALWAYS_DEAD)

        self.assertEqual(field.get(5, 5), Cell.ALWAYS_DEAD)

    def test_set_setting_cell_with_out_of_range_cords_should_set_cell_right_by_moduled_cords(self):
        field = Field(10, 10)

        field.set(50, 50, Cell.ALWAYS_DEAD)

        self.assertEqual(field.get(0, 0), Cell.ALWAYS_DEAD)

    def test_get_neighbors_count_getting_with_out_of_range_cords_should_return_right_count(self):
        field = Field(10, 10)
        field.set(0, 0, Cell.ALIVE)
        field.set(9, 0, Cell.ALIVE)
        field.set(9, 8, Cell.ALIVE)

        sut = field.get_neighbors_count(59, 109)

        self.assertEqual(sut, 3)

    def test_get_neighbors_count_cords_in_range_should_return_right_value(self):
        field = Field(10, 10)
        field.set(4, 6, Cell.ALIVE)
        field.set(5, 6, Cell.ALIVE)
        field.set(7, 7, Cell.ALIVE)

        sut = field.get_neighbors_count(6, 6)

        self.assertEqual(sut, 2)

    def test_get_neighbors_count_cords_in_bound_should_return_right_value(self):
        field = Field(10, 10)
        field.set(0, 0, Cell.ALIVE)
        field.set(9, 0, Cell.ALIVE)
        field.set(9, 8, Cell.ALIVE)

        sut = field.get_neighbors_count(9, 9)

        self.assertEqual(sut, 3)

    def test_get_neighbors_count_cell_near_always_alive_should_count_this_cell(self):
        field = Field(10, 10)
        field.set(5, 6, Cell.ALIVE)
        field.set(7, 7, Cell.ALWAYS_ALIVE)

        sut = field.get_neighbors_count(6, 6)

        self.assertEqual(sut, 2)

    def test_get_neighbors_count_cell_near_always_dead_should_not_count_this_cell(self):
        field = Field(10, 10)
        field.set(5, 6, Cell.ALIVE)
        field.set(7, 7, Cell.ALWAYS_DEAD)

        sut = field.get_neighbors_count(6, 6)

        self.assertEqual(sut, 1)
