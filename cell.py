import pygame
width = 30
height = 30
WHITE = (255, 255, 255)
BLACK = (0,0,0)
class Cell(pygame.sprite.Sprite):
    def __init__(self,x,y,position ):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill(WHITE)
        pygame.draw.rect(self.image, WHITE, [0, 0, width, height])
        #getting and setting pygame surface rect
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        self.position = position 
        #Left, right, Top, bottom
        self.walls = [1,1,1,1]
        #self.draw_borders()
    def draw_borders(self):
        test = ""
        if self.walls[0] == 1:
            pygame.draw.line(self.image,BLACK,[0,0],[0,height+2],width=2)
       
        if self.walls[1] == 1:
            pygame.draw.line(self.image,BLACK,[width-2,0],[width-2,height+2],width=2)
       
        if self.walls[2] == 1:
            pygame.draw.line(self.image,BLACK,[0-2,0-2],[width,-2],width=2)
        
        if self.walls[3] == 1:
            pygame.draw.line(self.image,BLACK,[0,height-2],[width,height-2],width=2)
        

    
        
