import pygame as pg

vec = pg.math.Vector2

FPS = 60
FIELD_COLOR = (48, 39, 32)
BG_COLOR = (24,79,115)

SPR_DIR='assets/sprites'

COLORS = ['orange', 'pink','green','purple','red','blue','yellow','brown']

ANIM_TIME_INTERVAL =250
FAST_ANIM_TIME_INTERVAL =15

TILE_SIZE = 40
FIELD_SIZE = FIELD_W, FIELD_H = 10, 20
FIELD_RES = FIELD_W * TILE_SIZE, FIELD_H * TILE_SIZE

FIELD_SCALE_W, FIELD_SCALE_H =1.7,1.0
WIN_RES = WIN_W, WIN_H = FIELD_RES[0] *FIELD_SCALE_W, FIELD_RES[1] *FIELD_SCALE_H

INIT_POS_OFFSET =vec(FIELD_W//2-1,0)
NEXT_POS_OFFSET =vec(FIELD_W *1.3,FIELD_H*0.45)
MOVE_DIRECTIONS ={ 'left':(-1,0), 'right':(1,0),'down':(0,1)}

TETROMINOS = {
    'T': [(0,0),(-1,0),(1,0),(0,-1)],
    'O': [(0,0),(0,-1),(1,0),(1,-1)],
    'J': [(0,0),(-1,0),(0,-1),(0,-2)],
    'L': [(0,0),(1,0),(0,-1),(0,-2)],
    'I': [(0,0),(0,1),(0,-1),(0,-2)],
    'S': [(0,0),(-1,0),(0,-1),(1,-1)],
    'Z': [(0,0),(1,0),(0,-1),(-1,-1)]
}
