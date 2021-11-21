from pygame import Color, Rect
import pygame
from pygame.draw import rect


class Dino:
    xPosition = 30
    yPosition = 250
    dinoSprite = Rect(xPosition,yPosition - 40,20,40)
    color_red = Color(255,0,0)

    def __init__(self):
        pass

    def update(self):
        pass

    def draw(self, screen):
        pygame.draw.rect(screen, self.color_red, self.dinoSprite)