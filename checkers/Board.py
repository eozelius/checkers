from Piece import Piece

class Board:
  def __init__(self):
    self.board = self.generate_board()
    print(self)

  def generate_board(self):
    board = []

    for row in range(0, 8):
      board.append([])
      for col in range(0, 8):
        board[row].append(None)
    
    for x in range(0, 8):
      for y in range(0, 8):
        x_is_even = x % 2 == 0
        y_is_even = y % 2 == 0

        # black pieces
        if x in range(0, 3):
          if x_is_even and not y_is_even:
            board[x][y] = 'BLK'
          if not x_is_even and y_is_even:
            board[x][y] = 'BLK'
        
        if x in range(5, 8):
          if not x_is_even and y_is_even:
            board[x][y] = 'RED'
          if x_is_even and not y_is_even:
            board[x][y] = 'RED'
    return board

  def __repr__(self):
    print()
    print('     0   1   2   3   4   5   6   7   ')
    for row in range(0, 8):
      print('  ', '-' * 33)
      print(row, ' | ', end='')
      for col in range(0, 8):
        to_print = ' '

        if self.board[row][col] == 'BLK':
          to_print = 'B'
        elif self.board[row][col] == 'RED':
          to_print = 'R'
        print(to_print, end=' | ')
      print()
    print('  ', '-' * 33)
    return ''