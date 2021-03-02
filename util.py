import math
class Util:
    players = ["White","Black"]
    piece_labels=["WF","WM","BF","BM"]
    start = [0,0,0,0,0,
               0,0,0,0,0,
               0,0,0,0,0,
               0,0,0,0,0,
               0,0,0,0,0,
               0,0,0,0,0,
             0,0]
    
    def shash(santorini):
        return ";".join(map(str,santorini))

    def add_or_update_state_score(states,state,winner):
        strstate=Util.shash(state)
        if(strstate in states):
            s,score = states[strstate]
            states[strstate] = (state,score+winner)
        else:
            states[strstate] =(state,winner)

    def add_all_rotation(states,state,winner):
        Util.add_or_update_state_score(states,state,winner)
        state1 =Util.rotate(state)
        Util.add_or_update_state_score(states,state1,winner)
        state2 = Util.rotate(state1)
        Util.add_or_update_state_score(states,state2,winner)
        state3 = Util.rotate(state2)
        Util.add_or_update_state_score(states,state3,winner)

        
    def rotate(santorini):
        rot = [ [1,21],[2,16],[3,11],[4,6],[5,1],
                [6,22],[7,17],[8,12],[9,7],[10,2],
                [11,23],[12,18],[13,13],[14,8],[15,3],
                [16,24],[17,19],[18,14],[19,9],[20,4],
                [21,25],[22,20],[23,15],[24,10],[25,5]]
        #table is at 5.
        result = santorini[:]
        for r in rot:
            result[4+r[1]]=santorini[4+r[0]]
        #We must rotate player positions
        for k in range(1,1+4):
            result[k] = rot[result[k]-1][1]
        return result     
    def tuple_to_id(xy):
        row,col = xy
        return (row-1)*5 + (col)
        
    def id_to_tuple(id):
        col = id % 5
        row = math.floor(id/5)
        return (row,col)

    def piece_pos(piece,santorini):
        pindex=Util.piece_labels.index(piece)
        return santorini[1+pindex]
    
    action_labels=["PUT","MOVE","BULID","END","SELECT"]
   
    cell_labels=["A1","A2","A3","A4","A5",
                "B1","B2","B3","B4","B5",
                "C1","C2","C3","C4","C5",
                "D1","D2","D3","D4","D5",
                "E1","E2","E3","E4","E5"]

    cell_neighbors=[[2,6,7], #1 
                   [1,3,6,7,8], #2
                   [2,4,7,8,9],  #3 
                   [3,5,8,9,10], #4
                   [4,9,10],  #5

                   [1,2,7,11,12], #6
                   [1,2,3,6,8,11,12,13], #7
                   [2,3,4,7,9,12,13,14], #8
                   [3,4,5,8,10,13,14,15], #9
                   [4,5,9,14,15], #10 

                   [6,7,12,16,17], #11
                   [6,7,8,11,13,16,17,18], #12
                   [7,8,9,12,14,17,18,19], #13
                   [8,9,10,13,15,18,19,20], #14
                   [9,10,14,19,20], #15

                   [11,12,17,21,22], #16
                   [11,12,13,16,18,21,22,23], #17
                   [12,13,14,17,19,22,23,24], #18
                   [13,14,15,18,20,23,24,25], #19
                   [14,15,19,24,25], #20

                   [16,17,22,], #21
                   [16,17,18,21,23], #22
                   [17,18,19,22,24], #23
                   [18,19,20,23,25], #24
                   [19,20,24]] #25
    def cell_string(cell):
        if (cell == 0):
            return "out of board"
        return con.cell_labels[cell-1]
    
    def piece_index(piecestring):
        ind = Util.piece_labels.index(piecestring)
        return ind + 1

    def decompose_santorini(santorini):
        onmove = santorini[0]
        action = santorini[30]
        table = santorini[5:30]
        positions = santorini[1:5]
        selected = santorini[31]
        return ( onmove,action,table,positions,selected)
