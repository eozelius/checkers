def in_bounds(x1, y1, x2, y2):
  if x1 >= 0 and x1 <= 7 and \
     y1 >= 0 and y1 <= 7 and \
     x2 >= 0 and x2 <= 7 and \
     y2 >= 0 and y2 <= 7:
    return True
  else:
    print('Move() OutOfBoundsError. ')
    raise Exception('Out of bounds error')

def letter_to_number(letter):
  letter = letter.lower()
  if letter == 'a':
    return 0
  elif letter == 'b':
    return 1
  elif letter == 'c':
    return 2
  elif letter == 'd':
    return 3
  elif letter == 'e':
    return 4
  elif letter == 'f':
    return 5
  elif letter == 'g':
    return 6
  elif letter == 'h':
    return 7
  else:
    print('{} letter must be A-H'.format(letter))
    raise Exception('letter must be A-H')

class Move:
  def __init__(self, origin, destination):
    origin_x = int(origin[1]) - 1
    origin_y = letter_to_number(origin[0])
    destination_x = int(destination[1]) - 1
    destination_y = letter_to_number(destination[0])

    if in_bounds(origin_x, origin_y, destination_x, destination_y):
      self.origin_x = origin_x
      self.origin_y = origin_y
      self.destination_x = destination_x
      self.destination_y = destination_y

  def __repr__(self):
    return 'move: ({}, {}) => ({}, {})'.format(self.origin_x, self.origin_y, self.destination_x, self.destination_y)