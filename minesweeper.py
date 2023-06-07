"""
Author: Mesoma Okolocha
Lab: 12
File: minesweeper.py
Controls the minesweeper game.
"""

import random

class Tile(object):

    def __init__(self, hasBomb):
        """Creates a new tile."""
        self.hasBomb = hasBomb
        self.unknown = True
        self.neighbors = 0

    def __str__(self):
        """Returns the string representation of the tile."""
        if self.unknown == True:
            return "?"
        elif self.hasBomb != False:
            return "*"
        elif self.neighbors == 0:
            return " "
        else:
            return str(self.neighbors)


    def step(self):
        """Converts unknown to false."""
        self.unknown = False
        if self.hasBomb ==  True:
            return  True

        return False
           
            

    def increaseNeighbors(self):
        """Increases the total number of neighbors by one."""
        self.neighbors += 1

class Minesweeper(object):
    def __init__(self, size, mines):
        self.size = size
        self.mines = mines
        self.board = [[Tile(False) for row in range(int(self.size))] for col in range(int(self.size))]
        self.exploded = False
        self.tilesLeft = (self.size * self.size) - self.mines
        coordinates = []
        for row in range(len(self.board)):
            for col in range(len(self.board[0])):
                coordinates.append([row,col])
        for mine in range(self.mines):
            while True:
                [[row, column]] = random.sample(coordinates, 1)
                if self.board[row][column].hasBomb == False:
                    self.placeBomb(row, column)
                    break


    def isGameOver(self):
        if self.exploded == True:
            return True
        elif self.tilesLeft == 0:
            return True
        else:
            return False

    def placeBomb(self, row, column):

        self.board[row][column].hasBomb = True

        for r in range(row-1, row+2):
            if r >= 0 and r < self.size:
                if column-1 >= 0:
                    self.board[r][column-1].increaseNeighbors()
                if column+1 < self.size:
                    self.board[r][column+1].increaseNeighbors()
        if row-1 >= 0:
            self.board[row-1][column].increaseNeighbors()
        if row+1 < self.size:
            self.board[row+1][column].increaseNeighbors()
                    

    def step(self, row, column):
        self.tilesLeft -= 1
        if self.board[row][column].unknown == True:
            self.board[row][column].step()
            if self.board[row][column].hasBomb == True:
                self.exploded = True
            else:
                self.spread(row, column)


    def spread(self, row, column):
        if self.board[row][column].neighbors == 0:
            for r in range(row-1, row+2):
                if r >= 0 and r < self.size:
                    if column-1 >= 0 and self.board[r][column-1].unknown == True:
                        self.step(r, column-1)
                    if column+1 < self.size and self.board[r][column+1].unknown == True:
                        self.step(r, column+1)
            if row-1 >= 0 and self.board[row-1][column].unknown == True:
                self.step(row-1, column)
            if row+1 < self.size and self.board[row+1][column].unknown == True:
                self.step(row+1, column)
                    
            

    def showAll(self):
        for x in range(len(self.board)):
            for y in range(len(self.board[0])):
                self.board[x][y].unknown = False

   
