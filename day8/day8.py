# --- Day 8: Treetop Tree House ---
# The expedition comes across a peculiar patch of tall trees all planted carefully in a grid. 
# The Elves explain that a previous expedition planted these trees as a reforestation effort. 
# Now, they're curious if this would be a good location for a tree house.
#
# First, determine whether there is enough tree cover here to keep a tree house hidden. To do 
# this, you need to count the number of trees that are visible from outside the grid when looking 
# directly along a row or column.
#
# The Elves have already launched a quadcopter to generate a map with the height of each tree 
# (your puzzle input). For example:
#
# 30373
# 25512
# 65332
# 33549
# 35390
# Each tree is represented as a single digit whose value is its height, where 0 is the shortest 
# and 9 is the tallest.
#
# A tree is visible if all of the other trees between it and an edge of the grid are shorter than it. 
# Only consider trees in the same row or column; that is, only look up, down, left, or right from any 
# given tree.
#
# All of the trees around the edge of the grid are visible - since they are already on the edge, 
# there are no trees to block the view. In this example, that only leaves the interior nine trees 
# to consider:
#
# The top-left 5 is visible from the left and top. (It isn't visible from the right or bottom since 
#                                                   other trees of height 5 are in the way.)
# The top-middle 5 is visible from the top and right.
# The top-right 1 is not visible from any direction; for it to be visible, there would need to only be 
# trees of height 0 between it and an edge.
# The left-middle 5 is visible, but only from the right.
# The center 3 is not visible from any direction; for it to be visible, there would need to be only trees 
# of at most height 2 between it and an edge.
# The right-middle 3 is visible from the right.
# In the bottom row, the middle 5 is visible, but the 3 and 4 are not.
# With 16 trees visible on the edge and another 5 visible in the interior, a total of 21 trees are visible 
# in this arrangement.
#
# Consider your map; how many trees are visible from outside the grid?

def is_visible_up(irow, icol, grid):
    if irow == 0:
        return True

    val = grid[irow][icol]
    for ir in range(irow, 0, -1):
        if grid[ir-1][icol] >= val:
            return False
    return True


def is_visible_down(irow, icol, grid):
    if irow == len(grid) - 1:
        return True

    val = grid[irow][icol]
    for ir in range(irow, len(grid)-1):
        if grid[ir+1][icol] >= val:
            return False
    return True


def is_visible_left(irow, icol, grid):
    if icol == 0:
        return True

    val = grid[irow][icol]
    for ic in range(icol, 0, -1):
        if grid[irow][ic-1] >= val:
            return False
    return True


def is_visible_right(irow, icol, grid):
    if icol == len(grid[0]) - 1:
        return True

    val = grid[irow][icol]
    for ic in range(icol, len(grid[0])-1):
        if grid[irow][ic+1] >= val:
            return False
    return True


def is_visible(irow, icol, grid):
    return is_visible_up(irow, icol, grid) or \
            is_visible_right(irow, icol, grid) or \
            is_visible_down(irow, icol, grid) or \
            is_visible_left(irow, icol, grid)


def run_part1(grid):
    total = 0
    for irow in range(len(grid)):
        for icol in range(len(grid[0])):
            if is_visible(irow, icol, grid):
                total = total + 1

    print("Part 1: Total =", total)

# --- Part Two ---
# Content with the amount of tree cover available, the Elves just need to know the best spot to build their 
# tree house: they would like to be able to see a lot of trees.
#
# To measure the viewing distance from a given tree, look up, down, left, and right from that tree; stop if 
# you reach an edge or at the first tree that is the same height or taller than the tree under consideration. 
# (If a tree is right on the edge, at least one of its viewing distances will be zero.)
#
# The Elves don't care about distant trees taller than those found by the rules above; the proposed tree house 
# has large eaves to keep it dry, so they wouldn't be able to see higher than the tree house anyway.
#
# In the example above, consider the middle 5 in the second row:
#
# 30373
# 25512
# 65332
# 33549
# 35390
# Looking up, its view is not blocked; it can see 1 tree (of height 3).
# Looking left, its view is blocked immediately; it can see only 1 tree (of height 5, right next to it).
# Looking right, its view is not blocked; it can see 2 trees.
# Looking down, its view is blocked eventually; it can see 2 trees (one of height 3, then the tree of height 5 
# that blocks its view).
# A tree's scenic score is found by multiplying together its viewing distance in each of the four directions. 
# For this tree, this is 4 (found by multiplying 1 * 1 * 2 * 2).
#
# However, you can do even better: consider the tree of height 5 in the middle of the fourth row:
#
# 30373
# 25512
# 65332
# 33549
# 35390
# Looking up, its view is blocked at 2 trees (by another tree with a height of 5).
# Looking left, its view is not blocked; it can see 2 trees.
# Looking down, its view is also not blocked; it can see 1 tree.
# Looking right, its view is blocked at 2 trees (by a massive tree of height 9).
# This tree's scenic score is 8 (2 * 2 * 1 * 2); this is the ideal spot for the tree house.
#
# Consider each tree on your map. What is the highest scenic score possible for any tree?

def get_score_up(irow, icol, grid):
    if irow == 0:
        return 0
   
    ir = irow - 1
    val = grid[irow][icol]
    score = 0

    while ir >= 0:
        score = score + 1
        if grid[ir][icol] >= val:
            return score
        ir = ir - 1
    return score


def get_score_right(irow, icol, grid):
    if icol == len(grid[0]) - 1:
        return 0

    ic = icol + 1
    val = grid[irow][icol]
    score = 0
    while ic <= len(grid[0]) - 1:
        score = score + 1
        if grid[irow][ic] >= val:
            return score
        ic = ic + 1
    return score


def get_score_down(irow, icol, grid):
    if irow == len(grid) - 1:
        return 0

    ir = irow + 1
    val = grid[irow][icol]
    score = 0

    while ir <= len(grid) - 1:
        score = score + 1
        if grid[ir][icol] >= val:
            return score
        ir = ir + 1
    return score


def get_score_left(irow, icol, grid):
    if icol == 0:
        return 0

    ic = icol - 1
    val = grid[irow][icol]
    score = 0

    while ic >= 0:
        score = score + 1
        if grid[irow][ic] >= val:
            return score
        ic = ic - 1
    return score


def run_part2(grid):
    max_score = 0

    for irow in range(len(grid)):
        for icol in range(len(grid[0])):
            score = get_score_up(irow, icol, grid) * \
                    get_score_right(irow, icol, grid) * \
                    get_score_down(irow, icol, grid) * \
                    get_score_left(irow, icol, grid)
            max_score = max(max_score, score)

    print("Part 2: Max Score =", max_score)


def main():
    input_file = open("./day8_input.txt", "r")
    grid = [line.strip() for line in input_file.readlines()]

    run_part1(grid)
    run_part2(grid)

if __name__ == "__main__":
    main()


