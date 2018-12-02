from primitives.field import Field, Cell

MAX_SIZE = 25


def generate_field(n, m):
    size = n * m
    if size > MAX_SIZE:
        raise ValueError('too much field size')

    for i in generate_numbers(size):
        yield from_number_to_field(i, n, m)


def generate_numbers(size):
    for i in range(2 ** size):
        yield bin(i)[2:].zfill(size)


def from_number_to_field(num, n, m):
    field = Field(n, m)
    idx = 0

    for i in range(n):
        for j in range(m):
            if num[idx] == '0':
                field.set(i, j, Cell.DEAD)
            else:
                field.set(i, j, Cell.ALIVE)
            idx += 1

    return field
