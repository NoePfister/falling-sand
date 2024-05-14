import pygame as pg


class Game:
    def __init__(self,screen_dimensions,cell_dimensions):
        self.screen_width = screen_dimensions[0]
        self.screen_height = screen_dimensions[1]

        self.cell_width = self.screen_width/cell_dimensions[0]
        self.cell_height = self.screen_height/cell_dimensions[1]

        self.cell_count_width = cell_dimensions[0]
        self.cell_count_height = cell_dimensions[1]

        self.cells = [[0 for x in range(self.cell_count_width)]for y in range(self.cell_count_height)]
        self.cells[7][10] = 1

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

            keys = pg.key.get_pressed()

            if keys[pg.K_ESCAPE]: self.quit()

            self.update_sand()
            self.draw_sand()
            self.draw_grid()

            pg.display.update()

    def draw_grid(self):
        for x in range(self.cell_count_width):
            pg.draw.rect(self.screen,(222,222,222),(x*self.cell_width,0,self.screen_width/300,self.screen_height))


        for y in range(self.cell_count_height):
            pg.draw.rect(self.screen,(222,222,222),(0,y*self.cell_height,self.screen_width,self.screen_height/300))

    def draw_sand(self):
        for x in range(self.cell_count_width):
            for y in range(self.cell_count_height):
                # print(self.cells[x][y])
                if self.cells[x][y]:
                    pg.draw.rect(self.screen,(111,111,111),(x*self.cell_width,y*self.cell_height,self.cell_width,self.cell_height))
                else:
                    pg.draw.rect(self.screen,(0,0,0),(x*self.cell_width,y*self.cell_height,self.cell_width,self.cell_height))

    def update_sand(self):
        cells_new = [[0 for x in range(self.cell_count_width)]for y in range(self.cell_count_height)]

        for x in range(self.cell_count_width):
            for y in range(self.cell_count_height):
                # continue if cell is 0
                if not self.cells[x][y]: continue
                # continue if cell is at floor
                if y == self.cell_count_height-1: continue
                if not self.cells[x][y+1]:
                    cells_new[x][y+1] = 1 
                    print(x,y)

        self.cells = cells_new
                    

    def quit(self):
        exit(0)


