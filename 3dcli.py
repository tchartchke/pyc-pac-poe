class ThrycThracThroe:
  WIN_COMBOS = (
   
  )

  def __init__(self):
    self.board = [[['x'] * 4] * 4] * 4

  def display_board(self):
    format = f"""
 {self.board[0][0][0]} | {self.board[0][0][1]} | {self.board[0][0][2]} | {self.board[0][0][3]}      {self.board[1][0][0]} | {self.board[1][0][1]} | {self.board[1][0][2]} | {self.board[1][0][3]}      {self.board[2][0][0]} | {self.board[2][0][1]} | {self.board[2][0][2]} | {self.board[2][0][3]} 
---------------    ---------------    ---------------
 {self.board[0][1][0]} | {self.board[0][1][1]} | {self.board[0][1][2]} | {self.board[0][1][3]}      {self.board[1][1][0]} | {self.board[1][1][1]} | {self.board[1][1][2]} | {self.board[1][1][3]}      {self.board[2][1][0]} | {self.board[2][1][1]} | {self.board[2][1][2]} | {self.board[2][1][3]} 
---------------    ---------------    ---------------
 {self.board[0][2][0]} | {self.board[0][2][1]} | {self.board[0][2][2]} | {self.board[0][2][3]}      {self.board[1][2][0]} | {self.board[1][2][1]} | {self.board[1][2][2]} | {self.board[1][2][3]}      {self.board[2][2][0]} | {self.board[2][2][1]} | {self.board[2][2][2]} | {self.board[2][2][3]} 
---------------    ---------------    ---------------
 {self.board[0][3][0]} | {self.board[0][3][1]} | {self.board[0][3][2]} | {self.board[0][3][3]}      {self.board[1][3][0]} | {self.board[1][3][1]} | {self.board[1][3][2]} | {self.board[1][3][3]}      {self.board[2][3][0]} | {self.board[2][3][1]} | {self.board[2][3][2]} | {self.board[2][3][3]} """
    print(format)

game = ThrycThracThroe()

game.display_board()