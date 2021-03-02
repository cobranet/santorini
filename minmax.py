from newsant import NewSant
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
        wm = len(self.sant.possible_walks(0))+len(self.sant.possible_walks(1))
        bm = len(self.sant.possible_walks(2))+len(self.sant.possible_walks(3))
        hw = self.sant.table[self.sant.workers[0]]+self.sant.table[self.sant.workers[1]]
        hb = self.sant.table[self.sant.workers[2]]+self.sant.table[self.sant.workers[3]]
        return wm + 4*hw - bm - 4*hb+random.randint(-5,5)
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
    
    
def test_min():
    s=NewSant()
    s.set_random_workers()
    n = Node(s)
    print(s.white_on_move)
    sc = minimax(n,3,True)
    
    print(sc[0].sant)
    print(sc[1])
    for move in sc[0].sant.moves:
        print(move)

    sc = minimax(sc[0],3,False)
    print(sc[0].sant)
    print(sc[1])
    for move in sc[0].sant.moves:
        print(move)

    sc = minimax(sc[0],3,True)
    print(sc[0].sant)
    print(sc[1])
    for move in sc[0].sant.moves:
        print(move)

def kk():
    s=NewSant()
    s.set_random_workers()
    n = Node(s)
    while(n.sant.winner == None):
        print(n.sant.winner)
        if(n.sant.white_on_move):
           # sc = minimax(n,3,True)
            sc= alphabeta(n,3,-100000000,10000000,True)
        else:
            sc=alphabeta(n,3,-100000000,100000000,False)
        #    sc = minimax(n,3,False)
        n = sc[0]    
        print(sc[0].sant)
        print(sc[1])
        print ('Moves {}'.format(len(sc[0].sant.moves)))
        for move in sc[0].sant.moves:
            print(move)



kk()
