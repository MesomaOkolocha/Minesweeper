"""
Author: Liz Matthews
File: minesweeperGUI.py

Displays a window with multiple buttons and plays the connect four game.
"""

from breezypythongui import EasyFrame
from tkinter import PhotoImage
from minesweeper import Minesweeper

class MinesweeperGUI(EasyFrame):

   def __init__(self):
      """Creates the minesweeper game with buttons."""
      super().__init__(title = "Minesweeper", resizable=False)
      
      # Size is 10 x 10
      self.size = 10
      
      # Starts with 10 mines
      self.mines = 10
      
      # Create a minesweeper game and set the size appropriately
      self.game = Minesweeper(size=self.size, mines=self.mines)      
      self.setSize(45 * len(self.game.board), 45 * len(self.game.board[0]))
      
      # Create size x size buttons for the game
      self.boardButtons = []
      for row in range(len(self.game.board)):
         self.boardButtons.append([])
         for column in range(len(self.game.board[row])):         
            self.boardButtons[-1].append(self.addButton(row = row,
                                                     column = column,
                                                     text = "",
                                                     command=self.makeMoveFunction(row, column),
                                                     bg="white",
                                                     fg="black"))
            
      self.setButtons()
      
      # Add a new game button
      self.newGameButton = self.addButton(row = len(self.game.board),
                                          column = len(self.game.board)-1,
                                          text = "New",
                                          command = self.newGame,
                                          state = "disabled")
      
   def makeMoveFunction(self, row, column):
      return lambda: self.nextMove(row, column)
      
   def setButtons(self):
      """Sets the buttons' text based on the state of the game."""
      for row in range(len(self.game.board)):
         for col in range(len(self.game.board[row])):
            self.boardButtons[row][col]["text"] = "{:^5s}".format(str(self.game.board[row][col]))
            if not self.game.board[row][col].unknown:
               self.boardButtons[row][col]["state"] = "disabled"

   def nextMove(self, row, column):
      """Makes a move in the game and updates the view with
      the results."""
     
      # Update the model and view
      self.game.step(row, column)
      self.setButtons()
      
      # Detect game over
      if self.game.isGameOver():
         # Show all the tiles and update view
         self.game.showAll()
         self.setButtons()
         
         # Detect endgame state
         if self.game.exploded:
            text = "You lost!"
         else:
            text = "You won!"
         self.messageBox("Game Is Over!", text)
         
         # Disable movement buttons and enable new game button
         for buttonRow in self.boardButtons:
            for b in buttonRow:
               b["state"] = "disabled"
         self.newGameButton["state"] = "normal"

   def newGame(self):
      """Create a new minesweeper game and updates the view."""
      self.game = Minesweeper(size=self.size, mines=self.mines)
      self.setButtons()      
      
      # Enable movement buttons and disable new game button
      self.newGameButton["state"] = "disabled"      
      for buttonRow in self.boardButtons:
         for b in buttonRow:
            b["state"] = "normal"

def main():
   app = MinesweeperGUI()
   app.mainloop()

if __name__ == "__main__":
   main()
