class SantMove:
    def __init__(self,who,move,build):
        self.who=who
        self.move=move
        self.build=build
    def __str__(self):
        return 'Worker {} move to {} and build {}'.format(self.who,self.move,self.build)
