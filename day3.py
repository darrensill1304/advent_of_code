data = []
with open("day3-input.txt") as file:
    for line in file:
        data.append([char for char in line.rstrip()])


def count_trees(right_slope, down_slope):
    row = col = n_trees = 0
    n_rows = len(data)

    while row < n_rows:
        # Account for wrap around
        if col > len(data[row]) - 1:
            col = col - len(data[row])

        if data[row][col] == "#":
            n_trees += 1
        row += down_slope
        col += right_slope

    return n_trees


r1d1 = count_trees(1, 1)
r3d1 = count_trees(3, 1)
r5d1 = count_trees(5, 1)
r7d1 = count_trees(7, 1)
r1d2 = count_trees(1, 2)

print("Right 1, Down 1 = {} Trees".format(r1d1))
print("Right 3, Down 1 = {} Trees. This is the solution to Part 1.".format(r3d1))
print("Right 5, Down 1 = {} Trees".format(r5d1))
print("Right 7, Down 1 = {} Trees".format(r7d1))
print("Right 1, Down 2 = {} Trees".format(r1d2))
print("Total Product: {}".format(r1d1 * r3d1 * r5d1 * r7d1 * r1d2))
