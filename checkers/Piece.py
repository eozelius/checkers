class Piece:
  def __init__(self, color):
    self.color = color

  def get_color(self):
    return self.color

  def print_color(self):
    return 'B' if self.color == 'BLACK' else 'R'