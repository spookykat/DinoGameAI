import pygame



class Obstacle:
    def __init__(self, game_speed, x):
        self.rect = pygame.Rect(700, 210, 10, 40)
        self.rect.x = 700 + x
        self.game_speed = game_speed
        self.color_green = pygame.Color(0,255,0)
    
    def update(self, obstacles):
        self.rect.x -= self.game_speed
        if self.rect.x < -self.rect.width:
            obstacles.pop(0)

    def collide(self, dino):
        if self.rect.colliderect(dino.dinoSprite):
            return False
        return True

    def draw(self, screen):
        pygame.draw.rect(screen, self.color_green, self.rect)
