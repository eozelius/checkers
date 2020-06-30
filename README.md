## Ethan Ozelius Checkers Game - In Python
CLI python 3 implementation of classic checkers game.

### Quick start
To start a game
```bash
cd checkers
pwd
~/checkers

# must be run with 'checkers/' prefix, as checkers
# is a package within the checkers application
$ python3 checkers/checkers.py
```

### Making a move
When it is your turn to move, you will be prompted via the command line to make a **origin** and **destination** move.  Each of these are represented with an `(x, y)` *tuple*.  Example
```bash
> Red's turn!
> Select an Origin (x, y).
>>> (2, 3)
> Select a Destination (x, y).
>>> (4, 5)
```

### Pieces Coordinates
The board will be represented by a 2D array, 8 rows and 8 columns.  The board will start at (0, 0) in the top left corner.

```
     0   1   2   3   4   5   6   7   
   ---------------------------------
0  |   | B |   | B |   | B |   | B | 
   ---------------------------------
1  | B |   | B |   | B |   | B |   | 
   ---------------------------------
2  |   | B |   | B |   | B |   | B | 
   ---------------------------------
3  |   |   |   |   |   |   |   |   | 
   ---------------------------------
4  |   |   |   |   |   |   |   |   | 
   ---------------------------------
5  | R |   | R |   | R |   | R |   | 
   ---------------------------------
6  |   | R |   | R |   | R |   | R | 
   ---------------------------------
7  | R |   | R |   | R |   | R |   | 
   ---------------------------------
```