##!/usr/bin/env python
# Name : Deepthi chiluka
# UTA ID: 1002028543

import copy
import random
import sys

class maxConnect4Game:
    def __init__(self):
        self.gameBoard = [[0 for i in range(7)] for j in range(6)]
        self.self.currentMove = 1
        self.player1Score = 0
        self.player2Score = 0
        self.pieceCount = 0
        self.gameFile = None
        self.moveOver = None
        random.seed()
#to countt number of pieces already played in the game
    def checkPieceCount(self):
        self.pieceCount = sum(1 for row in self.gameBoard for piece in row if piece)
#output game to console
    def printGameBoard(self):
        print (' -----------------')
        for i in range(6):
            print(self.gameBoard[i])
        print (' -----------------')
#output game to file
    def printGameBoardToFile(self):
        for row in self.gameBoard:
            self.gameFile.write(''.join(str(col) for col in row) + '\r\n')
        self.gameFile.write('%s\r\n' % str(self.currentMove))

    def playPiece(self, column):
        if not self.gameBoard[0][column]:
            for i in range(5, -1, -1):         
                if not self.gameBoard[i][column]:
                    self.gameBoard[i][column] = self.currentMove
                    self.pieceCount += 1
                    return 1

    def aiPlay(self, depth, value):
    
        self.childNodes(depth - 1, value)
        column = self.selectBestMove(value)
        result = self.playPiece(column)
        if not result:
            self.aiPlay(depth, value)
        else:
            print('\n\nmove %d: Player %d, column %d\n' % (self.pieceCount, self.currentMove, column+1))
        return

    def countScore(self):
        self.player1Score = 0
        self.player2Score = 0
        for row in self.gameBoard:

            if row[0:4] == [1]*4:
                self.player1Score += 1
            if row[1:5] == [1]*4:
                self.player1Score += 1
            if row[2:6] == [1]*4:
                self.player1Score += 1
            if row[3:7] == [1]*4:
                self.player1Score += 1
        
            if row[0:4] == [2]*4:
                self.player2Score += 1
            if row[1:5] == [2]*4:
                self.player2Score += 1
            if row[2:6] == [2]*4:
                self.player2Score += 1
            if row[3:7] == [2]*4:
                self.player2Score += 1
#checking vertically for player 2
        for j in range(7):
            
            if (self.gameBoard[0][j] == 1 and self.gameBoard[1][j] == 1 and
                   self.gameBoard[2][j] == 1 and self.gameBoard[3][j] == 1):
                self.player1Score += 1
            if (self.gameBoard[1][j] == 1 and self.gameBoard[2][j] == 1 and
                   self.gameBoard[3][j] == 1 and self.gameBoard[4][j] == 1):
                self.player1Score += 1
            if (self.gameBoard[2][j] == 1 and self.gameBoard[3][j] == 1 and
                   self.gameBoard[4][j] == 1 and self.gameBoard[5][j] == 1):
                self.player1Score += 1
            
            if (self.gameBoard[0][j] == 2 and self.gameBoard[1][j] == 2 and
                   self.gameBoard[2][j] == 2 and self.gameBoard[3][j] == 2):
                self.player2Score += 1
            if (self.gameBoard[1][j] == 2 and self.gameBoard[2][j] == 2 and
                   self.gameBoard[3][j] == 2 and self.gameBoard[4][j] == 2):
                self.player2Score += 1
            if (self.gameBoard[2][j] == 2 and self.gameBoard[3][j] == 2 and
                   self.gameBoard[4][j] == 2 and self.gameBoard[5][j] == 2):
                self.player2Score += 1

#checking diagonally for player 1
        if (self.gameBoard[2][0] == 1 and self.gameBoard[3][1] == 1 and
               self.gameBoard[4][2] == 1 and self.gameBoard[5][3] == 1):
            self.player1Score += 1
        if (self.gameBoard[1][0] == 1 and self.gameBoard[2][1] == 1 and
               self.gameBoard[3][2] == 1 and self.gameBoard[4][3] == 1):
            self.player1Score += 1
        if (self.gameBoard[2][1] == 1 and self.gameBoard[3][2] == 1 and
               self.gameBoard[4][3] == 1 and self.gameBoard[5][4] == 1):
            self.player1Score += 1
        if (self.gameBoard[0][0] == 1 and self.gameBoard[1][1] == 1 and
               self.gameBoard[2][2] == 1 and self.gameBoard[3][3] == 1):
            self.player1Score += 1
        if (self.gameBoard[1][1] == 1 and self.gameBoard[2][2] == 1 and
               self.gameBoard[3][3] == 1 and self.gameBoard[4][4] == 1):
            self.player1Score += 1
        if (self.gameBoard[2][2] == 1 and self.gameBoard[3][3] == 1 and
               self.gameBoard[4][4] == 1 and self.gameBoard[5][5] == 1):
            self.player1Score += 1
        if (self.gameBoard[0][1] == 1 and self.gameBoard[1][2] == 1 and
               self.gameBoard[2][3] == 1 and self.gameBoard[3][4] == 1):
            self.player1Score += 1
        if (self.gameBoard[1][2] == 1 and self.gameBoard[2][3] == 1 and
               self.gameBoard[3][4] == 1 and self.gameBoard[4][5] == 1):
            self.player1Score += 1
        if (self.gameBoard[2][3] == 1 and self.gameBoard[3][4] == 1 and
               self.gameBoard[4][5] == 1 and self.gameBoard[5][6] == 1):
            self.player1Score += 1
        if (self.gameBoard[0][2] == 1 and self.gameBoard[1][3] == 1 and
               self.gameBoard[2][4] == 1 and self.gameBoard[3][5] == 1):
            self.player1Score += 1
        if (self.gameBoard[1][3] == 1 and self.gameBoard[2][4] == 1 and
               self.gameBoard[3][5] == 1 and self.gameBoard[4][6] == 1):
            self.player1Score += 1
        if (self.gameBoard[0][3] == 1 and self.gameBoard[1][4] == 1 and
               self.gameBoard[2][5] == 1 and self.gameBoard[3][6] == 1):
            self.player1Score += 1

        if (self.gameBoard[0][3] == 1 and self.gameBoard[1][2] == 1 and
               self.gameBoard[2][1] == 1 and self.gameBoard[3][0] == 1):
            self.player1Score += 1
        if (self.gameBoard[0][4] == 1 and self.gameBoard[1][3] == 1 and
               self.gameBoard[2][2] == 1 and self.gameBoard[3][1] == 1):
            self.player1Score += 1
        if (self.gameBoard[1][3] == 1 and self.gameBoard[2][2] == 1 and
               self.gameBoard[3][1] == 1 and self.gameBoard[4][0] == 1):
            self.player1Score += 1
        if (self.gameBoard[0][5] == 1 and self.gameBoard[1][4] == 1 and
               self.gameBoard[2][3] == 1 and self.gameBoard[3][2] == 1):
            self.player1Score += 1
        if (self.gameBoard[1][4] == 1 and self.gameBoard[2][3] == 1 and
               self.gameBoard[3][2] == 1 and self.gameBoard[4][1] == 1):
            self.player1Score += 1
        if (self.gameBoard[2][3] == 1 and self.gameBoard[3][2] == 1 and
               self.gameBoard[4][1] == 1 and self.gameBoard[5][0] == 1):
            self.player1Score += 1
        if (self.gameBoard[0][6] == 1 and self.gameBoard[1][5] == 1 and
               self.gameBoard[2][4] == 1 and self.gameBoard[3][3] == 1):
            self.player1Score += 1
        if (self.gameBoard[1][5] == 1 and self.gameBoard[2][4] == 1 and
               self.gameBoard[3][3] == 1 and self.gameBoard[4][2] == 1):
            self.player1Score += 1
        if (self.gameBoard[2][4] == 1 and self.gameBoard[3][3] == 1 and
               self.gameBoard[4][2] == 1 and self.gameBoard[5][1] == 1):
            self.player1Score += 1
        if (self.gameBoard[1][6] == 1 and self.gameBoard[2][5] == 1 and
               self.gameBoard[3][4] == 1 and self.gameBoard[4][3] == 1):
            self.player1Score += 1
        if (self.gameBoard[2][5] == 1 and self.gameBoard[3][4] == 1 and
               self.gameBoard[4][3] == 1 and self.gameBoard[5][2] == 1):
            self.player1Score += 1
        if (self.gameBoard[2][6] == 1 and self.gameBoard[3][5] == 1 and
               self.gameBoard[4][4] == 1 and self.gameBoard[5][3] == 1):
            self.player1Score += 1
#checking player 2

        if (self.gameBoard[2][0] == 2 and self.gameBoard[3][1] == 2 and
               self.gameBoard[4][2] == 2 and self.gameBoard[5][3] == 2):
            self.player2Score += 1
        if (self.gameBoard[1][0] == 2 and self.gameBoard[2][1] == 2 and
               self.gameBoard[3][2] == 2 and self.gameBoard[4][3] == 2):
            self.player2Score += 1
        if (self.gameBoard[2][1] == 2 and self.gameBoard[3][2] == 2 and
               self.gameBoard[4][3] == 2 and self.gameBoard[5][4] == 2):
            self.player2Score += 1
        if (self.gameBoard[0][0] == 2 and self.gameBoard[1][1] == 2 and
               self.gameBoard[2][2] == 2 and self.gameBoard[3][3] == 2):
            self.player2Score += 1
        if (self.gameBoard[1][1] == 2 and self.gameBoard[2][2] == 2 and
               self.gameBoard[3][3] == 2 and self.gameBoard[4][4] == 2):
            self.player2Score += 1
        if (self.gameBoard[2][2] == 2 and self.gameBoard[3][3] == 2 and
               self.gameBoard[4][4] == 2 and self.gameBoard[5][5] == 2):
            self.player2Score += 1
        if (self.gameBoard[0][1] == 2 and self.gameBoard[1][2] == 2 and
               self.gameBoard[2][3] == 2 and self.gameBoard[3][4] == 2):
            self.player2Score += 1
        if (self.gameBoard[1][2] == 2 and self.gameBoard[2][3] == 2 and
               self.gameBoard[3][4] == 2 and self.gameBoard[4][5] == 2):
            self.player2Score += 1
        if (self.gameBoard[2][3] == 2 and self.gameBoard[3][4] == 2 and
               self.gameBoard[4][5] == 2 and self.gameBoard[5][6] == 2):
            self.player2Score += 1
        if (self.gameBoard[0][2] == 2 and self.gameBoard[1][3] == 2 and
               self.gameBoard[2][4] == 2 and self.gameBoard[3][5] == 2):
            self.player2Score += 1
        if (self.gameBoard[1][3] == 2 and self.gameBoard[2][4] == 2 and
               self.gameBoard[3][5] == 2 and self.gameBoard[4][6] == 2):
            self.player2Score += 1
        if (self.gameBoard[0][3] == 2 and self.gameBoard[1][4] == 2 and
               self.gameBoard[2][5] == 2 and self.gameBoard[3][6] == 2):
            self.player2Score += 1

        if (self.gameBoard[0][3] == 2 and self.gameBoard[1][2] == 2 and
               self.gameBoard[2][1] == 2 and self.gameBoard[3][0] == 2):
            self.player2Score += 1
        if (self.gameBoard[0][4] == 2 and self.gameBoard[1][3] == 2 and
               self.gameBoard[2][2] == 2 and self.gameBoard[3][1] == 2):
            self.player2Score += 1
        if (self.gameBoard[1][3] == 2 and self.gameBoard[2][2] == 2 and
               self.gameBoard[3][1] == 2 and self.gameBoard[4][0] == 2):
            self.player2Score += 1
        if (self.gameBoard[0][5] == 2 and self.gameBoard[1][4] == 2 and
               self.gameBoard[2][3] == 2 and self.gameBoard[3][2] == 2):
            self.player2Score += 1
        if (self.gameBoard[1][4] == 2 and self.gameBoard[2][3] == 2 and
               self.gameBoard[3][2] == 2 and self.gameBoard[4][1] == 2):
            self.player2Score += 1
        if (self.gameBoard[2][3] == 2 and self.gameBoard[3][2] == 2 and
               self.gameBoard[4][1] == 2 and self.gameBoard[5][0] == 2):
            self.player2Score += 1
        if (self.gameBoard[0][6] == 2 and self.gameBoard[1][5] == 2 and
               self.gameBoard[2][4] == 2 and self.gameBoard[3][3] == 2):
            self.player2Score += 1
        if (self.gameBoard[1][5] == 2 and self.gameBoard[2][4] == 2 and
               self.gameBoard[3][3] == 2 and self.gameBoard[4][2] == 2):
            self.player2Score += 1
        if (self.gameBoard[2][4] == 2 and self.gameBoard[3][3] == 2 and
               self.gameBoard[4][2] == 2 and self.gameBoard[5][1] == 2):
            self.player2Score += 1
        if (self.gameBoard[1][6] == 2 and self.gameBoard[2][5] == 2 and
               self.gameBoard[3][4] == 2 and self.gameBoard[4][3] == 2):
            self.player2Score += 1
        if (self.gameBoard[2][5] == 2 and self.gameBoard[3][4] == 2 and
               self.gameBoard[4][3] == 2 and self.gameBoard[5][2] == 2):
            self.player2Score += 1
        if (self.gameBoard[2][6] == 2 and self.gameBoard[3][5] == 2 and
               self.gameBoard[4][4] == 2 and self.gameBoard[5][3] == 2):
            self.player2Score += 1

    def childNodes(self, depth, value):
        if depth >= 0 and self.pieceCount < 42:
            self.subpart = []
            for gameColumn in range(0, 7):

                if not self.gameBoard[0][gameColumn]:

                    c = maxConnect4Game()
                    c.gameBoard = copy.deepcopy(self.gameBoard)
                    if self.currentMove == 1:
                        childMove = 2
                    elif self.currentMove == 2:
                        childMove = 1
                    c.evaluation = 0
                    c.pieceCount = self.pieceCount + 1

                    if value == self.currentMove:
                        self.eval(value)
                        c.evaluation = self.bestMove["moveOver"]
                        c.gameBoard[self.bestMove["row"]][self.bestMove["column"]] = self.currentMove
                        c.column = self.bestMove["column"]
                        self.subpart.append(c)
                        break
                    else:
                        for i in range(5, -1, -1):
                            if not c.gameBoard[i][gameColumn]:
                                c.gameBoard[i][gameColumn] = self.currentMove
                                c.column = gameColumn
                                self.subpart.append(c)
                                break

            for c in self.subpart:
                c.childNodes(depth - 1, value)       
        else: 

            self()

            if value == 1:
                self.moveOver = self.player1Score - self.player2Score + self.evaluation
            else:
                self.moveOver = self.player2Score - self.player1Score + self.evaluation
    
    def MinMax(self, value):
        if self.moveOver is not None:
            return self.moveOver
        elif self.currentMove == value:
            v = -999
            for c in self.subpart:
                v = max(v, c.MinMax(value))
        else:
            v = 999
            for c in self.subpart:
                v = min(v, c.MinMax(value))
        self.moveOver = v
        return self.moveOver

    def omega(self, value, ap, bt):
        if self.moveOver is not None:
            return self.moveOver
        elif self.currentMove == value:
            v = -999
            for c in self.subpart:
                v = max(v, c.omega(value, ap, bt))
                if ap >= bt:
                    self.moveOver = v
                    return self.moveOver
                else:
                    ap = max(ap, v)
        else:
            v = 999
            for c in self.subpart:
                v = min(v, c.omega(value, ap, bt))
                if bt <= ap:
                    self.moveOver = v
                    return self.moveOver
                else:
                    bt = min(v, bt)
        self.moveOver = v
        return self.moveOver

    def selectBestMove(self, value):
        ap = -999
        bt  = 999

        v = self.omega(value, ap, bt)
        for c in self.subpart:
            if c.moveOver == v:
                return c.column

    def eval(self, value):
        if value == 1:
            opposition = 2
        else:
            opposition = 1

        playMoves = []

        for column in range(0, 7):
            if not self.gameBoard[0][column]:
                for row in range(5, -1, -1):
                    if not self.gameBoard[row][column]:
                        playMoves.append({
                            "row": row,
                            "column": column
                        })
                        break
        
        if len(playMoves) > 0:
       
            self.loose = -1
            self.win = -1
            self.probMax = -1
            self.looseBestMove = None
            self.winBestMove = None
            self.probMove = None
            self.randomMove = playMoves[random.randrange(0, len(playMoves))] 
            for move in playMoves:
                looseCount = 0
                winCount = 0
                probCount = 0

                if move["column"] - 3 < 0:
                    column_min = 0
                else:
                    column_min = move["column"] - 3

                if move["column"] + 3 > 6:
                    column_max = 6
                else:
                    column_max = move["column"] + 3

                current_row = self.gameBoard[move["row"]][:]
                current_row[move["column"]] = opposition
                for i in range(column_min, column_max - 2, 1):
                    if current_row[i:i+4] == [opposition]*4:
                        looseCount += 1
                
                current_row[move["column"]] = value
                for i in range(column_min, column_max - 2, 1):
                    if current_row[i:i+4] == [value]*4:
                        winCount += 1
                    try:
                        if current_row[i:i+4].index(opposition) >= 0:
                            pass
                    except:
                        probCount += 1
                
                if move["row"] + 3 <= 5:
                    if self.gameBoard[move["row"] + 3][move["column"]] == opposition and self.gameBoard[move["row"] + 2][move["column"]] == opposition and self.gameBoard[move["row"] + 1][move["column"]] == opposition:
                        looseCount += 1

                    if self.gameBoard[move["row"] + 3][move["column"]] == value and self.gameBoard[move["row"] + 2][move["column"]] == value and self.gameBoard[move["row"] + 1][move["column"]] == value:
                        winCount += 1

                    probArray = []
                    probArray.append(self.gameBoard[move["row"] + 3][move["column"]])
                    probArray.append(self.gameBoard[move["row"] + 2][move["column"]])
                    probArray.append(self.gameBoard[move["row"] + 1][move["column"]])
                    try:
                        if probArray.index(opposition) >= 0:
                            pass
                    except:
                        probCount += 1
                        
                a_start = move["row"]
                b_start = move["column"]
                i = -3
                while i != 0 and a_start != 0 and b_start != 0:
                    a_start = a_start - 1
                    b_start = b_start - 1
                    i = i - 1

                r_end = move["row"]
                c_end = move["column"]
                i = 3
                while i != 0 and r_end != 5 and c_end != 6:
                    r_end = r_end + 1
                    c_end = c_end + 1
                    i = i - 1
                
                a_start_save = a_start
                r_end_save = r_end
                b_start_save = b_start
                c_end_save = c_end

                current_map = copy.deepcopy(self.gameBoard)
                current_map[move["row"]][move["column"]] = value
                while a_start <= r_end - 3:
                    if current_map[a_start][b_start] == value and current_map[a_start+1][b_start+1] == value and current_map[a_start+2][b_start+2] == value and current_map[a_start+3][b_start+3] == value:
                        winCount += 1 

                    probArray = []
                    probArray.append(current_map[a_start][b_start])
                    probArray.append(current_map[a_start+1][b_start+1])
                    probArray.append(current_map[a_start+2][b_start+2])
                    probArray.append(current_map[a_start+3][b_start+3])

                    a_start = a_start + 1
                    b_start = b_start + 1

                    try:
                        if probArray.index(opposition) >= 0:
                            pass
                    except:
                        probCount += 1
                
                a_start = a_start_save
                r_end = r_end_save
                b_start = b_start_save
                c_end = c_end_save

                current_map = copy.deepcopy(self.gameBoard)
                current_map[move["row"]][move["column"]] = opposition
                while a_start <= r_end - 3:
                    if current_map[a_start][b_start] == opposition and current_map[a_start+1][b_start+1] == opposition and current_map[a_start+2][b_start+2] == opposition and current_map[a_start+3][b_start+3] == opposition:
                        looseCount += 1 
                    a_start = a_start + 1
                    b_start = b_start + 1

                a_start = move["row"]
                b_start = move["column"]
                i = -3
                while i != 0 and a_start != 0 and b_start != 6:
                    a_start = a_start - 1
                    b_start = b_start + 1
                    i = i - 1

                r_end = move["row"]
                c_end = move["column"]
                i = 3
                while i != 0 and r_end != 5 and c_end != 0:
                    r_end = r_end + 1
                    c_end = c_end - 1
                    i = i - 1
                
                a_start_save = a_start
                r_end_save = r_end
                b_start_save = b_start
                c_end_save = c_end
                
                current_map = copy.deepcopy(self.gameBoard)
                current_map[move["row"]][move["column"]] = value
                while a_start <= r_end - 3:
                    if current_map[a_start][b_start] == value and current_map[a_start+1][b_start-1] == value and current_map[a_start+2][b_start-2] == value and current_map[a_start+3][b_start-3] == value:
                        winCount += 1 

                    probArray = []
                    probArray.append(current_map[a_start][b_start])
                    probArray.append(current_map[a_start+1][b_start-1])
                    probArray.append(current_map[a_start+2][b_start-2])
                    probArray.append(current_map[a_start+3][b_start-3])

                    a_start = a_start + 1
                    b_start = b_start - 1

                    try:
                        if probArray.index(opposition) >= 0:
                            pass
                    except:
                        probCount += 1
                
                a_start = a_start_save
                r_end = r_end_save
                b_start = b_start_save
                c_end = c_end_save
                
                current_map = copy.deepcopy(self.gameBoard)
                current_map[move["row"]][move["column"]] = opposition
                while a_start <= r_end - 3:
                    if current_map[a_start][b_start] == opposition and current_map[a_start+1][b_start-1] == opposition and current_map[a_start+2][b_start-2] == opposition and current_map[a_start+3][b_start-3] == opposition:
                        looseCount += 1 
                    a_start = a_start + 1
                    b_start = b_start - 1

                if looseCount != 0 and looseCount > self.loose:
                    self.loose = looseCount
                    self.looseBestMove = move

                if winCount != 0 and winCount > self.win:
                    self.win = winCount
                    self.winBestMove = move

                if probCount != 0 and probCount > self.probMax:
                    self.probMax = probCount
                    self.probMove = move


            if self.win >= self.loose and self.win != -1:
                self.bestMove = {
                    "row" : self.winBestMove["row"],
                    "column" : self.winBestMove["column"],
                    "moveOver" : self.win * 4
                }
            elif self.win < self.loose:
                self.bestMove = {
                    "row" : self.looseBestMove["row"],
                    "column" : self.looseBestMove["column"],
                    "moveOver" : self.loose * 4
                }
            elif self.probMax > 0:
                self.bestMove = {
                    "row" : self.probMove["row"],
                    "column" : self.probMove["column"],
                    "moveOver" : self.probMax
                }
            else:
                self.bestMove = {
                    "row" : self.randomMove["row"],
                    "column" : self.randomMove["column"],
                    "moveOver" : 0
                }
        else:
            self.bestMove = None
