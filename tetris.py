from settings import *
from tetromino import Tetromino
import math


class Tetris:
    def __init__(self,app):
        self.app = app
        self.sprite_group = pg.sprite.Group()
        self.tetromino = Tetromino(self)
    
    def check_tetromino_landing(self):
        if self.tetromino.landing:
            self.tetromino = Tetromino(self)

    def control(self,pressed_key):
        if pressed_key == pg.K_LEFT:
            self.tetromino.move(direction="right")
        elif pressed_key == pg.K_RIGHT:
            self.tetromino.move(direction="left")

    def draw_grid(self):
        for i in range(FIELD_W):
            for j in range(FIELD_H):
                pg.draw.rect(self.app.screen,"black",(i*TILE_SIZE,j*TILE_SIZE,TILE_SIZE,TILE_SIZE),1)

    def update(self):
        if self.app.anim_trigger:
            self.tetromino.update()
            self.check_tetromino_landing()
        self.sprite_group.update()

    def draw(self):
        self.draw_grid()
        self.sprite_group.draw(self.app.screen)