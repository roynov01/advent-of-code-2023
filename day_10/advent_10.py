class Node:
    # nodes = []
    def __init__(self, old_location, cur_location, dist_from_start, scroll, start):
        print(dist_from_start)
        self.old_location, self.cur_location = old_location, cur_location
        self.node_type = scroll[cur_location[1]][cur_location[0]]
        self.dist_from_start = dist_from_start
        new_location = self.find_to_where()
        new_dist_from_start = dist_from_start + 1
        if new_dist_from_start == 1443:
            print()
        if new_location == start and dist_from_start != 1:
            print(f'loop ended, length={new_dist_from_start}, furthest={new_dist_from_start/2}')
        else:
            print(f'{old_location=}\n{cur_location=}\n{self.node_type=}\n')
            Node(self.cur_location, new_location, new_dist_from_start, scroll, start)

    def find_to_where(self):
        if self.node_type == "|":
            if self.old_location[1] > self.cur_location[1]:
                return self.old_location[0], self.cur_location[1] - 1
            else:
                return self.old_location[0], self.cur_location[1] + 1
        elif self.node_type == "-":
            if self.old_location[0] > self.cur_location[0]:
                return self.cur_location[0] - 1, self.cur_location[1]
            else:
                return self.cur_location[0] + 1, self.cur_location[1]
        elif self.node_type == "7":
            if self.old_location[0] < self.cur_location[0]:
                return self.cur_location[0], self.cur_location[1] + 1
            else:
                return self.cur_location[0] - 1, self.cur_location[1]
        elif self.node_type == "J":
            if self.old_location[0] < self.cur_location[0]:
                return self.cur_location[0], self.cur_location[1] - 1
            else:
                return self.cur_location[0] - 1, self.cur_location[1]
        elif self.node_type == "L":
            if self.old_location[0] > self.cur_location[0]:
                return self.cur_location[0], self.cur_location[1] - 1
            else:
                return self.cur_location[0] + 1, self.cur_location[1]
        elif self.node_type == "F":
            if self.old_location[0] > self.cur_location[0]:
                return self.cur_location[0], self.cur_location[1] + 1
            else:
                return self.cur_location[0] + 1, self.cur_location[1]


if __name__ == "__main__":
    import sys
    sys.setrecursionlimit(25000)
    with open('day10_input.txt', 'r') as file:
        scroll = file.readlines()
    # scroll = [".....",".S-7.",".|.|.",".L-J.","....."]
    # scroll = ["..F7.",".FJ|.","SJ.L7","|F--J","LJ..."]
    for y in range(len(scroll)):
        cur_row = scroll[y]
        if cur_row.find("S") > -1:
            x = scroll[y].find("S")
            start = (x, y)
            if x != 0:
                if cur_row[x - 1] in {"-", "F", "L"}:
                    Node(start, (x - 1, y), 1, scroll, start)
            if x != len(cur_row):
                if cur_row[x + 1] in {"-", "7", "J"}:
                    Node(start, (x + 1, y), 1, scroll, start)
            else:
                Node(start, (x, y - 1), 1, scroll, start)
    print("answer 1 is 7173 (total length 14345")
