class PycPacPoe:
  WIN_COMBOS = ( 
    [0, 1, 2], 
    [3, 4, 5], 
    [6, 7, 8], 
    [0, 3, 6], 
    [1, 4, 7], 
    [2, 5, 8], 
    [0, 4, 8], 
    [2, 4, 6] 
  )
  def __init__(self):
    self.board = [' '] * 9

  def display_board(self):
    print(f" {self.board[0]} | {self.board[1]} | {self.board[2]} \n-----------\n {self.board[3]} | {self.board[4]} | {self.board[5]} \n-----------\n {self.board[6]} | {self.board[7]} | {self.board[8]} ")

  def input_to_index(self, input):
    return int(input) - 1

  def move(self, index, token = 'X'):
    self.board[index] = token

  def is_position_taken(self, index):
    return False if self.board[index] == ' ' else True

  def is_valid_move(self, index):
    return index in range(0,9) and not self.is_position_taken(index)
  
  def turn(self):
    position = self.input_to_index(input("Input position (1-9): "))
    while not self.is_valid_move(position):
      print("Not a valid position. Please try again.")
      position = self.input_to_index(input("Input position (1-9): "))

    print("before move")
    self.move(position, self.current_player())
    self.display_board()

  def turn_count(self):
    return 9 - self.board.count(' ')

  def current_player(self):
    return 'X' if self.turn_count() % 2 == 0 else 'O'

  def is_won(self):
    for combo in self.WIN_COMBOS:
      if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] != ' ':
        return True
    return False

  def is_full(self):
    return ' ' not in self.board

  def is_draw(self):
    return self.is_full() and not self.is_won()

  def is_over(self):
    return self.is_draw() or self.is_won()

  def winner(self):
    return 'X' if self.turn_count() % 2 == 1 else 'O'

  def play(self):
    while not self.is_over():
      self.turn()
    print("Game Complete")
    if self.is_won(): 
      print(f"Congrats {self.winner()}")
    else:
      print("Tie")


game = PycPacPoe()
game.play()