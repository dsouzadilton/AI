# DILTON D'SOUZA
# 8865
# TE COMPUTERS - A
# PRACTICAL BATCH - A

# TIC TAC TOE GAME - USING BFS

import unittest 
class Game: 
def __init__(self): 
self.field=[[0 for x in range(3)] for y in range(3)] 
def print(self): 
for line in self.field: 
print(str(line[0])+" "+str(line[1])+" "+str(line[2])) 
print("") 
def check(self): 
for i in range(3): 
for j in range(3): 
if(abs(self.field[i][j]>1)): 
raise ValueError("trying to cheat, are you") 
def status(self): 
self.check() 
for i in range(3): 
row_sum=0 
col_sum=0
for j in range(3): 
row_sum+=self.field[i][j] 
col_sum+=self.field[j][i] 
if(row_sum==-3): 
return -1 
elif(col_sum==-3): 
return -1 
elif(row_sum==3): 
return 1 
elif(col_sum==3): 
return 1 
diag=self.field[0][0]+self.field[1][1]+self.field[2][2] 
if(diag==-3): 
return -1 
elif(diag==3): 
return 1 
diag=self.field[0][2]+self.field[1][1]+self.field[2][0] 
if(diag==-3): 
return -1 
elif(diag==3):
return 1 
return 0 
def player_draw(self): 
while True: 
choice=input("your turn: ") choice=choice.strip().split(" ") x=int(choice[0])-1 
y=int(choice[1])-1 
if x<0 or x>2: 
continue 
if y<0 or y>2: 
continue 
if self.field[x][y]!=0: 
continue 
self.field[x][y]=1 
break 
def ai_draw(self): 
self.check 
print("former state") 
self.print() 
if self.moves_available():
lowest_score=2 
choice =(0,0) 
for i in range(3): 
for j in range(3): 
if self.field[i][j]==0: 
self.field[i][j]=-1 
current_score=self.max_ai(self.field.copy()) if current_score<lowest_score: 
lowest_score=current_score 
choice=(i,j) 
self.field[i][j]=0 
self.field[choice[0]][choice[1]]=-1 
else: 
print("board is full, ai can't draw") 
print("ai has chosen") 
self.print() 
def min_ai(self,state:[]): 
lowest_score=2 
if not self.moves_available(): 
return self.status() 
if abs(self.status())>0:
return self.status() 
for i in range(3): 
for j in range(3): 
if(state[i][j]==0): 
state[i][j]=-1 
current_score=self.max_ai(state) if current_score<lowest_score: 
lowest_score=current_score 
state[i][j]=0 
return lowest_score 
def max_ai(self,state): 
highest_score=-2 
if not self.moves_available(): 
return self.status() 
if abs(self.status())>0: 
return self.status() 
for i in range(3): 
for j in range(3): 
if(state[i][j]==0):
state[i][j]=1 
current_score=self.min_ai(state) 
if current_score>highest_score: 
highest_score=current_score 
state[i][j]=0 
return highest_score 
def moves_available(self): 
for i in range(3): 
for j in range(3): 
if self.field[i][j]==0: 
return True 
return False 
class TestGame(unittest.TestCase): def testStatus(self): 
game=Game() 
game.field[0][0]=-1 
game.field[0][1]=-1 
game.field[0][2]=-1 
self.assertEqual(game.status(),-1) 
game=Game() 
game.field[1][0]=1
game.field[1][1]=1 
game.field[1][2]=1 
self.assertEqual(game.status(),1) 
game=Game() 
game.field[2][0]=-1 
game.field[2][1]=-1 
game.field[2][2]=-1 
self.assertEqual(game.status(),-1) 
game=Game() 
game.field[0][0]=1 
game.field[1][0]=1 
game.field[2][0]=1 
self.assertEqual(game.status(),1) 
game=Game() 
game.field[0][1]=-1 
game.field[1][1]=-1 
game.field[2][1]=-1 
self.assertEqual(game.status(),-1) 
game=Game() 
game.field[0][2]=1 
game.field[1][2]=1
game.field[2][2]=1 
self.assertEqual(game.status(),1) 
game=Game() 
game.field[0][0]=-1 
game.field[1][1]=-1 
game.field[2][2]=-1 
self.assertEqual(game.status(),-1) 
game=Game() 
game.field[0][2]=1 
game.field[1][1]=1 
game.field[2][0]=1 
self.assertEqual(game.status(),1) 
if __name__=="__main__": 
suite=unittest.TestLoader().loadTestsFromTestCase(TestGame) unittest.TextTestRunner().run(suite) 
game=Game() 
while(game.moves_available()): 
if(game.status()!=0): 
break 
game.player_draw()
if(game.status()!=0): 
break 
game.ai_draw() 
if(game.status()==1): 
print("player won") 
elif(game.status()==-1): 
print("ai won") 
else: 
print("draw") 
''' 
