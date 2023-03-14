import pygame
from gameObject import GameObject

class Player: # type: ignore
    def __init__ (self,x,y,width,height,image_path):
        image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(image, (width, height))
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        
class Player(GameObject):
    def __init__ (self, x, y, width, height, image_path, speed):
        super().__init__(x, y, width, height, image_path)
        self.speed = speed
        
    def move(self, direction, max_height):
        if (self.y >= max_height - self.height and direction >0) or (self.y == 0 and direction < 0):
            return 
        self.y += (direction * self.speed)