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
        self.dinoSprite = Rect(self.xPosition,self.yPosition - 40,20,40)
        self.isDuck = False
        self.inAir = False
        
    def jump(self):
        if self.isJump:
            if self.jumpcount >= -10:
                self.inAir = True
                neg = 1
                if self.jumpcount > 0:
                    neg = -1
                self.yPosition += self.jumpcount ** 2 * 0.2 * neg
                self.jumpcount -= 1
            else:
                self.isJump = False
                self.inAir = False
                self.jumpcount = 10
    
    def duck(self):
        if self.isDuck:
            self.dinoSprite = Rect(self.xPosition,self.yPosition - 20,20,20)
        else:
            self.dinoSprite = Rect(self.xPosition,self.yPosition - 40,20,40)

    def update(self,screen):
        self.duck()
        self.jump()
        self.draw(screen)
            

    def draw(self, screen):
        
        pygame.draw.rect(screen, self.color_red, self.dinoSprite)