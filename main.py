import pygame as pg
from game import Game

def start():
    # anything more than 100 x 100 cells is really slow
    game = Game([1000,1000],[100,100],100)


if __name__ == "__main__":
    start()
