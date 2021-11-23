import pygame
import random
import math

from dino import Dino
from obstacles import Obstacle

(width, height) = (700,300)
backgroundcolor = (255, 255, 255)

background = pygame.Surface((width,height))
background.fill((backgroundcolor))

dino = Dino()
gamespeed = 10
score = 0

obstacles = []
clock = pygame.time.Clock()

screen = pygame.display.set_mode((width, height))

pygame.draw.line(background, pygame.Color(0,0,0), (0, 250), (700,250))


running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # Start to jump by setting isJump to True.
                dino.isJump = True

  screen.blit(background, (0,0))

  score += 0.03 * gamespeed
  gamespeed += 0.02
  print(gamespeed)

  if len(obstacles) == 0:
    x = random.randint(10, 900)
    obstacles.append(Obstacle(gamespeed, x))

  dino.update(screen)

  for obstacle in obstacles:
    obstacle.update(obstacles)
    obstacle.draw(screen)
    running = obstacle.collide(dino)

       
  clock.tick(30)
  pygame.display.update()
  
print(math.floor(score))