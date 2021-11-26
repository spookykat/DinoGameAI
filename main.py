import pygame
import random
import math

from dino import Dino
from obstacles import SmallObstacle, TallObstacle

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
  jumped = False 
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE or event.key == pygame.K_UP:
                # Start to jump by setting isJump to True.
              dino.isJump = True
              jumped = True
            if event.key == pygame.K_DOWN:
              dino.isDuck = True
    else:
      dino.isDuck = False

  screen.blit(background, (0,0))

  score += 0.03 * gamespeed
  gamespeed += 0.02

  if len(obstacles) == 0:
    x = random.randint(10, 900)
    rand = random.randint(1,2)
    if rand == 2: 
      obstacles.append(TallObstacle(gamespeed, x))
    else:
      obstacles.append(SmallObstacle(gamespeed, x))

  dino.update(screen)

  for obstacle in obstacles:
    obstacle.update(obstacles)
    obstacle.draw(screen)
    running = obstacle.collide(dino)

  distanceNextObstacle = obstacle.rect.x - dino.xPosition
  if jumped:
    obstacle.jumpcount += 1
  print(obstacle.jumpcount)
  clock.tick(30)
  pygame.display.update()

print(math.floor(score))
