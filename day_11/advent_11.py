class Galaxy:
    galaxies = []
    total_dist = 0

    def __init__(self, x, y):
        self.x, self.y = x, y
        self.update_distances()
        Galaxy.galaxies.append(self)

    def __add__(self, other):
        return abs(self.x - other.x) + abs(self.y - other.y)

    def update_distances(self):
        for gal in Galaxy.galaxies:
            Galaxy.total_dist += (gal + self)
            # print(f'distance_between ({gal.x},{gal.y}) ({self.x},{self.y}): {(gal + self)}, total: {Galaxy.total_dist}')

    @classmethod
    def reset(cls):
        Galaxy.galaxies = []
        Galaxy.total_dist = 0


def expand(scroll, expand_amount):
    empty_cols_i = [True for _ in range(len(scroll[0]))]
    expanded = scroll.copy()
    rows_added = 0
    empty_row = ['.' for _ in scroll[0]]
    for row in range(len(scroll)):
        if scroll[row] == empty_row:
            for i in range(expand_amount):
                expanded.insert(row + rows_added, ['.' for _ in range(len(scroll[0]))])
                rows_added += 1
        for col in range(len(scroll[row])):
            if scroll[row][col] == "#":
                empty_cols_i[col] = False

    for row in range(len(expanded)):
        cols_added = 0
        for i in range(len(empty_cols_i)):
            if empty_cols_i[i]:
                for j in range(expand_amount):
                    expanded[row].insert(i + cols_added, '.')
                    cols_added += 1
    return expanded


with open('day11_input.txt', 'r') as file:
    scroll = file.readlines()
scroll1 = [list(x.strip()) for x in scroll]
scroll2 = [list(x.strip()) for x in scroll]
# scroll1 = [list(x) for x in ["...#......",".......#..","#.........","..........","......#...",".#........",".........#","..........",".......#..","#...#....."]]
expansion_level = 2
ans1 = expand(scroll1, expansion_level-1)

for row in range(len(ans1)):
    for col in range(len(ans1[0])):
        if ans1[row][col] == "#":
            Galaxy(col, row)

print(f'ans1: {Galaxy.total_dist}')  # 10231178

Galaxy.reset()
expansion_level = 1_000_000
ans2 = expand(scroll2, expansion_level-1)
for row in range(len(ans2)):
    for col in range(len(ans2[0])):
        if ans2[row][col] == "#":
            Galaxy(col, row)

print(f'ans2: {Galaxy.total_dist}')
