def split_num(line: str):
    numbers, indexes, symbols, cur, ind_start = [], [], [], "", None
    for i, c in enumerate(line):
        if c.isdigit():
            cur += c
            if ind_start is None:
                ind_start = i
        else:
            if c != ".":
                symbols.append(i)
            if cur:
                numbers.append(int(cur))
                indexes.append([ind_start, i-1])
                ind_start, cur = None, ""
    if cur:
        numbers.append(int(cur))
        indexes.append([ind_start, len(line)-1])
    return numbers, indexes, symbols


def check_all_conditions(cur_num, cur_ind, cur_symbol, down_symbol, up_symbol):
    to_return_bool_up, to_return_bool_down, to_return_bool_cur = [False for _ in cur_num], [False for _ in cur_num], [False for _ in cur_num]
    for j in range(len(cur_ind)):
        if cur_symbol:
            start, end = cur_ind[j]
            for i in range(start - 1, end + 2):
                if i in cur_symbol:
                    to_return_bool_cur[j] = True
        if down_symbol:
            for j in range(len(cur_ind)):
                start, end = cur_ind[j]
                for i in range(start - 1, end + 2):
                    if i in down_symbol:
                        to_return_bool_down[j] = True
        if up_symbol:
            for j in range(len(cur_ind)):
                start, end = cur_ind[j]
                for i in range(start - 1, end + 2):
                    if i in up_symbol:
                        to_return_bool_up[j] = True
    return check_all_bool(to_return_bool_cur, to_return_bool_up, to_return_bool_down, cur_num)


def check_all_bool(bool1, bool2, bool3, numbers):
    to_return = [False for _ in numbers]
    for i in range(len(numbers)):
        if bool1[i] or bool2[i] or bool3[i]:
            to_return[i] = True
    return [numbers[i] for i in range(len(numbers)) if to_return[i]]

def calc(scroll):
    symbols_up, symbols_down, numbers_to_sum = [], [], 0
    for i, line in enumerate(scroll):
        if i < len(scroll)-1:
            _, _, symbols_down = split_num(scroll[i+1])
        numbers, indexes, symbols = split_num(line)
        numbers_to_sum += sum(check_all_conditions(numbers, indexes, symbols, symbols_down, symbols_up))
        symbols_up = symbols
    return numbers_to_sum


with open('day3_input.txt', 'r') as file:
    scroll = file.read().splitlines()
print(f"ans: {calc(scroll)}")
