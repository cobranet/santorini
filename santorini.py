from util import Util as utl
import random
""" Santorini model ... State is array of this values :
  [ White or Black on Move 0 or 1, White female position from 1 to 25 or 0, White male position ... , Black female ...,
    Black male,
    .... 25 numbers from 0 to 3 ... height on position ... and after that is possible actions 0 - PUT , 1 -MOVE, 2-BUILD , 3- END 4 - SELECT  ]
   last field is choosen player 0 - none , 1 - white female , 2 - white male , 3 - black female 4- black male
   there is 32 values and that is full state of game

"""
class Santorini:
   """ Table is numbers from 1 to 25 and have string representation
       1 is "A1",2 is "A2" .... and so on ... 
   """


   def check_end(maximizingPlayer):
       return false

   def start():
      return utl.start

   def is_end():
      return false;
   
   def active_piece(santorini):
      onmove,action,table,positions,selected = utl.decompose_santorini(santorini)
      return selected
     
      
   def possible_builds(santorini):
      onmove,action,table,positions,selected = utl.decompose_santorini(santorini)
      pieces = [utl.piece_labels[selected-1]]
      moves = []
      action = santorini[30]
      for p in pieces:
         pos = utl.piece_pos(p,santorini)
         adj = utl.cell_neighbors[pos-1]
         for cell in adj:
            ltab = table[cell-1]
            if ( ltab < 4 and cell not in positions):
               moves.append((p,"BUILD",cell))
      return moves

   def possible_moves(santorini):
      onmove,action,table,positions,selected = utl.decompose_santorini(santorini)
      my=positions[onmove*2:onmove*2+2]
      pieces = [utl.piece_labels[selected-1]]
      moves = []
      action = santorini[30]
      for p in pieces:
         pos = utl.piece_pos(p,santorini)
         lvl = table[pos-1]
         adj = utl.cell_neighbors[pos-1]
         for cell in adj:
            ltab = table[cell-1]
            if ( ltab < 4 and ltab - lvl < 2 and cell not in positions):
               moves.append((p,"MOVE",cell))
      return moves

   """ Check end by no move 
       this is execute before MOVE and winner is player not on move 
   """
   def check_end_by_nomove(santorini):
      onmove,action,table,positions,selected = utl.decompose_santorini(santorini)
      moves = Santorini.all_possible(santorini)
      if (onmove==0):
         winner = 1
      else:
         winner = 0
      if (len(moves) == 0):
         return (True,winner)
      return (False,None)

   """Check end by climb
    this is execute after MOVE action and winner is player on move
   """
   def check_end_by_climb(santorini):
     onmove,action,table,positions,selected = utl.decompose_santorini(santorini)
     my=positions[onmove*2:onmove*2+2]
     for piece in my:
        if (table[piece-1]==3):
           return (True,onmove)
     return (False,None)

   """Execute bulid
      is list of possible so check is not needed
   """ 
   def execute_build(santorini,move):
      who,action,where = move
      onmove = santorini[0]
      nexts = santorini[:]
      nexts[where+4] = nexts[where+4]+1
      # now is time to other player to move
      nexts[30]=1
      nexts[31]=0
      if ( nexts[0] == 1 ):
         nexts[0] = 0
      else:
         nexts[0] = 1
      return nexts
  
  
   """Execute move
      is list of possible so check is not needed
   """ 
   def execute_move(santorini,move):
      who,action,where = move
      onmove = santorini[0]
      nexts = santorini[:]
      nexts[utl.piece_index(who)] = where
      # now we must build
      nexts[30]=2
      return nexts
   
   """Excute put 
   is from list of possible so check is not needed"""
   def execute_put(santorini,move):
      
      who,action,where = move
      onmove = santorini[0]
      nexts = santorini[:]
      nexts[31]=0
      nexts[utl.piece_index(who)] = where
      if ( onmove == 1):
         nexts[0] = 0
      else:
         nexts[0]= 1
      # if all four piecs are on table we should change action santorini[30]
      where = nexts[1:5]
      for k in where:
         if k == 0:
            return nexts
      nexts[30]=1
      return nexts
   

   
   
   "This should return  M and F of proper color"
   def possible_selects(santorini):
      selects = []
      onmove = santorini[0]
      if ( onmove == 0):
         if(santorini[30]!=0 or santorini[1]==0):
            selects.append(("WF","SELECT",""))
         if(santorini[30]!=0 or santorini[2]==0):            
            selects.append(("WM","SELECT",""))
      else:
         if(santorini[30]!=0 or santorini[3]==0):
            selects.append(("BF","SELECT",""))
         if(santorini[30]!=0 or santorini[4]==0):
            selects.append(("BM","SELECT",""))
      return selects   
   
   "This should return possible moves if there is any"
   def all_possible(santorini):
      if(santorini[31] == 0):
         moves = Santorini.possible_selects(santorini)
         return moves
      if(santorini[30] == 0):
         moves = Santorini.possible_puts(santorini)
      if(santorini[30] == 1):
         moves = Santorini.possible_moves(santorini)
      if(santorini[30]==2):
         moves=Santorini.possible_builds(santorini)
      return moves
   
      
   
   "This should return moves of put if there is any"
   def possible_puts(santorini):
       puts = []
       action = santorini[30]
       if (action != 0 ):
          return puts
       onmove = santorini[0]
       selected = santorini[31]
       where = santorini[1:5]
       piece=utl.piece_labels[selected-1]
       for cell in range(1,1+25):
          if cell not in where:
             puts.append((piece,"PUT",cell))
       return puts
       
   
   def cell_index(cellstr):
      return utl.cell_labels.index(cellstr)+1


   def execute_select(santorini,move):
      who,action,where = move
      piece = utl.piece_index(who)
      nexts = santorini[:]
      nexts[31]= piece
      return nexts
   
   def execute_all(santorini,move):
      lend = False
      winner = None
      message = ""
      if(santorini[31]==0):
         s = Santorini.execute_select(santorini,move)
         lend,winner = Santorini.check_end_by_nomove(s)
         if(lend):
            message = "Winer by no move select"
            s[30]=3
            s[0]=winner
         return s
      if(santorini[30] == 0):
         s = Santorini.execute_put(santorini,move)
         return s
      if(santorini[30]==1):
         s=Santorini.execute_move(santorini,move)
         lend,winner = Santorini.check_end_by_climb(s)
         if(lend):
            message = "Winer by climb"
            s[30]=3
            s[0]=winner
         # if(not lend) :
         #    lend,winner = Santorini.check_end_by_nomove(s)
         #    if(lend):
         #       message = "Winnner by no move 1"
         #       print(message)
         #       s[30]=3
         #       s[0]= winner
               
      if(santorini[30]==2 ):
         s = Santorini.execute_build(santorini,move)
         lend,winner = Santorini.check_end_by_nomove(s)
         if(lend):
            message = "Winer by no move 2"
            s[30]=3
            s[0]=winner
      return s
   def play_random_game(santorini):
      s = santorini[:]
      while(s[30]!=3):
         moves = Santorini.all_possible(s)
         if (len(moves) == 0 ):
            s[30]=3
            if (s[0]==0):
               s[0]=1
            else:
               s[0]=0
         else:
            move = random.choice(moves)
            s=Santorini.execute_all(s,move)
      return s


   

   def best(santorini,numtimes):
      s=santorini[:]
      onmove = s[0]
      moves = Santorini.all_possible(s)
      scores=[]
      if (s[30] == 0):
         n = 10
      else:
         n = numtimes
      for idx,move in enumerate(moves):
         scores.append(0)
         news = Santorini.execute_all(s,move)
         for i in range(n):
            end = Santorini.play_random_game(news)
            if (end[0] == onmove):
               scores[idx] = scores[idx]+1
            else:
               scores[idx]=scores[idx]-1
      best = None
      score = -numtimes*2
      for i in range(len(scores)):
         if scores[i] > score:
            best = moves[i]
            score = scores[i]
      return (best,score)
