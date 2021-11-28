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
        self.distanceNextObstacle = 0
        self.type = 0

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
        self.jumped = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        self.move(action)


        self.screen.blit(self.background, (0,0))

        
        self.score += 0.03 * self.gamespeed
        self.gamespeed += 0.02

        reward = 0

        self.placeObstacle()

        self.dino.update(self.screen)
        for obstacle in self.obstacles:
            obstacle.update(self.obstacles)     
            obstacle.draw(self.screen)
            self.collided = not obstacle.collide(self.dino)

        self.distanceNextObstacle = obstacle.rect.x - self.dino.xPosition
        self.type = obstacle.type

        if self.jumped:
            obstacle.jumpcount +=1
        pygame.display.update()
        self.clock.tick(60)
        if obstacle.jumpcount < 10:
            reward += 5
        if not self.collided:
            reward += 10
        else:
            reward -= -10

        return reward, self.collided, self.score

    def move(self, action=[0,0]):
        if action[0] == 1:
            self.dino.isJump = True
            self.jumped = True
        if action[1] == 1:
            self.dino.isDuck = True
        else:
            self.dino.isDuck = False

