import numpy as np
from pprint import pprint 
from time import perf_counter as pc
from generator import Puzzle_goal
from puzzle import * 

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

class Nodes:
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

