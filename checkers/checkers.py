from CheckersGame import CheckersGame
from Move import Move

if __name__ == '__main__':
  checkers = CheckersGame()
  checkers.start_game()

  while (checkers.game_active):
    origin = input(' >> xy origin => ')
    destination = input(' >> xy destination => ')

    move = Move(origin, destination)
    checkers.move(move)