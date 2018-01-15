from pystockfish import *
SEARCH_DEPTH = 19
SEARCH_TIME = 1000


class chess_engine_wrapper:

    def __init__(self):
         self.chess_engine = Engine(depth=SEARCH_DEPTH)
         self.moves = []

    def get_best_move(self, last_rival_move = None):
        self.chess_engine.setposition(self.moves)
        best_move = (self.chess_engine.bestmove())['move']
        return best_move

    def update_move(self, my_move):
        self.moves.append(str(my_move[0]) + str(my_move[1]))

def chess_engine_tester():
    chess_engine = chess_engine_wrapper()
    while True:
        rival_move = input('insert_rival_move')
        best_move = chess_engine.get_best_move(rival_move)
        print(best_move)


#chess_engine_tester()