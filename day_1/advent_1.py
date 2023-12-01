numbers_dict = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}
minimal_length = min([len(x) for x in numbers_dict]) - 1


def part1(text):
    numbers = [None, None]
    for char in text:
        if char in numbers_dict.values() or char == "0":
            if numbers[0] is None:
                numbers[0] = char
            else:
                numbers[1] = char
    if not any(numbers):
        return 0
    if numbers[1] is None:
        numbers[1] = numbers[0]
    return int(f'{numbers[0]}{numbers[1]}')


def part2(text):
    for i in range(minimal_length, len(text)):
        for key, val in numbers_dict.items():
            if key in text[:i]:
                text = text.replace(key, val+key[1:])
    return part1(text)


with open('advent_code/day1_input.txt', 'r') as file:
    scroll = file.readlines()
ans1 = sum([part1(row) for row in scroll])
ans2 = sum([part2(row) for row in scroll])
print(f"ans1: {ans1}\nans2: {ans2}")
