import chess

class State():
    def __init__(self, board):
        self.board = chess.Board()


    def Board(self):
        print(self.board)





if "__main__" == __name__:
    state = State()
    state.Board()
