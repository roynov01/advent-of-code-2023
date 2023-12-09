class Seq:
    def __init__(self, sequence, question_num):
        self.main = [[int(s) for s in sequence]]
        self.question_num = question_num
        self.ans = self.calc()

    def calc(self):
        for level in range(len(self.main[0])):
            if not any(self.main[level]):  # for lowest level. which is only zeroes
                main = self.main.copy()
                to_add = 0
                if self.question_num == 1:
                    for level_rev in range(level, -1, -1):
                        main[level_rev].append(to_add)  # add last element
                        if level_rev > 0:
                            to_add = main[level_rev-1][-1] + main[level_rev][-1]  # calculate what is the next element on the previous line will be
                    return main[0][-1]
                elif self.question_num == 2:
                    for level_rev in range(level, -1, -1):
                        main[level_rev].insert(0, to_add)  # add last element
                        if level_rev > 0:
                            to_add = main[level_rev-1][0] - main[level_rev][0]  # calculate what is the next element on the previous line will be
                    return main[0][0]
            self.main.append([None for _ in range(len(self.main[level])-1)])  # create empty new row
            for i in range(len(self.main[level]), 0, -1):
                if i == 1:
                    break
                self.main[level + 1][i - 2] = self.main[level][i-1] - self.main[level][i-2]  # fill the new row


with open('day9_input.txt', 'r') as file:
    scroll = file.readlines()
    scroll1, scroll2 = [Seq(x.split(), 1) for x in scroll], [Seq(x.split(), 2) for x in scroll]
    count, count2 = sum([x.ans for x in scroll1]), sum([x.ans for x in scroll2])

print(f'ans1: {count}, ans2: {count2}')  # 2038472161, 1091
