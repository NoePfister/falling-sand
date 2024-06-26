import pygame as pg
import utils
from enums import Types, Colors
from cell import Cell
import random
import os


class Game:
    def __init__(self,screen_dimensions,cell_dimensions, fps):
        self.screen_width = screen_dimensions[0]
        self.screen_height = screen_dimensions[1]

        self.cell_width = self.screen_width/cell_dimensions[0]
        self.cell_height = self.screen_height/cell_dimensions[1]

        self.cell_count_width = cell_dimensions[0]
        self.cell_count_height = cell_dimensions[1]

        self.fps = fps
        self.clock = pg.time.Clock()

        self.color = Colors.DEFAULT

        self.cells = [[Cell() for x in range(self.cell_count_width)]for y in range(self.cell_count_height)]
        # print(self.cells)

        self.setup()
        self.loop()


    def setup(self):
        pg.init()
        self.screen = pg.display.set_mode((self.screen_height,self.screen_width))
        pg.display.set_caption("Falling Sand")
        

    def loop(self):
        while True:


            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.quit()
                # if event.type == pg.MOUSEBUTTONDOWN:
                #     self.spawn_at_mouse()

            if pg.mouse.get_pressed()[0]:
                self.spawn_at_mouse()
            # self.wait_for_n()

            # os.system("cls")

            keys = pg.key.get_pressed()

            if keys[pg.K_ESCAPE]: self.quit()
            if keys[pg.K_r]: self.cells = [[Cell() for x in range(self.cell_count_width)]for y in range(self.cell_count_height)]
            if keys[pg.K_1]: self.color = Colors.RED
            if keys[pg.K_2]: self.color = Colors.ORANGE
            if keys[pg.K_3]: self.color = Colors.YELLOW
            if keys[pg.K_4]: self.color = Colors.GREEN
            if keys[pg.K_5]: self.color = Colors.BLUE
            if keys[pg.K_6]: self.color = Colors.PINK
            if keys[pg.K_7]: self.color = Colors.DEFAULT

            self.update_sand()
            self.draw_sand()
            # self.draw_grid()

            pg.display.update()

            self.clock.tick(self.fps)

    def wait_for_n(self):
        waiting = True
        while waiting:
            for event in pg.event.get():
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_n:
                        waiting = False
                    if event.key == pg.K_ESCAPE:
                        self.quit()
                if event.type == pg.MOUSEBUTTONDOWN:
                    self.spawn_at_mouse()

    def draw_grid(self):
        for x in range(self.cell_count_width):
            pg.draw.rect(self.screen,self.color,(x*self.cell_width,0,self.screen_width/300,self.screen_height))


        for y in range(self.cell_count_height):
            pg.draw.rect(self.screen,self.color,(0,y*self.cell_height,self.screen_width,self.screen_height/300))

    def draw_sand(self):
        for x in range(self.cell_count_width):
            for y in range(self.cell_count_height):
                # print(self.cells[x][y])
                # print(x,y)
                color = self.cells[x][y].color.value
                if self.cells[x][y].type == Types.CELL:
                    pg.draw.rect(self.screen,color,(x*self.cell_width,y*self.cell_height,self.cell_width,self.cell_height))
                else:
                    pg.draw.rect(self.screen,(0,0,0),(x*self.cell_width,y*self.cell_height,self.cell_width,self.cell_height))

    def update_sand(self):
        cells_new = [[Cell() for x in range(self.cell_count_width)]for y in range(self.cell_count_height)]

        for x in range(self.cell_count_width):
            for y in range(self.cell_count_height):
                color = self.cells[x][y].color
                # continue if cell is 0
                if self.cells[x][y].type == Types.EMPTY_CELL:
                    # print("0")
                    continue
                # continue if cell is at floor
                if y == self.cell_count_height-1:
                    cells_new[x][y] = Cell(color,Types.CELL)
                    # print("floor")
                    continue
                # check if celll under the cell is free
                if self.cells[x][y+1].type == Types.EMPTY_CELL:
                    cells_new[x][y+1] = Cell(color,Types.CELL) 
                    # print("Free")
                    # print(x,y)
                else:
                    # Check if it can go right or left

                    # If cell is at the edge, force it in one direction
                    if x == 0 and self.cells[x+1][y+1].type == Types.EMPTY_CELL:
                        cells_new[x+1][y+1] = Cell(color,Types.CELL)
                        continue
                    elif x == self.cell_count_width-1 and self.cells[x-1][y+1].type == Types.EMPTY_CELL:
                        cells_new[x-1][y+1] = Cell(color,Types.CELL)
                        continue
                    elif x == 0 or x == self.cell_count_width-1:
                        cells_new[x][y] = Cell(color,Types.CELL)
                        continue

                    a = random.randint(1,2)
                    if a == 2: a = -1
                    # Right:
                    if self.cells[x+a][y+1].type == Types.EMPTY_CELL:
                        cells_new[x+a][y+1] =Cell(color,Types.CELL)
                        continue
                    # Left
                    if self.cells[x+a][y+1].type == Types.EMPTY_CELL:
                        cells_new[x+a][y+1] = Cell(color,Types.CELL)
                        continue
                    # Else leave the cell
                    cells_new[x][y] = Cell(color,Types.CELL)

                    # print(cells_new)
        self.cells = cells_new
                    
    def spawn_at_mouse(self):
        pos = pg.mouse.get_pos()

        cell_pos = [0,0]

        cell_pos[0] = utils.clamp(int(pos[0]//self.cell_width),0,self.cell_count_width-1)
        cell_pos[1] = utils.clamp(int(pos[1]//self.cell_height),0,self.cell_count_height-1)
        # print(cell_pos)

        # Check if there is already a cell there
        if self.cells[cell_pos[0]][cell_pos[1]].type != Types.EMPTY_CELL: return

        self.cells[cell_pos[0]][cell_pos[1]] = Cell(self.color,Types.CELL)

    def quit(self):
        exit(0)


