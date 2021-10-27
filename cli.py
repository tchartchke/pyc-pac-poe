board = ['-'] * 9
positions = list(range(1, 10))

winningCombos = ( 
  [0, 1, 2], 
  [3, 4, 5], 
  [6, 7, 8], 
  [0, 3, 6], 
  [1, 4, 7], 
  [2, 5, 8], 
  [0, 4, 8], 
  [2, 4, 6] 
)

def printBoard(b):
  print(f" {b[0]} | {b[1]} | {b[2]} \n {b[3]} | {b[4]} | {b[5]} \n {b[6]} | {b[7]} | {b[8]} ")


def spaceOpen(position):
  return True if board[position] == '-' else False


def updateBoard(position, symbol):
    board[position] = symbol 


def getMove():
  position = input("Select position: ")
  try:
    return int(position)
  except: 
    print("Not a number")


def validMove(input):
  return True if input in positions and spaceOpen(input-1) else False


def takeTurn(symbol):
  position = getMove()
  while not position:
    position = getMove()
  if spaceOpen(position):
    updateBoard(position, symbol)


def gameIsWon():
  for combo in winningCombos:
    if not spaceOpen(combo[0]) and board[combo[0]] == board[combo[1]] == board[combo[2]]:
      return board[combo[0]]
  return False


def play():
  '''
  get player 1
  get player 2
  while no win
    play rounds
  congratulate winner
  '''

  p1 = input("Player 1 symbol: ")
  p2 = input("Player 2 symbol: ")

