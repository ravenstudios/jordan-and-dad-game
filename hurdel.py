from constants import *
import pygame

class Hurdel:

    def __init__(self):
        self.width = BLOCK_SIZE // 2
        self.height = BLOCK_SIZE * 1.5
        self.x = GAME_WIDTH
        self.y = GAME_HEIGHT - self.height
        self.speed = -5


    def update(self):
        if self.x + self.width  < 0:
            self.x = GAME_WIDTH
        self.x += self.speed


    def draw(self, surface):
        pygame.draw.rect(surface, RED, (self.x, self.y, self.width, self.height))
