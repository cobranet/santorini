import random

class SantMove:
    def __init__(self,who,move,build):
        self.who=who
        self.move=move
        self.build=build
    def __str__(self):
        return 'Worker {} move to {} and build {}'.format(self.who,self.move,self.build)

class NewSant:
    cell_neighbors=[[1,5,6], #0
                   [0,2,5,6,7], #1
                   [1,3,6,7,8],  #2 
                   [2,4,7,8,9], #3
                   [3,8,9],  #4

                   [0,1,6,10,11], #5
                   [0,1,2,5,7,10,11,12], #6
                   [1,2,3,6,8,11,12,13], #7
                   [2,3,4,7,9,12,13,14], #8
                   [3,4,8,13,14], #9

                   [5,6,11,15,16], #10
                   [5,6,7,10,12,15,16,17], #11
                   [6,7,8,11,13,16,17,18], #12
                   [7,8,9,12,14,17,18,19], #13
                   [8,9,13,18,19], #14

                   [10,11,16,20,21], #15
                   [10,11,12,15,17,20,21,22], #16
                   [11,12,13,16,18,21,22,23], #17
                   [12,13,14,17,19,22,23,24], #18
                   [13,14,18,23,24], #19

                   [15,16,21], #20
                   [15,16,17,20,22], #21
                   [16,17,18,21,23], #22
                   [17,18,19,22,24], #23
                   [18,19,23]] #24
    def is_empty(self,point):
        return not point in self.workers

    def execute_move(self,move):
        self.moves.append(move)
        self.workers[move.who]=move.move
        if(move.build == None ) :
            self.winner = self.white_on_move
            return
        
        self.table[move.build]= self.table[move.build]+1
        self.white_on_move = not self.white_on_move
        if (len(self.possible_moves())==0):
            self.winner = not self.white_on_move

    def copyMe(self):
        s = NewSant();
        s.table =[]
        s.workers=[]
        for k in self.table:
            s.table.append(k)
        for k in self.workers:
            s.workers.append(k)
        s.white_on_move = self.white_on_move
        s.winner = self.winner
        for k in self.moves:
            s.moves.append(k)
        return s
    
    def possible_walks(self,worker):
        points =[]
        worker_level = self.table[self.workers[worker]]
        for k in NewSant.cell_neighbors[self.workers[worker]]:
            if self.is_empty(k) and self.table[k] <= worker_level+1:
                points.append(k)
        return points

    def possible_builds(self,point,worker):
        points=[]
        for k in NewSant.cell_neighbors[point]:
            if (self.is_empty(k) or k==self.workers[worker])  and self.table[k] < 4:
                points.append(k)
        return points

    def possible_moves(self):
        moves = []
        k = 0
        if(not self.white_on_move):
            k = 2
        for work in range(2):
            for walk in self.possible_walks(work+k):
                if self.table[walk] == 3:
                    moves = []
                    moves.append(SantMove(work+k,walk,None))
                    return moves             
                for build in self.possible_builds(walk,work+k):
                    moves.append(SantMove(work+k,walk,build))
        return moves
            
    
    def __init__(self):
        self.moves = []
        self.winner = None
        self.workers =[None,None,None,None]
        self.table = [0,0,0,0,0,
                      0,0,0,0,0,
                      0,0,0,0,0,
                      0,0,0,0,0,
                      0,0,0,0,0
        ]
        self.white_on_move = False
    
        
        
    def set_random_workers(self):
        nums = []
        while len(nums) < 4:
            k = random.randint(0,24)
            if not k in nums: 
                nums.append(k)
        self.workers = nums
    def __str__(self):
        if self.white_on_move:
            who='WHITE TO PLAY'
        else:
            who='BLACK TO PLAY'
            
        output = '{} WF:{} WM:{} BF:{} BM:{}\n______________\n'.format(who,self.workers[0],self.workers[1],self.workers[2],self.workers[3])
        for i in range(5):
            line = ''
            for k in range(5):
                line = line + str(self.table[i*5+k])
            output = output + line +'\n'
        if (self.winner != None):
            if(self.winner == False):
                output = output + "Winner is Black"
            else:
                output = output + "Winner is White"
        return output


def play_random_game():    
    s = NewSant()

    s.set_random_workers()

    while(s.winner == None):
        move = random.choice(s.possible_moves())
        print(move)
        s.execute_move(move)
    print(s)

