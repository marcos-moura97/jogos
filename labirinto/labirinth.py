from tkinter import *
from tkinter import messagebox

from random import randint


## Estrutura

class Labirinth:

    def __init__(self):
        self.start_game()

    def start_game(self):
        self.cell_size = 12
        self.lc = 20

        self.checked_cells = []
        self.walls = []
        self.rechecked_cells = []

        self.map = [['w' for _ in range(self.lc)] for _ in range(self.lc)]

        ccr, ccc = randint(1,self.lc), randint(1,self.lc)

        self.create_initial_point(ccr, ccc)
        self.create_tk_structure()
        self.create()
        self.draw_initial_point(ccr, ccc)

        for i in range(1):
            try:
                self.create_end_point()
            except:
                pass

    def create_tk_structure(self):
        self.app = Tk()
        self.app.title("Labirinth Game")

        self.ffs = Canvas(self.app, width = self.lc*self.cell_size, height=self.lc*self.cell_size, bg='grey')
        self.ffs.pack()

    def create(self):
        for row in range(self.lc):
            for column in range(self.lc):
                if self.map[row][column] == 'P':
                    cor = 'grey'
                elif self.map[row][column] == 'w':
                    cor = 'black'
                self.draw_cell(row,column,cor)


    def draw_cell(self, row,column,cor):
        x1 = column*self.cell_size
        y1 = row*self.cell_size

        x2 = x1+self.cell_size
        y2 = y1+self.cell_size
        self.ffs.create_rectangle(x1,y1,x2,y2, fill=cor)

    def check_neighbours(self, ccr,ccc):
        neighbours = [[
             ccr,
             ccc - 1,
             ccr - 1,
             ccc - 2,
             ccr,
             ccc - 2,
             ccr + 1,
             ccc - 2,
             ccr - 1,
             ccc - 1,
             ccr + 1,
             ccc - 1
             ],

            # left
             [ccr, ccc + 1, ccr - 1, ccc + 2, ccr, ccc + 2, ccr + 1, ccc + 2, ccr - 1, ccc + 1, ccr + 1, ccc + 1], #right
             [ccr - 1, ccc, ccr - 2, ccc - 1, ccr - 2, ccc, ccr - 2, ccc + 1, ccr - 1, ccc - 1, ccr - 1, ccc + 1], #top
             [ccr + 1, ccc, ccr + 2, ccc - 1, ccr + 2, ccc, ccr + 2, ccc + 1, ccr + 1, ccc-1, ccr + 1, ccc + 1]] #bottom


        self.available_neighbours = []

        for i in neighbours:
            if i[0]>0 and i[0]<(self.lc-1) and i[1] >0 and i[1]<(self.lc-1):
                if self.map[i[2]][i[3]] == 'P' or self.map[i[4]][i[5]] == 'P' or self.map[i[6]][i[7]] == 'P' or self.map[i[8]][i[9]] == 'P' or self.map[i[10]][i[11]] == 'P':
                    self.walls.append(i[0:2])

                else:
                    self.available_neighbours.append(i[0:2])

        return self.available_neighbours

    def create_initial_point(self, ccr, ccc):
        self.map[ccr][ccc] = 'P'

        self.populate_map(ccr, ccc)

        self.y1 = ccr*self.cell_size
        self.x1 = ccc*self.cell_size

    def draw_initial_point(self, ccr, ccc):
        initial_color = 'Green'
        self.draw_cell(ccr,ccc,initial_color)

    def create_end_point(self):
        final_color = 'Red'

        e = randint(1,len(self.rechecked_cells))-1

        ecr = self.rechecked_cells[e][0]
        ecc = self.rechecked_cells[e][1]

        self.yf = ecr*self.cell_size
        self.xf = ecc*self.cell_size

        self.draw_cell(ecr,ecc,final_color)

    def draw_rect(self):
        self.ffs.create_rectangle((self.x1,self.y1,self.x1+12,self.y1+12), fill="green")

    def del_rect(self):
        self.ffs.create_rectangle((self.x1,self.y1,self.x1+12,self.y1+12), fill="white")

    def move(self, event):

        self.del_rect()

        col = self.x1//self.cell_size
        row = self.y1//self.cell_size

        if event.char == "a":
            if self.map[row][col-1] == "P":
                self.x1-=self.cell_size
            else:
                pass

        elif event.char == "d":
            if self.map[row][col+1] == "P":
                self.x1+=self.cell_size
            else:
                pass

        elif event.char == "w":
            if self.map[row-1][col] == "P":
                self.y1-=self.cell_size
            else:
                pass

        elif event.char == "s":
            if self.map[row+1][col] == "P":
                self.y1+=self.cell_size
            else:
                pass

        self.draw_rect()
        self.check_win()

    def populate_map(self, ccr, ccc):
        while 1:
            self.available_neighbours = self.check_neighbours(ccr,ccc)

            if len(self.available_neighbours) != 0:
                d = randint(1, len(self.available_neighbours))-1
                ncr, ncc = self.available_neighbours[d]
                self.map[ncr][ncc] = 'P'
                self.checked_cells.append([ncr,ncc])
                ccr, ccc = ncr, ncc
            if len(self.available_neighbours) == 0:
                try:
                    ccr,ccc = self.checked_cells.pop()
                    self.rechecked_cells.append([ccr,ccc])

                except:
                    break

    def check_win(self):
        if(self.x1==self.xf and self.y1==self.yf):
            messagebox.showinfo(title='Winner!', message='Congratulations, you won the game!')
            self.app.destroy()


game = Labirinth()
game.app.bind("<Key>",game.move)

game.app.mainloop()
