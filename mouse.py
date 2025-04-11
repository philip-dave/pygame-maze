import pygame as py
width = 20
height = 20
WHITE = (255, 255, 255)
BLACK = (0,0,0)
YELLOW = (0,255,255)
RED = (255,0,0)

class Mouse(py.sprite.Sprite):

    def __init__(self,x,y):
        super().__init__()
        self.image = py.Surface((width, height))
        self.image.fill(WHITE)
        py.draw.rect(self.image, WHITE, [0, 0, width, height])
        py.draw.polygon(self.image,RED,((0,0),(0,20),(20,10)))
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        #directions [1,2,3,4]
        #right down left up
        self.direction = 1

    def turn(self,direction):
        if direction==1:
            self.image.fill(WHITE)
            py.draw.rect(self.image, WHITE, [0, 0, width, height])
            py.draw.polygon(self.image,RED,((0,0),(0,20),(20,10)))
        elif direction==2:
            self.image.fill(WHITE)
            py.draw.rect(self.image, WHITE, [0, 0, width, height])
            py.draw.polygon(self.image,RED,((0,0),(20,0),(10,20)))
        elif direction==3:
            self.image.fill(WHITE)
            py.draw.rect(self.image, WHITE, [0, 0, width, height])
            py.draw.polygon(self.image,RED,((20,0),(20,20),(0,10)))
        elif direction==4:
            self.image.fill(WHITE)
            py.draw.rect(self.image, WHITE, [0, 0, width, height])
            py.draw.polygon(self.image,RED,((0,20),(20,20),(10,0)))
