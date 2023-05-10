from settings import *
from tetromino import Tetromino
import math


class Tetris:
    def __init__(self,app):
        self.app = app
        self.sprite_group = pg.sprite.Group()
        self.tetromino = Tetromino(self)

    def draw_grid(self):
        for i in range(FIELD_W):
            for j in range(FIELD_H):
                pg.draw.rect(self.app.screen,"black",(i*TILE_SIZE,j*TILE_SIZE,TILE_SIZE,TILE_SIZE),1)
    def update(self):
        self.tetromino.update()
        self.sprite_group.update()
    def draw(self):
        self.draw_grid()
        self.sprite_group.draw(self.app.screen)