class Node:
    def __init__(self, old_location, cur_location, dist_from_start, scroll):
        self.old_location, self.cur_location = old_location, cur_location
        self.node_type = scroll[cur_location[1]][cur_location[0]]
        self.new_location = self.find_to_where()
        self.dist_from_start = dist_from_start + 1

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
    with open('day10_input.txt', 'r') as file:
        scroll = file.readlines()
    # scroll = [".....",".S-7.",".|.|.",".L-J.","....."]
    for y in range(len(scroll)):
        cur_row = scroll[y]
        if cur_row.find("S") > -1:
            x = scroll[y].find("S")
            start = (x, y)
            if x != 0:
                if cur_row[x - 1] in {"-", "F", "L"}:
                    new_location = (x - 1, y)
            if x != len(cur_row):
                if cur_row[x + 1] in {"-", "7", "J"}:
                    new_location = (x + 1, y)
            else:
                new_location = (x, y - 1)
            break
    dist_from_start, cur_location = 1, start
    while True:
        cur_node = Node(cur_location, new_location, dist_from_start, scroll)
        print(f'{dist_from_start}:\t{cur_node.cur_location},\t{cur_node.node_type}')
        cur_location, new_location = cur_node.cur_location, cur_node.new_location
        dist_from_start += 1
        if cur_node.new_location == start:
            break
    print(f'loop ended, length={cur_node.dist_from_start}, furthest={cur_node.dist_from_start / 2}')  # 7173
