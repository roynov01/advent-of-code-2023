import time as t

with open('day5_input.txt', 'r') as file:
    time, record = [x for x in file.readline().split()[1:]], [x for x in file.readline().split()[1:]]
    time2, record2 = ["".join(time)], ["".join(record)]

def calc(time, record):
    wins_each_race = []
    for race in range(len(time)):
        acceleration, cur_count = 0, 0
        for mili in range(int(time[race])):
            acceleration += 1
            if acceleration * (int(time[race])-mili-1) > int(record[race]):
                cur_count += 1
        wins_each_race += [cur_count]
    results = 1
    for i in wins_each_race:
        results *= i
    return results

def calc2(time, record):
    acceleration, start = 0, 0
    for mili in range(time):
        acceleration += 1
        if acceleration * (time - mili - 1) > int(record):
            start = mili + 1
            break
    for mili in range(time, 0, -1):
        if mili * (time - mili) > int(record):
            return mili - start +1

print(f"ans1: {calc(time, record)}")
start = t.time()
print(f"ans2_boring: {calc(time2, record2)}, in {round(t.time()-start,2)} seconds")
start = t.time()
print(f"ans2_amazing: {calc2(int(time2[0]), int(record2[0]))}, in {round(t.time()-start)} seconds")

