from numpy import loadtxt

inputData = loadtxt("./day1-input.txt", delimiter="\n", unpack=False)

# Part 1

found = False
answer = -1

for ii in range(len(inputData)):
    for jj in range(ii+1, len(inputData)):
        if inputData[ii] + inputData[jj] == 2020:
            found = True
            answer = inputData[ii] * inputData[jj]
            break
    if found:
        break

if found:
    print("Part 1 Answer: {}".format(answer))
else:
    print("Oops. Your code is shit.")

# Part 2
found = False
answer = -1

for ii in range(len(inputData)):
    for jj in range(ii+1, len(inputData)):
        for kk in range(len(inputData)):
            if kk != ii and kk != jj:
                if inputData[ii] + inputData[jj] + inputData[kk] == 2020:
                    found = True
                    answer = inputData[ii] * inputData[jj] * inputData[kk]
                    break
            if found:
                break
    if found:
        break

if found:
    print("Part 2 Answer: {}".format(answer))
else:
    print("Oops. Your code is shit part 2.")
