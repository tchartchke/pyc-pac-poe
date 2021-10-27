board = ['-'] * 9
positions = list(range(1, 10))


# winning combos: 
# 0 1 2 
# 3 4 5 
# 6 7 8 
# 0 3 6 
# 1 4 7 
# 2 5 8 
# 0 4 8 
# 2 4 6

def printBoard(b):
  print(f" {b[0]} | {b[1]} | {b[2]} \n {b[3]} | {b[4]} | {b[5]} \n {b[6]} | {b[7]} | {b[8]} ")

def spaceOccupied(position):
  return True if board[position] == '-' else False

def updateBoard(position, symbol):
    board[position] = symbol 

def takeTurn(symbol):
  position = input("Enter position number")
  if not spaceOccupied(position):
    updateBoard(position, symbol)
  pass

def play():
  '''
  get player 1
  get player 2
  
  start round
  '''
  pass
