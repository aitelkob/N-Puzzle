import numpy as np
from pprint import pprint 
from time import perf_counter as pc

GOAL_STATE = [[]]
GLOBAL_STATE_DICT = {}
N = 0
def customSort(node):
    return node.heuristic
def manhattan_distance(a,b):
    return abs(b[0]  - a[0]) + abs(b[1] - a[1])
def manhattan_heuristic(state):
    distance = 0
    for i in range(N):
        for j in range(N):
            num = state[i][j]
            if num != GOAL_STATE[i][j] and num != 0:
                goal = GLOBAL_STATE_DICT[num]
                distance += manhattan_distance((i, j), goal)
    return distance

class Node:
    def __init__(self,data,distance,pos_zero):
        self.data = data
        self.heuristic = distance
        self.pos_zero = pos_zero
    def get_empty(self,data):
        for i in range(N):
            for j in range(N):
                if data[i][j] == 0:
                    return i,j

    def get_next_node(self):
        blank = self.pos_zero
        x,y = map(int, blank)
        moves = ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1))
        nodes = []
        for move in moves:
            if 0 <= move[0] < N and 0 <= move[1] < N:
                tmp = np.copy(self.data)
                goal = GLOBAL_STATE_DICT[tmp[move]]
                tmp[move],tmp[blank] = tmp[blank],tmp[move]
                goal_dist = manhattan_distance(move,goal)
                zero_dist = manhattan_distance(goal,(x,y))
                nodes.append(Node(tmp, self.heuristic - goal_dist + zero_dist,move))
        return sorted(nodes, key=customSort)

def search(path, g, threshold):
    node = list(path.keys())[-1]
    f = g + node.heuristic

    if f > threshold:
        return f
    if np.array_equal(node.data, GOAL_STATE):
        return True
    minimum = float('inf')
    for n in node.get_next_node():
        if n not in path:
            path[n] = None
            tmp = search(path, g + 1, threshold)
            if tmp == True:
                return True
            if tmp < minimum:
                minimum = tmp
            path.popitem()

    return minimum

def solve(initial_state):
    zero = np.where(initial_state == 0)
    initial_node = Node(initial_state, manhattan_heuristic(initial_state),
 zero)
    threshold = initial_node.heuristic
    path = {initial_node: None}
    while 1:
        tmp = search(path, 0, threshold)
        if tmp == True:
            print("GOOD!")
            return path.keys()
        elif tmp == float('inf'):
            print("WRONG!")
            return False
        threshold = tmp

def define_goal_state(n):
    global GOAL_STATE
    global N
    global GLOBAL_STATE_DICT

    m = [[0] * n for i in range(n)]
    dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
    x, y, c = 0, -1, 1
    for i in range(n + n - 2):
        for j in range((n + n - i) // 2):
            x += dx[i % 4]
            y += dy[i % 4]
            m[x][y] = c
            c += 1
    print(m)
    GOAL_STATE = np.array(m)
    N = len(GOAL_STATE)
    GLOBAL_STATE_DICT = {m[r][c]: (r, c) for r in range(N) for c in range(
N)}


tests = {'3x3': np.array([[8, 7, 3], [4, 1, 2], [0, 5, 6]]),
         '4x4': np.array([[13, 2, 10, 3],
                                [1, 12, 8, 4],
                                [5, 0, 9, 6],
                                [15, 14, 11, 7]])}

for name, puzzle in tests.items():
    define_goal_state(len(puzzle))
    print('Puzzle:\n', puzzle)
    t0 = pc()
    path = solve(puzzle)
    t1 = pc()
    print(f'{name} depth:{len(path)} runtime:{round(t1 - t0, 3)} s')


