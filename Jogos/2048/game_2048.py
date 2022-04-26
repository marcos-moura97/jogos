import pygame, sys, time, random
from pygame.locals import *

class Game2048:
    def __init__(self):

        pygame.init()
        self.window = pygame.display.set_mode((450, 550))
        pygame.display.set_caption("2048")

        #Setting color & font
        self.WHITE = (255,255,255)
        self.GREEN = (77,204,0)
        self.RED = (255,0,0)
        self.BLUE = (0,0,255)
        self.myfont = pygame.font.SysFont(None, 50)


    #initialize board
    def init_board(self):
        board = []
        for i in range(4):
            board += [["0"] * 4]

        # Init with two numbers.
        self.addNewNum(board, 2)

        #debugging code

        """
        board[0][0] = "0"
        board[0][1] = "0"
        board[0][2] = "8"
        board[0][3] = "0"
        board[1][0] = "0"
        board[1][1] = "8"
        board[1][2] = "0"
        board[1][3] = "64" 
        board[2][0] = "0"   
        board[2][1] = "2"
        board[2][2] = "32"
        board[2][3] = "256"
        board[3][0] = "0"
        board[3][1] = "16"  
        board[3][2] = "1024"
        board[3][3] = "1024"   
        """

        return board


    def addNewNum(self, board, n):

        """Generates a 2 or 4, and set the number at a random location on board \
        that is originally a 0.
        """

        for i in range(n):
            newNum = str(random.choice([2,4]))
            randomx = random.randrange(4)
            randomy = random.randrange(4)
            while board[randomy][randomx] != "0":
                randomx = random.randrange(4)
                randomy = random.randrange(4)
            board[randomy][randomx] = newNum


    def checkWin(self, board):

        """ Checks if the player has the number 2048 on the board.
        If so, return True. Otherwise, return False.
        """

        win = False
        for line in board:
            for num in line:
                if num == "2048":
                    win = True
        return win


    def add(self, board, i_list, j_list, i_direction, j_direction):

        """Iterates through the board, and adds a number with its adjacent neighbor if the two numbers are the same.
        ex. 2248 becomes 0448.
        i_list, j_list - lists, indicate how add interate through the list.
        i_direction, j_direction - an int, either 1, -1 or 0. Defines the direction of the add.
        ex. +1, 2248 becomes 0448. -1, 2248 becomes 4480, 0, does not add.

        move is a counter that's later used to determine whether a move can still be made by the player.
        """

        move = 0
        for i in i_list:
            for j in j_list:

            #check if 2 numbers are the same, if yes, add them together
                if board[i][j] == board[i + i_direction][j + j_direction]:
                    board[i+ i_direction][j + j_direction] = str(int(board[i][j])+int(board[i+ i_direction][j+j_direction]))
                    if board[i][j] != 0:
                        move += 1
                    board[i][j] = "0"
        return move


    def push(self, board, i_list, j_list, i_direction, j_direction):

        """Push a number to its adjacent slot if the slot is 0.
        i_list, j_list - lists, indicate how push interate through the list.
        i_direction, j_direction - an int, either 1, -1 or 0. Defines the direction of the push.
        move is a counter that's later used to determine whether a move can still be made by the player.
        """

        move = 0
        for i in i_list:
            for j in j_list:
                if board[i + i_direction][j + j_direction] == "0":
                    board[i + i_direction][j + j_direction] = board[i][j]
                    if board[i][j] != 0:
                        move += 1
                    board[i][j] = "0"
        return move


    def pushDirection(self, board, UserInput):
        """Takes in a UserInput and calls add and push function with the proper i_list,\
        j_list, i_direction and j_direction.
        UserInput - a str
        """

        move = 0
        if UserInput == "u":
            i_list, j_list = range(1,4), range(4)
            i_direction, j_direction = -1, 0
        elif UserInput == "d":
            i_list, j_list = range(2,-1,-1), range(4)
            i_direction, j_direction = 1, 0
        elif UserInput == "l":
            i_list, j_list = range(4), range(1,4)
            i_direction, j_direction = 0, -1
        elif UserInput == "r":
            i_list, j_list = range(4), range(2,-1,-1)
            i_direction, j_direction = 0, 1

        for i in range(4):
            move += self.push(board, i_list, j_list, i_direction, j_direction)
        move += self.add(board, i_list, j_list, i_direction, j_direction)
        for i in range(4):
            move += self.push(board, i_list, j_list, i_direction, j_direction)

        return move


    def checkCell(self, board, i, j):
        """Checks the cell above/ below/ to the left/ to the right
        of board[i][j] and see if one or more equals to board[i][j]
        if so, return True.
        else, return False.
        """

        move_i = []
        move_j = []
        board_size = len(board)
        if i > 0:
            move_i.append(-1)
            move_j.append(0)
        if i < (board_size - 1):
            move_i.append(1)
            move_j.append(0)
        if j > 0:
            move_j.append(-1)
            move_i.append(0)
        if j < (board_size - 1):
            move_j.append(1)
            move_i.append(0)
        for k in range(len(move_i)):
            if board[i + move_i[k]][j + move_j[k]] == board[i][j]:
                return True
        return False


    def canMove(self, board):
        """Checks if the player can still can still make a move.
        If so, return True. Else, return False.
        """

        board_size = len(board)
        for i in range(board_size):
            for j in range(board_size):
                if board[i][j] == 0:
                    return True
                if self.checkCell(board, i, j):
                    return True
        return False

    def checkLose(self, board):

        """Takes in a list (board), return True the player does not lose
        (if there is still 0 in the list or \ if any move can still be made)
        otherwise False
        """

        nozero = False

        for elt in board:
            nozero = nozero or ("0" in elt)

        if not nozero:
            return not self.canMove(board)
        return False


    def main(self, board, UserInput):

        if not self.checkLose(board) and not self.checkWin(board):

            move = self.pushDirection(board, UserInput)
            if move != 0:
                self.addNewNum(board, 1)
        return board

    #######################################################
    #######################################################
    #######################################################
    #######################################################


    def buildText(self, board,i,j):

        if board[j][i] == "0":
            text = self.myfont.render(" ", True, self.BLUE)
        else:
            text = self.myfont.render(board[j][i], True, self.BLUE)
        textRect = text.get_rect()
        textRect.centerx = i*100 + 75
        textRect.centery = j*100 + 180
        return text, textRect


    def showText(self, board):
        """Display numbers on screen"""

        for i in range(4):
            for j in range(4):
                self.window.blit(self.buildText(board, i, j)[0], self.buildText(board, i, j)[1])

    def quitWindow(self, event, QUIT=None):
        if event.type == QUIT:
            pygame.quit()
            sys.exit()


    def gameOver(self):

        label = self.myfont.render("GAME OVER", True, self.RED)
        labelRect = label.get_rect()
        labelRect.centerx = self.window.get_rect().centerx
        labelRect.centery = self.window.get_rect().centery
        self.window.blit(label, labelRect)
        event = pygame.event.wait()
        self.quitWindow(event)


    def win(self):
        self.window.fill(self.WHITE)
        label = self.myfont.render("You WIN !!!!!", True, self.RED)
        labelRect = label.get_rect()
        labelRect.centerx = self.window.get_rect().centerx
        labelRect.centery = self.window.get_rect().centery
        self.window.blit(label, labelRect)
        event = pygame.event.wait()
        self.quitWindow(event)


    def gameLoop(self):

        #Initialize a game board with 16 blocks to store number
        board = self.init_board()
        blocks = []
        for i in range(4):
            for j in range(4):
                blocks.append([pygame.Rect((i*100) + 30 , (j*100) + 135, 90, 90), self.WHITE])

        while True:
            for event in pygame.event.get():

                self.quitWindow(event)
                if event.type == KEYDOWN:
                    if event.key == K_UP:
                        board = self.main(board, "u")
                    if event.key == K_DOWN:
                        board = self.main(board, "d")
                    if event.key == K_LEFT:
                        board = self.main(board, "l")
                    if event.key == K_RIGHT:
                        board = self.main(board, "r")


            self.window.fill(self.WHITE)
            header = self.myfont.render("2048", True, self.BLUE)
            self.window.blit(header, (30, 50))
            pygame.draw.rect(self.window, self.GREEN, pygame.Rect(20, 125, 410, 410))

            for block in blocks:
                pygame.draw.rect(self.window, block[1], block[0])
            self.showText(board)

            if self.checkLose(board):
                self.gameOver()
            elif self.checkWin(board):
                self.win()

            pygame.display.update()

            time.sleep(0.02)


game = Game2048()
game.gameLoop()
