#22p21c0253-ณัฐนันท์ 

import numpy as np
import heapq

class Board:
	parent = None
	state = None
	operator = None
	depth = 0
	zero = None
	cost = 0

	def __init__(self, state, parent = None, operator = None, depth = 0):
		self.parent = parent
		self.state = np.array(state)
		self.operator =  operator
		self.depth = depth
		self.zero = self.find_0()
		self.cost = self.depth + self.manhattan()
	
	def __lt__(self, other):
		if self.cost != other.cost:
			return self.cost < other.cost
		else:
			op_pr = {'Up': 0, 'Down': 1, 'Left': 2, 'Right': 3}
			return op_pr[self.operator] < op_pr[other.operator]

	def __str__(self):
		return str(self.state[:3]) + '\n' \
				+ str(self.state[3:6]) + '\n' \
				+ str(self.state[6:])+'\n' 

	def goal_test(self):
		if np.array_equal(self.state, np.arange(9)):
			return True
		else:
			return False

	def find_0(self):
		for i in range(9):
			if self.state[i] == 0:
				return i

	def manhattan(self):
		state = self.index(self.state)
		goal = self.index(np.arange(9))
		return sum((abs(state // 3 - goal // 3) + abs(state % 3 - goal % 3))[1:])

	def index(self, state):
	    index = np.array(range(9))
	    for x, y in enumerate(state):
	        index[y] = x
	    return index

	def swap(self, i, j):
		new_state = np.array(self.state)
		new_state[i], new_state[j] = new_state[j], new_state[i]
		return new_state

	def up(self):
		if self.zero > 2:
			return Board(self.swap(self.zero, self.zero - 3), self, 'Up', self.depth + 1)
		else:
			return None	

	def down(self):
		if self.zero < 6:
			return Board(self.swap(self.zero, self.zero + 3), self, 'Down', self.depth + 1)
		else:
			return None

	def left(self):
		if self.zero % 3 != 0:
			return Board(self.swap(self.zero, self.zero - 1), self, 'Left', self.depth + 1)
		else:
			return None

	def right(self):
		if (self.zero + 1) % 3 != 0:
			return Board(self.swap(self.zero, self.zero + 1), self, 'Right', self.depth + 1)
		else:
			return None

	def neighbors(self):
		neighbors = []
		neighbors.append(self.up())
		neighbors.append(self.down())
		neighbors.append(self.left())
		neighbors.append(self.right())
		return list(filter(None, neighbors))

	__repr__ = __str__


class Solver:
	soln = None
	path = None
	nodes_expanded = 0
	max_depth = 0

	def ancestral_chain(self):
		current = self.soln
		chain = [current]
		while current.parent != None:
			chain.append(current.parent)
			current = current.parent
		return chain
	
	def path(self):
		path = [node.operator for node in self.ancestral_chain()[-2::-1]]
		return path

	def ast(self, state):
		frontier = []
		heapq.heappush(frontier, state)
		froxplored = set()
		while frontier:
			board = heapq.heappop(frontier)
			froxplored.add(tuple(board.state))
			print(board)
			if board.goal_test():
				self.soln = board
				self.path = self.path()
				self.nodes_expanded = len(froxplored)-len(frontier)-1
				return self.soln
			for neighbor in board.neighbors():
				if tuple(neighbor.state) not in froxplored:
					heapq.heappush(frontier, neighbor)
					froxplored.add(tuple(neighbor.state))
					self.max_depth = max(self.max_depth, neighbor.depth)
		return None

value = [1,2,5,3,4,0,6,7,8]

p = Board(np.array(value))
print("="*15)
print("Input board")          
print("="*15)
print(p)

print("="*15)
s = Solver()
soln = s.ast(p)
print("="*15)
print("Result board")          
print("="*15)
print(soln)