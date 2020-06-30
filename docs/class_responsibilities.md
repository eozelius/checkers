__main__
  # start a new game
  game = Checkers()
  board = Board()
  game.start_game()

class Checkers
  - attributes
    + public <boolean> active
    + private remaining_red_pieces
    + private remaining_black_pieces
    + private whose_turn_is_it?

  __init__(self):
    self.board = Board()

  - public methods
    + end_game()
      print('game over')
    + start_game()
      self.active = true
    
      # set up while loop to get input from via commandline, 
      # until self.is_active is false
      while( self.is_active ) {
        # print whose turn it is.
        self.board.print_board()

        # get input from user

        # get origin and destination coordinates from user.
        # origin must contain a piece of that player's color.
        self.board.move(color, origin, destination)


        # check to see if game is complete
        black_pieces = utils.get_pieces_count('black')
        red_pieces = utils.get_pieces_count('red)
        if len(black_pieces == 0 || red_pieces == 0):
          self.is_active = false
      }

      self.end_game()

class Board
  - attributes
    # Board is an 8x8 2D array, containing a <Piece> instance, or null.
    private Array[][]<null || <Piece>> board

  - private methods
    + is_legal_move(board, origin, destination):
      # is destination in bound?
      # is destination square occupied by a piece of th

  - public methods
    + generate_board
    + print_board
    + move(<tuple(x, y)> origin, <tuple(x, y)> destination )

class Piece
  - attributes
    + is_queen
    + color

  - public methods
    + get_color
    + get/set is_queen()

  