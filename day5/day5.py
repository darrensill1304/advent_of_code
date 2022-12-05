# --- Day 5: Supply Stacks ---
# The expedition can depart as soon as the final supplies have been unloaded from the ships. Supplies are stored in 
# stacks of marked crates, but because the needed supplies are buried under many other crates, the crates need to be 
# rearranged.
#
# The ship has a giant cargo crane capable of moving crates between stacks. To ensure none of the crates get crushed 
# or fall over, the crane operator will rearrange them in a series of carefully-planned steps. After the crates are 
# rearranged, the desired crates will be at the top of each stack.
#
# The Elves don't want to interrupt the crane operator during this delicate procedure, but they forgot to ask her 
# which crate will end up where, and they want to be ready to unload them as soon as possible so they can embark.
#
# They do, however, have a drawing of the starting stacks of crates and the rearrangement procedure (your puzzle 
# input). For example:
#
#     [D]    
# [N] [C]    
# [Z] [M] [P]
#  1   2   3 
#
# move 1 from 2 to 1
# move 3 from 1 to 3
# move 2 from 2 to 1
# move 1 from 1 to 2
# In this example, there are three stacks of crates. Stack 1 contains two crates: crate Z is on the bottom, and crate 
# N is on top. Stack 2 contains three crates; from bottom to top, they are crates M, C, and D. Finally, stack 3 contains 
# a single crate, P.
#
# Then, the rearrangement procedure is given. In each step of the procedure, a quantity of crates is moved from one 
# stack to a different stack. In the first step of the above rearrangement procedure, one crate is moved from stack 2 to 
# stack 1, resulting in this configuration:
#
# [D]        
# [N] [C]    
# [Z] [M] [P]
#  1   2   3 
# In the second step, three crates are moved from stack 1 to stack 3. Crates are moved one at a time, so the first crate 
# to be moved (D) ends up below the second and third crates:
#
#         [Z]
#         [N]
#     [C] [D]
#     [M] [P]
#  1   2   3
# Then, both crates are moved from stack 2 to stack 1. Again, because crates are moved one at a time, crate C ends up below 
# crate M:
#
#         [Z]
#         [N]
# [M]     [D]
# [C]     [P]
#  1   2   3
# Finally, one crate is moved from stack 1 to stack 2:
#
#         [Z]
#         [N]
#         [D]
# [C] [M] [P]
#  1   2   3
# The Elves just need to know which crate will end up on top of each stack; in this example, the top crates are C in stack 1, 
# M in stack 2, and Z in stack 3, so you should combine these together and give the Elves the message CMZ.
#
# After the rearrangement procedure completes, what crate ends up on top of each stack?

import re


class Move:
    def __init__(self, n, f, t):
        self.n_moves = int(n)
        self.source = int(f) - 1
        self.dest = int(t) - 1


def parseStack(lines):
    stack = []

    for line in lines:
        i_col = 0;
        elems = line.split()
        for elem in elems:
            if len(stack) == i_col:
                stack.append([]) # First pass only. Ensure we have all arrays required
            char = re.search('[(A-Za-z)]', elem).group(0)
            if char != 'x':
                stack[i_col].insert(0, char)
            i_col = i_col + 1
    return stack


def parseMoves(lines):
    moves = []

    for line in lines:
        res = re.findall("[0-9]+", line)
        moves.append(Move(res[0], res[1], res[2]))
    return moves


def extractTopBoxes(stack):
    top_elems = []
    for col in stack:
        top_elems.append(col[-1])
    return ''.join(top_elems)


def runPart1(stack, moves):
   for move in moves:
        source_stack = stack[move.source]
        dest_stack = stack[move.dest]
        for _ in range(move.n_moves):
            dest_stack.append(source_stack.pop()) 

# --- Part Two ---
# As you watch the crane operator expertly rearrange the crates, you notice the process isn't following 
# your prediction.
#
# Some mud was covering the writing on the side of the crane, and you quickly wipe it away. The crane 
# isn't a CrateMover 9000 - it's a CrateMover 9001.
#
# The CrateMover 9001 is notable for many new and exciting features: air conditioning, leather seats, 
# an extra cup holder, and the ability to pick up and move multiple crates at once.
#
# Again considering the example above, the crates begin in the same configuration:
#
#     [D]    
# [N] [C]    
# [Z] [M] [P]
#  1   2   3 
# Moving a single crate from stack 2 to stack 1 behaves the same as before:
#
# [D]        
# [N] [C]    
# [Z] [M] [P]
#  1   2   3 
# However, the action of moving three crates from stack 1 to stack 3 means that those three moved crates 
# stay in the same order, resulting in this new configuration:
#
#         [D]
#         [N]
#     [C] [Z]
#     [M] [P]
#  1   2   3
# Next, as both crates are moved from stack 2 to stack 1, they retain their order as well:
#
#         [D]
#         [N]
# [C]     [Z]
# [M]     [P]
#  1   2   3
# Finally, a single crate is still moved from stack 1 to stack 2, but now it's crate C that gets moved:
#
#         [D]
#         [N]
#         [Z]
# [M] [C] [P]
#  1   2   3
# In this example, the CrateMover 9001 has put the crates in a totally different order: MCD.
#
# Before the rearrangement process finishes, update your simulation so that the Elves know where they should 
# stand to be ready to unload the final supplies. After the rearrangement procedure completes, what crate ends 
# up on top of each stack?

def runPart2(stack, moves):
    for move in moves:
        source = stack[move.source]
        dest = stack[move.dest]
        to_move = source[-1*move.n_moves:len(source)]
        stack[move.dest] = dest + to_move
        stack[move.source] = source[0:-1*move.n_moves]


def main():
    input_file = open("./day5_input.txt", "r")
    lines = [line.strip() for line in input_file.readlines()]

    stack_input = lines[0:8]
    moves_input = lines[10:len(lines)+1]

    stack_pt1 = parseStack(stack_input)
    stack_pt2 = parseStack(stack_input)

    moves = parseMoves(moves_input)
    
    runPart1(stack_pt1, moves)
    runPart2(stack_pt2, moves)
    
    print("Part 1: Top Elements =", extractTopBoxes(stack_pt1))
    print("Part 2: Top Elements =", extractTopBoxes(stack_pt2))
        

if __name__ == "__main__":
    main()
