def question1(directions):
    count = 0
    cur_node = Node.root
    while True:
        if cur_node is Node.end:
            break
        count += 1
        current_direction = next(directions)
        if current_direction == 'L':
            cur_node_name = Node.left[str(cur_node)]
        elif current_direction == 'R':
            cur_node_name = Node.right[str(cur_node)]
        cur_node = Node.find_node(cur_node_name)
    return count


class Node:
    nodes, left, right = {}, {}, {}
    root, end = None, None

    def __init__(self, cur, left, right):
        if cur == "AAA":
            Node.root = self
        elif cur == "ZZZ":
            Node.end = self
        Node.nodes[cur], Node.left[cur], Node.right[cur] = self, left, right
        self.cur = cur

    def __str__(self):
        return self.cur

    @classmethod
    def find_node(cls, label):
        return cls.nodes.get(label)


def question2(directions):
    cur_nodes = [Node.nodes[str(node)] for node in Node.nodes if str(node).endswith("A")]
    count = 0
    while True:
        if all([str(node).endswith("Z") for node in cur_nodes]):
            break
        count += 1
        current_direction = next(directions)
        if current_direction == 'L':
            cur_nodes_names = [Node.left[str(node)] for node in cur_nodes]
        elif current_direction == 'R':
            cur_nodes_names = [Node.right[str(node)] for node in cur_nodes]
        cur_nodes = [Node.find_node(node) for node in cur_nodes_names]
        if count%10000 == 0:
            print(f'{cur_nodes_names}, {count=}')
    return count


def generator(alist):
    while True:
        for i in alist:
            yield i


with open('day8_input.txt', 'r') as file:
    scroll = file.readlines()
directions, count = generator(scroll[0].replace('\n', '')), 0
for line in scroll[1:]:
    cur, left, right = line[:3], line[7:10], line[12:15]
    n = Node(cur, left, right)

print(f'res1: {question1(directions)}')  # 17287
print(f'res2: {question2(directions)}')  # brute force takes too long. need to use math.lcm
