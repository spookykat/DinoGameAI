from pygame import Color, Rect
import pygame
from pygame.draw import rect


class Dino:

    def __init__(self):
        self.xPosition = 30
        self.yPosition = 250
        self.color_red = Color(255,0,0)
        self.isJump = False
        self.jumpcount = 10

    def jump(self):
        if self.isJump:
            if self.jumpcount >= -10:
                neg = 1
                if self.jumpcount > 0:
                    neg = -1
                self.yPosition += self.jumpcount**2 * 0.1 * neg
                self.jumpcount -= 1
            else:
                self.isJump = False
                self.jumpcount = 10

    def update(self,screen):
        self.jump()
        self.draw(screen)    

    def draw(self, screen):
        self.dinoSprite = Rect(self.xPosition,self.yPosition - 40,20,40)
        pygame.draw.rect(screen, self.color_red, self.dinoSprite)