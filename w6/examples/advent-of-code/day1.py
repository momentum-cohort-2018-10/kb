# 1. read the text file
# 2. read each line in the text file
# 3. convert each line to an integer
# 4. put those integers into an array
# 5. add the integers up

from itertools import cycle


def get_freq_changes():
    frequencies = []
    with open("day1.txt") as data_file:
        for num in data_file:
            num = num.strip()
            num = int(num)
            frequencies.append(num)
    return frequencies


freq_changes = get_freq_changes()
print("problem 1", sum(freq_changes))


def run_through_freq(freq_changes):
    freq_set = set()
    num_total = 0

    for num in cycle(freq_changes):
        freq_set.add(num_total)
        num_total += num
        if num_total in freq_set:
            return num_total


print("problem 2", run_through_freq(freq_changes))
