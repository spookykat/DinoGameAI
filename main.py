import pygame

from dino import Dino
from obstacles import Obstacle

(width, height) = (700,300)
backgroundcolor = (255, 255, 255)

background = pygame.Surface((width,height))
background.fill((backgroundcolor))

dino = Dino()

obstacle1 = Obstacle(20)
obstacles = [obstacle1]
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

  for obstacle in obstacles:
    obstacle.update(obstacles)
    obstacle.draw(screen)

  dino.update(screen)         
  clock.tick(30)
  pygame.display.update()
  