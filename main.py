import pygame

from dino import Dino

(width, height) = (700,300)
backgroundcolor = (255, 255, 255)
dino = Dino()

screen = pygame.display.set_mode((width, height))
screen.fill(backgroundcolor)

pygame.draw.line(screen, pygame.Color(0,0,0), (0, 250), (700,250))
dino.draw(screen)
pygame.display.flip()

running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False