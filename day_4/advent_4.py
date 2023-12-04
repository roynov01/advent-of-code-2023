import sys
sys.setrecursionlimit(5000)
def q1(scroll):
    points = 0
    for line in scroll:
        line = line.split(": ")[1]
        winning, numbers = line.split(" | ")
        # winning = set(winning.replace("  ", " ").replace("   ", " ").replace("    ", " ").split(" "))
        # numbers = set(numbers.replace("  ", " ").replace("   ", " ").replace("    ", " ").split(" "))
        winning = winning.split()
        numbers = numbers.split()
        count = -1
        for num in numbers:
            if num in winning:
                count += 1
        if count != -1:
            points += 2**count
    return points


def how_many(line):
    line = line.split(": ")[1]
    winning, numbers = line.split(" | ")
    winning = winning.split()
    numbers = numbers.split()
    count = 0
    for num in numbers:
        if num in winning:
            count += 1
    return count

def q2(scroll):
    res = [0]
    for i, line in enumerate(scroll):
        helper(i, res)

    return res[0]

def helper(index, res):
    res[0] += 1
    if index >= len(scroll)-1:
        return
    print(index)
    right = how_many(scroll[index])
    for j in range(right):
        helper(index+j+1, res)

    return





#
with open('day4_input.txt', 'r') as file:
# with open('day_4_q1.txt', 'r') as file:
    scroll = file.read().splitlines()
#
# scroll = [
# "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53",
# "Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19",
# "Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1",
# "Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83",
# "Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36",
# "Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11",
# ]

ans1 = q1(scroll)
ans2 = q2(scroll)
print(f"ans1: {ans1}\nans2: {ans2}")
