import pygame



class Obstacle:
    def __init__(self, game_speed, x):
        self.rect = pygame.Rect(700, 0, 0, 0)
        self.rect.x = 700 + x
        self.game_speed = game_speed
        self.color_green = pygame.Color(0,255,0)
        self.type = None
        self.jumpcount = 0
    
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

class SmallObstacle(Obstacle):
    def __init__(self, game_speed, x):
        super().__init__(game_speed, x)
        self.rect.y = 230
        self.rect.width = 50
        self.rect.height = 20
        self.type = 1
        

class TallObstacle(Obstacle):
    def __init__(self, game_speed, x):
        super().__init__(game_speed, x)
        self.rect.y = 200
        self.rect.width = 10
        self.rect.height = 50
        self.type = 2