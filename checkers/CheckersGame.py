from Board import Board

class CheckersGame:
  def __init__(self):
    self.board = Board()
    self.game_active = False
    self.red_pieces = 8
    self.black_pieces = 8
    self.active_color = None

  def start_game(self):
    self.game_active = True
    self.active_color = 'RED'
    print(self.board)

  def end_game(self):
    self.game_active = False
    self.active_color = None
    self.Board = Board()
    print('Thanks for playing')

  def game_over(self):
    return False

  def move(self, move):
    self.board.move(move)
    print(self.board)

    if self.game_over():
      self.game_active = False
