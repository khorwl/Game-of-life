import unittest

from primitives.field import Field, Cell
from tools.generator import generate_numbers, generate_field


class GenerateNumbersTests(unittest.TestCase):

    def test_generate_numbers_generating_with_valid_argument_should_return_right_value(self):
        size = 2
        numbers = list(generate_numbers(size))

        self.assertEqual(numbers, ['00', '01', '10', '11'])

    def test_from_number_to_field_with__valid_arguments(self):
        n = 1
        m = 2
        field1 = Field(n, m)
        field2 = Field(n, m)
        field2.set(0, 1, Cell.ALIVE)
        field3 = Field(n, m)
        field3.set(0, 0, Cell.ALIVE)
        field4 = Field(n, m)
        field4.set(0, 1, Cell.ALIVE)
        field4.set(0, 0, Cell.ALIVE)
        fields = [field1, field2, field3, field4]
        actual = list()

        for i in generate_field(n, m):
            actual.append(i)

        self.assertEqual(actual, fields)
