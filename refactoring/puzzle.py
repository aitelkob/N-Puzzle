from pprint import pprint
from time import perf_counter as pc
from generator import Puzzle_goal
import numpy as np
from node_class import *

GOAL_STATE = [[]]
GLOBAL_STATE_DICT = {}
N = 0

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
    initial_node = Nodes(initial_state, manhattan_heuristic(initial_state),
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

    m = Puzzle_goal(n)
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
