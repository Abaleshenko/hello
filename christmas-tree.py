
from random import choice

# FOREST
def find(scale, icon):
    matrix = [[choice('.*🎄%#&') for _ in range(scale)] for _ in range(scale)]
    coord = []

    for row in matrix:
        print(' '.join(row))
    print()

    for row in range(len(matrix)):
        for column in range(len(matrix[row])):
            if matrix[row][column] == icon:
                coord.append(f'({row}, {column})')

    return f"Found {len(coord) or None}"



print(find(52, '🎄'))
print()