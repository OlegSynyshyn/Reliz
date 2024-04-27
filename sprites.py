import pygame

class Sprite(pygame.sprite.Sprite):
    def __init__ (self, img_name="rover.png", x=200, y=200, width=100, height=100, speed=0):
        super().__init__()

        self.image = pygame.image.load(img_name)
        self.image = pygame.transform.scale(self.image, (width, height))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y 


    def reset (self, window):
        window.blit(self.image, (self.rect.x, self.rect.y))

    
class Hero(Sprite):
    def __init__(self):
        super().__init__("allience.png", 50,25,120,120,10)
        self.money = 90
        self.health = 50
        self.armor = 100
    
    
                