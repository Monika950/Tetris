from settings import *
import pygame

class Block(pygame.sprite.Sprite):
    def __init__(self,tetromino,pos):
        self.tetromino = tetromino
        
         
class Tetromino:
    def __init__(self,tetris):
        self.tetris=tetris
    
    def update(self):
        pass