# import main Flask class and request object
from flask import Flask, request
import json
import sys
from newsant import NewSant
from newsant import SantMove
from minmax import Node
from minmax import alphabeta

# create the Flask app
app = Flask(__name__)


@app.route('/query-example')
def query_example():
    return 'Query String Example'

@app.route('/form-example')
def form_example():
    return 'Form Data Example'


@app.route('/move',methods=['POST'])
def move():
     data = request.json
     workers = data['workers']
     table = data['table']
     white_on_move = data['white_on_move']
     newSant = NewSant()
     newSant.table = table;
     newSant.workers = workers;
     newSant.white_on_move= white_on_move
     n = Node(newSant)
     depth = 3
     if(n.sant.white_on_move):
         sc= alphabeta(n,depth,-100000000,10000000,True)
     else:
         sc=alphabeta(n,depth,-100000000,100000000,False)
     resp = {}
     resp['table'] = sc[0].sant.table
     resp['workers'] = sc[0].sant.workers
     resp['white_on_move']=sc[0].sant.white_on_move
     resp['winner']=sc[0].sant.winner
     if(sc[0].sant.white_on_move == False):
         resp['on_move']='Red';
     else:
         resp['on_move']='Blue';
         
     if (resp['winner'] != None ):
         if(resp['winner']):
             resp['winner']='Blue'
         else:
             resp['winner']='Red'
     return json.dumps(resp)

@app.route('/play_move',methods=['POST'])
def odigraj():
     data = request.json
     print(data)
     game = data['game']
     print(game)
     move = data['move']
     print(move)
     workers = game['workers']
     table = game['table']
     white_on_move = game['white_on_move']

     newSant = NewSant()
     newSant.table = table;
     newSant.workers = workers;
     newSant.white_on_move= white_on_move
     humanMove = SantMove(int(move['who'])-1,
                              int(move['move']),
                              int(move['build']))
     newSant.execute_move(humanMove)

     resp = {}
     resp['table'] = newSant.table
     resp['workers'] = newSant.workers
     resp['white_on_move']=newSant.white_on_move
     resp['winner']=newSant.winner
     if(newSant.white_on_move == False):
         resp['on_move']='Red';
     else:
         resp['on_move']='Blue';
         
     if (resp['winner'] != None ):
         if(resp['winner']):
             resp['winner']='Blue'
         else:
             resp['winner']='Red'
     return json.dumps(resp)

 
if __name__ == '__main__':
    # run app in debug mode on port 5000
     app.run(debug=True, port=5000)
