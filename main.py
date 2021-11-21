import pygame

from dino import Dino

(width, height) = (700,300)
backgroundcolor = (255, 255, 255)

background = pygame.Surface((width,height))
background.fill((backgroundcolor))

dino = Dino()
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
                print("huts")
                dino.isJump = True

  screen.blit(background, (0,0))
  dino.update(screen)         
  clock.tick(30)
  pygame.display.update()
  