from snail_opti import snail
from pprint import pprint

class Node:
    def __init__(self,data,level=0,f_sco=0):
        self.data = data
        self.level = level
        self.f_sco = f_sco
    def get_copy(self, mapp):
        tmp = [row[:] for row in mapp]
        return tmp
    def get_child(self):
        
    # i need function to move the empty space in logic path
    def move_blank(self,mapp,xi,yi,xj,yj):
        if xj >= 0 and xj< len(self.data) and yj >= 0 and yj <= len(self.data):
            temp1 = []
            temp1 = self.get_copy(mapp)
            temp2 = temp1[xj][yj]
            print(temp2)
            temp1[xj][yj] = temp1[xi][yi]
            temp1[xi][yi] = temp2
            return temp1
        else:
            return None
    def get_empty(self,mapp,x):
        for i in range(0,len(self.data)):
            for j in range(0,len(self.data)):
                if mapp[i][j] == x:
                    return i,j

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
                 if start[i][j] != goal[i][j] and start[i][j] != 0:
                     tmp+=1
        return tmp


    ## The heuristic value 
    def f_score(self,start,goal):
        # f(x) = h(x) + g(x)
        # g(x) isnumber of nodes traversed from start node 
               #to get to the current node.
        return self.h_score(start.data,goal) + start.level
    def solver(self):
        start = [[1,2,3], [8,0,4], [7,6,5]]
        copy = [[1,2,3], [8,0,4], [7,6,5]]
        goal = snail(copy)
        star = Node(start,0,0)
        pprint(vars(star))
        star.f_sco = self.f_score(star,goal)
        self.open_lst.append(star)
        testing = [[1,2,3], [8,0,4], [7,6,5]]
        #tmp = star.get_copy(star.data)
        x,y = star.get_empty(star.data,0)
        moves = [[x,y-1],[x,y+1],[x-1,y],[x+1,y]]
        while True:
            tmp = self.open_lst[0]
            pprint(vars(tmp))
            exit()
            # check all possible direction
            for move in moves:
                weliyed = star.move_blank(star.data,x,y,move[0],move[1])
                if weliyed is not None:
                    weld_node = Node(weliyed,level+1)
                    pprint(weld_node)

start = [[1,2,3], [8,0,4], [7,6,5]]
puz = Puzzle(3)
puz.solver()

