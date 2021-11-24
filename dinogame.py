import pygame
import random

from dino import Dino
from obstacles import TallObstacle, SmallObstacle

class dinoGame:
    def __init__(self):
        self.width = 700
        self.height = 300

        self.backgroundcolor = (255, 255, 255)
        self.background = pygame.Surface((self.width,self.height))
        self.background.fill((self.backgroundcolor))

        self.dino = Dino()
        self.gamespeed = 10
        self.score = 0
        self.obstacles = []
        self.clock = pygame.time.Clock()
        self.frameiteration = 0
        self.running = True

        self.screen = pygame.display.set_mode((self.width, self.height))

        pygame.draw.line(self.background, pygame.Color(0,0,0), (0, 250), (700,250))

    def reset(self):
        self.gamespeed = 10
        self.score = 0
        self.obstacles = []
        self.frameiteration = 0

    def placeObstacle(self):
        if len(self.obstacles) == 0:
          x = random.randint(10, 900)
          rand = random.randint(1,2)
          if rand == 1: 
            self.obstacles.append(TallObstacle(self.gamespeed, x))
          else:
            self.obstacles.append(SmallObstacle(self.gamespeed, x))

    def play_step(self):
        self.frameiteration += 1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE or event.key == pygame.K_UP:
                        # Start to jump by setting isJump to True.
                        self.dino.isJump = True
                    if event.key == pygame.K_DOWN:
                        self.dino.isDuck = True
            else:
                self.dino.isDuck = False

        self.screen.blit(self.background, (0,0))

        self.score += 0.03 * self.gamespeed
        self.gamespeed += 0.02

        self.placeObstacle()

        self.dino.update(self.screen)
        for obstacle in self.obstacles:
            obstacle.update(self.obstacles)     
            obstacle.draw(self.screen)
            self.running = obstacle.collide(self.dino)
        pygame.display.update()

dinogame = dinoGame()
while dinogame.running:
    dinogame.clock.tick(30)
    dinogame.play_step()
    