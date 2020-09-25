#22p21c0253-ณัฐนันท์ 

from queue import PriorityQueue as pq
from copy import deepcopy

class Node(object):
    def __init__(self, board, move,parent=None):
        self.board = board
        self.move = move
        self.parent = parent

    def __lt__(self,other): 
        return 0

    def find_zero(self):
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == 0:
                    return i,j

    def manhattan_distance(self):
        cost = 0
        for i in range(3):
            for j in range(3):
                row = int(self.board[i][j]/3)
                column = int(self.board[i][j]%3)
                cost += abs(i-row)+abs(j-column)
        return cost

    def generate_nodes(self):
        find_zero = self.find_zero()
        board = self.board
        allnodes = []
        if not find_zero[0]-1<0:
            board_up = deepcopy(board)
            board_up[find_zero[0]][find_zero[1]] = board_up[find_zero[0]-1][find_zero[1]]
            board_up[find_zero[0]-1][find_zero[1]] = 0
            board_up_node = Node(board_up,'down',self) 
            allnodes.append(board_up_node)
        if find_zero[0]+1<3:
            board_down = deepcopy(board)
            board_down[find_zero[0]][find_zero[1]] = board_down[find_zero[0]+1][find_zero[1]]
            board_down[find_zero[0]+1][find_zero[1]] = 0
            board_down_node = Node(board_down, 'up',self)
            allnodes.append(board_down_node)
        if not find_zero[1]-1<0:
            board_left = deepcopy(board)
            board_left[find_zero[0]][find_zero[1]] = board_left[find_zero[0]][find_zero[1]-1]
            board_left[find_zero[0]][find_zero[1]-1] = 0
            board_left_node = Node(board_left,'right',self)
            allnodes.append(board_left_node)
        if find_zero[1]+1<3:
            board_right = deepcopy(board)
            board_right[find_zero[0]][find_zero[1]] = board_right[find_zero[0]][find_zero[1]+1]
            board_right[find_zero[0]][find_zero[1]+1] = 0
            board_right_node = Node(board_right,'left',self)
            allnodes.append(board_right_node)
        
        return allnodes

    def track(self):
        path = []
        path.append((self.move,self.board))
        n = self.parent
        while n.parent is not None:
            path.append((n.move,n.board))
            n = n.parent
        path.append((n.move,n.board))
        path.reverse()
        return path

class Astar():
    def solve(self,initial_node):
        PQ = pq()
        visited = []
        explored = 0
        PQ.put((initial_node.manhattan_distance(),initial_node))
        while not PQ.empty():  
            h, n = PQ.get()
            if n.board in visited:
                continue
            if h==0:
                self.draw(n.track())
                return
        
            visited.append(n.board)
            explored+=1
            for nnode in n.generate_nodes(): 
                PQ.put((nnode.manhattan_distance(),nnode))

    def draw_board(self,board):
        print(' ___________')
        for plate in board:
            print('| {} | {} | {} | '.format(plate[0],plate[1],plate[2]))
        print(' ___________')

    def draw(self,path):
        for board in path:
            self.draw_board(board[1])


initial_node = Node([[1,2,5],[3,4,0],[6,7,8]],'start')
s = Astar()
s.solve(initial_node)
