from snail_opti import snail

class Node:
    def __init__(self,data,level=0,f_sco=0):
        self.data = data
        self.level = level
        self.f_sco = f_sco
    def set_next_node(self, next_node):
        self.next_node = next_node

    def get_next_node(self):
        return self.next_node

    def get_value(self):
        return self.value

class Puzzle:
    def __init__(self, size):
        self.n = size
        self.open_lst = []
        self.close_lst = []
    ### check if solveable
    def check_input(self):
        pass 
    ## how far the goal node is
    def h_score(self,start,goal):
        # diff between the start and goal
        # hena we can use diff distance algo [euclidean_distance,manhattan_distance,hamming_distance]
        tmp = 0
        for i in range(0,self.n):
             for j in range(0,self.n):
                 #if start[i][j] != goal[i][j] and start[i][j] != '_':
                     print("this is i = {} and j = {} == {} ".format(i,j,start[i][j]))
        return tmp


    ## The heuristic value 
    def f_score(self,start,goal):
        # f(x) = h(x) + g(x)
        # g(x) isnumber of nodes traversed from start node 
               #to get to the current node.
        return self.h_score(start,goal) + start.level
    def solver(self):
        start = [[1,2,3], [8,0,4], [7,6,5]]
        copy = [[1,2,3], [8,0,4], [7,6,5]]
        goal = snail(copy)
        print(start)
        print(goal)
        star = Node(start,0,0)
        print(star)
        star.f_sco = self.f_score(start,goal)
        #print(start.f_sco)
start = [[1,2,3], [8,0,4], [7,6,5]]
puz = Puzzle(3)
puz.solver()

