def is_valid(data):
    initial_split = data.split(":")
    pwd = initial_split[1][1:-1]

    second_split = initial_split[0].split(" ")
    char = second_split[1]

    bounds = second_split[0].split("-")
    lower = int(bounds[0])
    upper = int(bounds[1])

    # Uncomment below for Part 1
    # count = pwd.count(char)
    # return lower <= count <= upper

    # Uncomment below for Part 2
    return (pwd[lower-1] == char) ^ (pwd[upper-1] == char)


valid_count = 0

file = open("day2-input.txt", "r")
for line in file:
    if is_valid(line):
        valid_count += 1

print("Number of Valid Passwords: {}".format(valid_count))
