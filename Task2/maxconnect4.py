#!/usr/bin/env python
# Name : deepthi chiluka
# UTA ID: 1002028543
#written in python 3 and not compatable for omega

import sys
import time
from MaxConnect4Game import *
#this is to check whether the board is ready
def oneMoveGame(currentGame, depth):
    if currentGame.pieceCount == 42:    
        print ('BOARD FULL\n\nGame Over!\n')
        sys.exit(0)

    if depth == 0:
        print ('please enter a depth value greater than 0')
        sys.exit(0)
#making a move with some depth and considering current game and current turn
    currentGame.aiPlay(depth, currentGame.currentMove) 

    print ('Game state after move:')
    currentGame.printGameBoard()

    currentGame.countScore()
    print('Score: Player 1 = %d, Player 2 = %d\n' % (currentGame.player1Score, currentGame.player2Score))

    if currentGame.currentMove == 1:
        currentGame.currentMove= 2
    elif currentGame.currentMove == 2:
        currentGame.currentMove= 1

    currentGame.printGameBoardToFile()
    currentGame.gameFile.close()


def interactiveGame(currentGame, depth, value):
    if currentGame.pieceCount == 42:    
        currentGame.countScore()
        #if value value is 1 and present score of player 1 is less than player 2 than player 1 wins else its draw
        if value == 1:
            print('Score: value (Player 1) = %d, Human (Player 2) = %d\n' % (currentGame.player1Score, currentGame.player2Score))
            if currentGame.player1Score > currentGame.player2Score:
                print ("You lost the Game")
            elif currentGame.player1Score < currentGame.player2Score:
                print ("You won the Game")
            else:
                print ("Its okay. It is a draw")
                #if its value is zero and present score of player 1 is less than player 2 than player 1 wins
        else:
            print('Score: Human (Player 1) = %d, value (Player 2) = %d\n' % (currentGame.player1Score, currentGame.player2Score))
            if currentGame.player1Score > currentGame.player2Score:
                print ("You lost the Game")
            elif currentGame.player1Score < currentGame.player2Score:
                print ("You won the Game")
            else:
                print ("Its okay. It is a draw")

        print ('BOARD FULL\n\nGame Over!\n')
        sys.exit(0)
#this is case when depth value is zero we cannot find anything
    if depth == 0:
        print ('Please try to enter a depth value greater than  0')
        sys.exit(0)

    if value == currentGame.currentMove:
        outFile = "value.txt"
        currentGame.aiPlay(depth, value)
        currentGame.printGameBoard()
        currentGame.countScore()
        if value != 1:
            print('Score: Human (Player 1) = %d, value (Player 2) = %d\n' % (currentGame.player1Score, currentGame.player2Score))
        else:
            print('Score: value (Player 1) = %d, Human (Player 2) = %d\n' % (currentGame.player1Score, currentGame.player2Score))

    else:
        outFile = "human.txt"
        try: 
            column = int(input("Which column would you like to play: "))
            if type(column) == int:
                if column > 0 and column <= 7:
                    result = currentGame.playPiece(column - 1)
                    if not result:
                        print ("No moves on column "+ str(column) + ". Try Again")
                        interactiveGame(currentGame, depth, value)
                    else:
                        if value != 1:
                            print('Score: Human (Player 1) = %d, value (Player 2) = %d\n' % (currentGame.player1Score, currentGame.player2Score))
                        else:
                            print('Score: value (Player 1) = %d, Human (Player 2) = %d\n' % (currentGame.player1Score, currentGame.player2Score))
                else:
                    print ("Invalid Move. Please Try Again")
                    interactiveGame(currentGame, depth, value)
        except:
            sys.exit('Wrong input given.' + outFile)
    try:
        currentGame.gameFile = open(outFile, 'w')
    except:
        sys.exit('Error in opening output file...')
    
    currentGame.printGameBoardToFile()

    nextGame = maxConnect4Game()
    nextGame.gameBoard = copy.deepcopy(currentGame.gameBoard)
    nextGame.pieceCount = currentGame.pieceCount
    nextGame.rate = 0
    currentGame.gameFile.close()

    if currentGame.currentMove == 1:
        nextGame.currentMove= 2
        currentGame.currentMove= 2
    else:
        nextGame.currentMove= 1
        currentGame.currentMove= 1

    interactiveGame(nextGame, depth, value)

def main(argv):
    
    if len(argv) != 5:
        print ('Four command-line arguments are needed:')
        print('Usage: %s interactive [input_file] [value-next/human-next] [depth]' % argv[0])
        print('or: %s one-move [input_file] [output_file] [depth]' % argv[0])
        sys.exit(2)

    game_mode, inFile = argv[1:3]

    if not game_mode == 'interactive' and not game_mode == 'one-move':
        print('%s is an unrecognized game mode' % game_mode)
        sys.exit(2)

    currentGame = maxConnect4Game() 

    try:
        currentGame.gameFile = open(inFile, 'r')
    except IOError:
        sys.exit("\nError opening input file.\nCheck file name.\n")


    info = currentGame.gameFile.readlines()
    currentGame.gameBoard = [[int(char) for char in line[0:7]] for line in info[0:-1]]
    currentGame.currentMove = int(info[-1][0])
    currentGame.rate = 0
    currentGame.gameFile.close()

    print ('\nMaxConnect-4 game\n')
    print ('staus of Game before any moves:')
    currentGame.printGameBoard()

    currentGame.chec.pieceCount()
    currentGame.countScore()
    print('Score: Player 1 = %d, Player 2 = %d\n' % (currentGame.player1Score, currentGame.player2Score))

    if game_mode == 'interactive':
        if argv[3] == "value-next":
            value = currentGame.currentMove
    
        elif argv[3] == "human-next":
            if currentGame.currentMove== 1:
                value = 2
            else:
                value = 1
        interactiveGame(currentGame, int(argv[4]),value)
    else: 
        outFile = argv[3]
        try:
            currentGame.gameFile = open(outFile, 'w')
        except:
            sys.exit('Error opening output file.')
        oneMoveGame(currentGame, int(argv[4])) 

#to evaluate time taken to execute the programe
if __name__ == '__main__':
    start_time=time.time()
    main(sys.argv)
    end_time=time.time()
    time_taken=end_time-start_time
    print("Execution time in seconds: {}".format(time_taken))
#most of the code is taken from the reference file given by professor