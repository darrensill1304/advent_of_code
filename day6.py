import numpy as np
import string


questions = []
count = 0

with open('day6-input.txt') as file:
    for line in file:
        if line == '\n':
            matched_answers = np.logical_and.reduce(questions)
            count += np.count_nonzero(matched_answers)
            questions = []
        else:
            letters = [char for char in line.rstrip()]
            individual_answer = np.zeros(26, dtype=bool)
            for char in letters:
                idx = string.ascii_lowercase.index(char)
                individual_answer[idx] = True
            questions.append(individual_answer)

print("Count: {}".format(count))
