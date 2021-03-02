from newsant import NewSant
from newsant import SantMove
import random
class Node:
    def __init__(self,sant):
        self.sant = sant
    def is_end(self):
        if(self.sant.winner != None):
            return True
        else:
            return False
    def score(self):
        if (self.sant.winner != None):

            if(self.sant.winner == False):
                return -1000000
            else:
                return 1000000
        scor = 0
        for k in self.sant.possible_walks(0):
            scor = scor + self.sant.table[k]
        for k in self.sant.possible_walks(1):
            scor = scor + self.sant.table[k]
        for k in self.sant.possible_walks(2):
            scor = scor - self.sant.table[k]
        for k in self.sant.possible_walks(3):
            scor = scor - self.sant.table[k]
        return scor
    def getChildrens(self):
        games=[]
        for move in self.sant.possible_moves():
            k = self.sant.copyMe()
            k.execute_move(move)
            games.append(Node(k))
        return games
    
def minimax(node, depth, maximizingPlayer):
    if depth == 0 or node.is_end():
        return (node,node.score())
    if maximizingPlayer == True:
        bv = -100000000
        bn = node
        for child in node.getChildrens():
            n,value = minimax(child,depth-1,False)
            if (value > bv):
                bv = value
                bn = child
        return (bn,bv)
    else: 
        bv = 100000000
        bn = node
        for child in node.getChildrens():
            n,value = minimax(child,depth-1,True)
            if(bv > value):
                bv = value
                bn = child
        
        return (bn,bv)

def alphabeta(node, depth,alpha,beta,maximizingPlayer):
    if depth == 0 or node.is_end():
        return (node,node.score())
    if maximizingPlayer == True:
        bv = -100000000
        bn = node
        a= alpha
        for child in node.getChildrens():
            n,value = alphabeta(child,depth-1,a,beta,False)
            if (value > bv):
                bv = value
                bn = child
            a=max(a,bv)
            if(a >= beta):
                break
        return (bn,bv)
    else: 
        bv = 100000000
        bn = node
        b = beta
        for child in node.getChildrens():
            n,value = alphabeta(child,depth-1,alpha,b,True)
            if(bv > value):
                bv = value
                bn = child
            b = min(b,bv)
            if(b<=alpha):
                break
        return (bn,bv)
    
    
def is_valid_move(sant,move):
    for poss in sant.possible_moves():
        if (poss.who == move.who and poss.move== move.move and poss.build ==poss.build):
            return True
    return False
        

def vsHuman():
    s = NewSant()
    s.set_random_workers()
    n = Node(s)
    while(n.sant.winner == None):
        moves = len(n.sant.moves)
        if moves > 15:
            depth = 3
        else:
            depth = 4
        
        if(n.sant.white_on_move):
           # sc = minimax(n,3,True)
            sc= alphabeta(n,depth,-100000000,10000000,True)
        else:
            print(n.sant)
            valid = False
            while(valid == False):
                print('Please enter move !!')
                who = int(input('Who? '));
                move = int(input('Move? '));
                build = int(input ('Build? ')); 
                humanMove =SantMove(who,move,build)
                valid = is_valid_move(n.sant, humanMove)
                if(not valid):
                    print('Invalid move')
            n.sant.execute_move(humanMove)
            sc = (n,0)
            
            
        #    sc = minimax(n,3,False)
        n = sc[0]    
        print(sc[0].sant)
        print(sc[1])
        print('Moves {}'.format(len(sc[0].sant.moves)))
        print( sc[0].sant.moves[-1])
    
        
def kk():
    s=NewSant()
    s.set_random_workers()
    n = Node(s)
    while(n.sant.winner == None):
        moves = len(n.sant.moves)
        if moves > 15:
            depth = 3
        else:
            depth = 3
        
        if(n.sant.white_on_move):
           # sc = minimax(n,3,True)
            sc= alphabeta(n,depth,-100000000,10000000,True)
        else:
            sc=alphabeta(n,depth,-100000000,100000000,False)
        #    sc = minimax(n,3,False)
        n = sc[0]    
        print(sc[0].sant)
        print(sc[1])
        print('Moves {}'.format(len(sc[0].sant.moves)))
        print( sc[0].sant.moves[-1])


#kk()
vsHuman()
