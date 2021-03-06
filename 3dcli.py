class ThrycThracThroe:
  WIN_COMBOS = (
    # potato slices
    [[0,0,0], [0,0,1], [0,0,2], [0,0,3]],
    [[0,1,0], [0,1,1], [0,1,2], [0,1,3]],
    [[0,2,0], [0,2,1], [0,2,2], [0,2,3]],
    [[0,3,0], [0,3,1], [0,3,2], [0,3,3]],

    [[1,0,0], [1,0,1], [1,0,2], [1,0,3]],
    [[1,1,0], [1,1,1], [1,1,2], [1,1,3]],
    [[1,2,0], [1,2,1], [1,2,2], [1,2,3]],
    [[1,3,0], [1,3,1], [1,3,2], [1,3,3]],

    [[2,0,0], [2,0,1], [2,0,2], [2,0,3]],
    [[2,1,0], [2,1,1], [2,1,2], [2,1,3]],
    [[2,2,0], [2,2,1], [2,2,2], [2,2,3]],
    [[2,3,0], [2,3,1], [2,3,2], [2,3,3]],

    [[3,0,0], [3,0,1], [3,0,2], [3,0,3]],
    [[3,1,0], [3,1,1], [3,1,2], [3,1,3]],
    [[3,2,0], [3,2,1], [3,2,2], [3,2,3]],
    [[3,3,0], [3,3,1], [3,3,2], [3,3,3]],

    [[0,0,0], [0,1,0], [0,2,0], [0,3,0]],
    [[0,0,1], [0,1,1], [0,2,1], [0,3,1]],
    [[0,0,2], [0,1,2], [0,2,2], [0,3,2]],
    [[0,0,3], [0,1,3], [0,2,3], [0,3,3]],

    [[1,0,0], [1,1,0], [1,2,0], [1,3,0]],
    [[1,0,1], [1,1,1], [1,2,1], [1,3,1]],
    [[1,0,2], [1,1,2], [1,2,2], [1,3,2]],
    [[1,0,3], [1,1,3], [1,2,3], [1,3,3]],

    [[2,0,0], [2,1,0], [2,2,0], [2,3,0]],
    [[2,0,1], [2,1,1], [2,2,1], [2,3,1]],
    [[2,0,2], [2,1,2], [2,2,2], [2,3,2]],
    [[2,0,3], [2,1,3], [2,2,3], [2,3,3]],

    [[3,0,0], [3,1,0], [3,2,0], [3,3,0]],
    [[3,0,1], [3,1,1], [3,2,1], [3,3,1]],
    [[3,0,2], [3,1,2], [3,2,2], [3,3,2]],
    [[3,0,3], [3,1,3], [3,2,3], [3,3,3]],

    [[0,0,0], [1,0,0], [2,0,0], [3,0,0]],
    [[0,0,1], [1,0,1], [2,0,1], [3,0,1]],
    [[0,0,2], [1,0,2], [2,0,2], [3,0,2]],
    [[0,0,3], [1,0,3], [2,0,3], [3,0,3]],

    [[0,1,0], [1,1,0], [2,1,0], [3,1,0]],
    [[0,1,1], [1,1,1], [2,1,1], [3,1,1]],
    [[0,1,2], [1,1,2], [2,1,2], [3,1,2]],
    [[0,1,3], [1,1,3], [2,1,3], [3,1,3]],

    [[0,2,0], [1,2,0], [2,2,0], [3,2,0]],
    [[0,2,1], [1,2,1], [2,2,1], [3,2,1]],
    [[0,2,2], [1,2,2], [2,2,2], [3,2,2]],
    [[0,2,3], [1,2,3], [2,2,3], [3,2,3]],

    [[0,3,0], [1,3,0], [2,3,0], [3,3,0]],
    [[0,3,1], [1,3,1], [2,3,1], [3,3,1]],
    [[0,3,2], [1,3,2], [2,3,2], [3,3,2]],
    [[0,3,3], [1,3,3], [2,3,3], [3,3,3]],  

    # diagonal slices
    [[0,0,0], [1,0,1], [2,0,2], [3,0,3]],
    [[0,1,0], [1,1,1], [2,1,2], [3,1,3]],
    [[0,2,0], [1,2,1], [2,2,2], [3,2,3]],
    [[0,3,0], [1,3,1], [2,3,2], [3,3,3]],

    [[3,0,0], [2,0,1], [3,0,2], [3,0,3]],
    [[3,1,0], [2,1,1], [3,1,2], [3,1,3]],
    [[3,2,0], [2,2,1], [3,2,2], [3,2,3]],
    [[3,3,0], [2,3,1], [3,3,2], [3,3,3]],

    [[0,0,0], [1,1,0], [2,2,0], [3,3,0]],
    [[0,0,1], [1,1,1], [2,2,1], [3,3,1]],
    [[0,0,2], [1,1,2], [2,2,2], [3,3,2]],
    [[0,0,3], [1,1,3], [2,2,3], [3,3,3]],

    [[3,0,0], [2,1,0], [1,2,0], [0,3,0]],
    [[3,0,1], [2,1,1], [1,2,1], [0,3,1]],
    [[3,0,2], [2,1,2], [1,2,2], [0,3,2]],
    [[3,0,3], [2,1,3], [1,2,3], [0,3,3]],

    [[0,0,0], [0,1,1], [0,2,2], [0,3,3]],
    [[1,0,0], [1,1,1], [1,2,2], [1,3,3]],
    [[2,0,0], [2,1,1], [2,2,2], [2,3,3]],
    [[3,0,0], [3,1,1], [3,2,2], [3,3,3]],

    [[0,3,0], [0,2,1], [0,1,2], [0,0,3]],
    [[1,3,0], [1,2,1], [1,1,2], [1,0,3]],
    [[2,3,0], [2,2,1], [2,1,2], [1,0,3]],
    [[3,3,0], [3,2,1], [3,1,2], [2,0,3]],

    # cross-diagonals
    [[0,0,0], [1,1,1], [2,2,2], [3,3,3]],
    [[0,3,0], [1,2,1], [2,1,2], [3,0,3]],
    [[3,0,0], [2,1,1], [1,2,2], [0,3,3]],
    [[3,3,0], [2,2,1], [1,1,2], [0,0,3]]
  )

  def __init__(self):
    self.board = [[[' ', ' ', ' ', ' '], [' ', ' ', ' ', ' '], [' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ']], [[' ', ' ', ' ', ' '], [' ', ' ', ' ', ' '], [' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ']], [[' ', ' ', ' ', ' '], [' ', ' ', ' ', ' '], [' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ']], [[' ', ' ', ' ', ' '], [' ', ' ', ' ', ' '], [' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ']]]

  def display_board(self):
    format = f"""       (1)                (2)                (3)                (4)
  1   2   3   4      1   2   3   4      1   2   3   4      1   2   3   4     
1 {self.board[0][0][0]} | {self.board[0][0][1]} | {self.board[0][0][2]} | {self.board[0][0][3]}      {self.board[1][0][0]} | {self.board[1][0][1]} | {self.board[1][0][2]} | {self.board[1][0][3]}      {self.board[2][0][0]} | {self.board[2][0][1]} | {self.board[2][0][2]} | {self.board[2][0][3]}      {self.board[3][0][0]} | {self.board[3][0][1]} | {self.board[3][0][2]} | {self.board[3][0][3]} 
 ---------------    ---------------    ---------------    ---------------
2 {self.board[0][1][0]} | {self.board[0][1][1]} | {self.board[0][1][2]} | {self.board[0][1][3]}      {self.board[1][1][0]} | {self.board[1][1][1]} | {self.board[1][1][2]} | {self.board[1][1][3]}      {self.board[2][1][0]} | {self.board[2][1][1]} | {self.board[2][1][2]} | {self.board[2][1][3]}      {self.board[3][1][0]} | {self.board[3][1][1]} | {self.board[3][1][2]} | {self.board[3][1][3]} 
 ---------------    ---------------    ---------------    ---------------
3 {self.board[0][2][0]} | {self.board[0][2][1]} | {self.board[0][2][2]} | {self.board[0][2][3]}      {self.board[1][2][0]} | {self.board[1][2][1]} | {self.board[1][2][2]} | {self.board[1][2][3]}      {self.board[2][2][0]} | {self.board[2][2][1]} | {self.board[2][2][2]} | {self.board[2][2][3]}      {self.board[3][2][0]} | {self.board[3][2][1]} | {self.board[3][2][2]} | {self.board[3][2][3]} 
 ---------------    ---------------    ---------------    ---------------
4 {self.board[0][3][0]} | {self.board[0][3][1]} | {self.board[0][3][2]} | {self.board[0][3][3]}      {self.board[1][3][0]} | {self.board[1][3][1]} | {self.board[1][3][2]} | {self.board[1][3][3]}      {self.board[2][3][0]} | {self.board[2][3][1]} | {self.board[2][3][2]} | {self.board[2][3][3]}      {self.board[3][3][0]} | {self.board[3][3][1]} | {self.board[3][3][2]} | {self.board[3][3][3]} """
    print(format)

  def input_to_coord(self, input):
    return [int(input[0])-1, int(input[1])-1, int(input[2])-1]

  def move(self, index, token = 'X'):
    self.board[index[0]][index[2]][index[1]] = token

  def is_position_taken(self, index):
    return False if self.board[index[0]][index[1]][index[2]] == ' ' else True

  def is_valid_move(self, index):
    return index[0] in range(0,4) and index[1] in range(0,4) and index[2] in range(0,4) and not self.is_position_taken(index)

  def turn(self):
    print(f"Current player: {self.current_player()}")
    position = self.input_to_coord(input("Input position (eg. board 1, column 3, row 2 as 132): "))
    while not self.is_valid_move(position):
      print("Not a valid position. Please try again.")
      position = self.input_to_coord(input("Input position (eg. board 1, column 3, row 2 as 132): "))
    self.move(position, self.current_player())
    self.display_board()

  def turn_count(self):
    i = 0
    for board in self.board:
      for x in board:
        for y in x:
          if y == ' ': i+=1
    return 48 - i

  def current_player(self):
    return 'X' if self.turn_count() % 2 == 0 else 'O'

  def is_full(self):
    return self.turn_count() > 47

  def is_won(self):
    for combos in self.WIN_COMBOS:
      if self.board[combos[0][0]][combos[0][1]][combos[0][2]] == self.board[combos[1][0]][combos[1][1]][combos[1][2]] == self.board[combos[2][0]][combos[2][1]][combos[2][2]] == self.board[combos[3][0]][combos[3][1]][combos[3][2]] != ' ':
        return True
    return False
  
  def is_draw(self):
    return self.is_full() and not self.is_won()

  def is_over(self):
    return self.is_draw() or self.is_won()

  def winner(self):
    return 'X' if self.turn_count() % 2 == 1 else 'O'

  def play(self):
    print("This is PvP 4x4 3d tic-tac-toe")
    self.display_board()
    while not self.is_over():
      self.turn()
    print("Game Complete")
    if self.is_won(): 
      print(f"Congrats {self.winner()}")
    else:
      print("Tie")

game = ThrycThracThroe()
game.play()


# TODO:
# something is wrong with move validations
# error handling