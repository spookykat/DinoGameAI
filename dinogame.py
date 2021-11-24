from operator import countOf
import pygame
import random

from dino import Dino
from obstacles import TallObstacle, SmallObstacle

class dinoGameAI:
    def __init__(self):
        self.width = 700
        self.height = 300

        self.backgroundcolor = (255, 255, 255)
        self.background = pygame.Surface((self.width,self.height))
        self.background.fill((self.backgroundcolor))

        self.dino = Dino()
        self.clock = pygame.time.Clock()
        self.reset()
        

        self.screen = pygame.display.set_mode((self.width, self.height))

        pygame.draw.line(self.background, pygame.Color(0,0,0), (0, 250), (700,250))

    def reset(self):
        self.gamespeed = 10
        self.score = 0
        self.obstacles = []
        self.frameiteration = 0
        self.collided = False

    def placeObstacle(self):
        if len(self.obstacles) == 0:
          x = random.randint(10, 900)
          rand = random.randint(1,2)
          if rand == 1: 
            self.obstacles.append(TallObstacle(self.gamespeed, x))
          else:
            self.obstacles.append(SmallObstacle(self.gamespeed, x))

    def play_step(self, action):
        self.frameiteration += 1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        self.move(action)

        self.screen.blit(self.background, (0,0))

        self.score += 0.03 * self.gamespeed
        self.gamespeed += 0.02

        self.placeObstacle()

        self.dino.update(self.screen)
        for obstacle in self.obstacles:
            obstacle.update(self.obstacles)     
            obstacle.draw(self.screen)
            self.collided = not obstacle.collide(self.dino)
        pygame.display.update()

    def move(self, action="none"):
        if action == "jump":
            self.dino.isJump = True
        if action == "duck":
            self.dino.isDuck = True
        else:
            self.dino.isDuck = False

dinogame = dinoGameAI()

while not dinogame.collided:

    dinogame.play_step("none")           
    dinogame.clock.tick(30)

    
    