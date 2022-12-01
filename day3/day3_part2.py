"""
--- Part Two ---
Next, you should verify the life support rating, which can be determined by multiplying the oxygen generator rating by the CO2 scrubber rating.

Both the oxygen generator rating and the CO2 scrubber rating are values that can be found in your diagnostic report - finding them is the tricky part. 
Both values are located using a similar process that involves filtering out values until only one remains. Before searching for either rating value, 
start with the full list of binary numbers from your diagnostic report and consider just the first bit of those numbers. Then:

Keep only numbers selected by the bit criteria for the type of rating value for which you are searching. Discard numbers which do not match the bit criteria.
If you only have one number left, stop; this is the rating value for which you are searching.
Otherwise, repeat the process, considering the next bit to the right.
The bit criteria depends on which type of rating value you want to find:

To find oxygen generator rating, determine the most common value (0 or 1) in the current bit position, and keep only numbers with that bit in that position. 
If 0 and 1 are equally common, keep values with a 1 in the position being considered.
To find CO2 scrubber rating, determine the least common value (0 or 1) in the current bit position, and keep only numbers with that bit in that position. 
If 0 and 1 are equally common, keep values with a 0 in the position being considered.
For example, to determine the oxygen generator rating value using the same example diagnostic report from above:

Start with all 12 numbers and consider only the first bit of each number. There are more 1 bits (7) than 0 bits (5), 
so keep only the 7 numbers with a 1 in the first position: 11110, 10110, 10111, 10101, 11100, 10000, and 11001.
Then, consider the second bit of the 7 remaining numbers: there are more 0 bits (4) than 1 bits (3), 
so keep only the 4 numbers with a 0 in the second position: 10110, 10111, 10101, and 10000.
In the third position, three of the four numbers have a 1, so keep those three: 10110, 10111, and 10101.
In the fourth position, two of the three numbers have a 1, so keep those two: 10110 and 10111.
In the fifth position, there are an equal number of 0 bits and 1 bits (one each). So, to find the oxygen generator rating, keep the number with a 1 in that position: 10111.
As there is only one number left, stop; the oxygen generator rating is 10111, or 23 in decimal.
Then, to determine the CO2 scrubber rating value from the same example above:

Start again with all 12 numbers and consider only the first bit of each number. 
There are fewer 0 bits (5) than 1 bits (7), so keep only the 5 numbers with a 0 in the first position: 00100, 01111, 00111, 00010, and 01010.
Then, consider the second bit of the 5 remaining numbers: there are fewer 1 bits (2) than 0 bits (3), so keep only the 2 numbers with a 1 in the second position: 01111 and 01010.
In the third position, there are an equal number of 0 bits and 1 bits (one each). So, to find the CO2 scrubber rating, keep the number with a 0 in that position: 01010.
As there is only one number left, stop; the CO2 scrubber rating is 01010, or 10 in decimal.
Finally, to find the life support rating, multiply the oxygen generator rating (23) by the CO2 scrubber rating (10) to get 230.

Use the binary numbers in your diagnostic report to calculate the oxygen generator rating and CO2 scrubber rating, 
then multiply them together. What is the life support rating of the submarine? (Be sure to represent your answer in decimal, not binary.)
"""

def get_most_common_bit(numbers_list, idx):
    """
    Get the most common bit in the list at the given index.
    """
    bit_counts = {}
    for number in numbers_list:
        bit = number[idx]
        if bit not in bit_counts:
            bit_counts[bit] = 0
        bit_counts[bit] += 1

    return "1" if bit_counts["0"] == bit_counts["1"] else max(bit_counts, key=bit_counts.get)

input_file = open("day3/input.txt", "r")

# unpack the input file into a list of strings
input_list = input_file.read().splitlines()
# create a copy for the oxygen generator and CO2 scrubber
oxygen_list = input_list.copy()
CO2_list = input_list.copy()

for i_bit in range(len(input_list[0])):

    if len(oxygen_list) == 1 and len(CO2_list) == 1:
        break

    if len(oxygen_list) > 1:
        # Get the most common bit
        most_common_bit = get_most_common_bit(oxygen_list, i_bit)

        # Extract lines where current bit matches most common
        oxygen_list = [line for line in oxygen_list if line[i_bit] == most_common_bit]

    if len(CO2_list) > 1:
        # Get the least common bit
        most_common_bit = get_most_common_bit(CO2_list, i_bit)
        least_common_bit = '0' if most_common_bit == '1' else '1'

        # Extract lines where current bit matches least common
        CO2_list = [line for line in CO2_list if line[i_bit] == least_common_bit]
    

oxy_gen_rating = int(oxygen_list[0], 2)
CO2_scrub_rating = int(CO2_list[0], 2)

print ("Oxygen generator rating:", oxy_gen_rating)
print ("CO2 scrubber rating:", CO2_scrub_rating)
print ("Life support rating:", oxy_gen_rating * CO2_scrub_rating)
