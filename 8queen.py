from queue import PriorityQueue as pq
from copy import deepcopy


class Node(object):
    
    def _init_(self, board, move,parent=None):
        self.board = board
        self.move = move
        self.parent = parent
    
    def _lt_(self,other): 
        return 0
    
    def zero_position(self):
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == 0:
                    return i,j

    def manhattan_distance(self):
        total = 0
        for i in range(3):
            for j in range(3):
                row = int(self.board[i][j]/3)
                column = int(self.board[i][j]%3)
                total += abs(i-row)+abs(j-column)
        return total
    
    def generate_nodes(self):
        zero_position = self.zero_position() 
        board = self.board 
        allnodes = [] 
        if not zero_position[0]-1<0: 
            board_up = deepcopy(board) 
            board_up[zero_position[0]][zero_position[1]] = board_up[zero_position[0]-1][zero_position[1]] 
            board_up[zero_position[0]-1][zero_position[1]] = 0 
            board_up_node = Node(board_up,'down',self) 
            allnodes.append(board_up_node) 
        if zero_position[0]+1<3:  
            board_down = deepcopy(board)
            board_down[zero_position[0]][zero_position[1]] = board_down[zero_position[0]+1][zero_position[1]] 
            board_down[zero_position[0]+1][zero_position[1]] = 0 
            board_down_node = Node(board_down, 'up',self)
            allnodes.append(board_down_node)
        if not zero_position[1]-1<0: 
            board_left = deepcopy(board)
            board_left[zero_position[0]][zero_position[1]] = board_left[zero_position[0]][zero_position[1]-1] #puts a value of the node above to the place, where zero was.
            board_left[zero_position[0]][zero_position[1]-1] = 0 
            board_left_node = Node(board_left,'right',self)
            allnodes.append(board_left_node)
        if zero_position[1]+1<3: 
            board_right = deepcopy(board)
            board_right[zero_position[0]][zero_position[1]] = board_right[zero_position[0]][zero_position[1]+1] #puts a value of the node above to the place, where zero was.
            board_right[zero_position[0]][zero_position[1]+1] = 0 
            board_right_node = Node(board_right,'left',self)
            allnodes.append(board_right_node)
        
        return allnodes
    
    def traceback(self):
        path = []
        path.append((self.move,self.board))
        n = self.parent
        while n.parent is not None:
            path.append((n.move,n.board))
            n = n.parent
        path.append((n.move,n.board))
        path.reverse()
        return path

     
initial_node = Node([[5,7,8],[2,3,1],[4,0,6]],'start')
def Astar(initial_node):
    PQueue = pq() 
    visited = []
    explored = 0
    PQueue.put((initial_node.manhattan_distance(),initial_node)) 
    while not PQueue.empty():  
       h, n = PQueue.get() 
       if n.board in visited:   
           continue
       if h==0: 
           print('Congratulations!')
           print('The numbered of explored nodes:%d'%explored)
           draw_path(n.traceback())
           return
       
       visited.append(n.board)
       
       explored+=1
       
       for nnode in n.generate_nodes(): 
           PQueue.put((nnode.manhattan_distance(),nnode))
        
def draw_board(board):
    print('_____')
    for i in board:
        print('|%d|%d|%d|'%(i[0],i[1],i[2]))
        print('_____') 
  
def draw_path(path):
    for b in path:
        print(b[0])
        draw_board(b[1])
    print('END') 


Astar(initial_node)
