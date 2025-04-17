import pygame as py
from time import sleep
width = 20
height = 20
WHITE = (255, 255, 255)
BLACK = (0,0,0)
YELLOW = (0,255,255)
RED = (255,0,0)

class Mouse(py.sprite.Sprite):

    """
    Initializes the sprite
    Draws the "mouse" in it's initial state
    Creates a rect, direction, maximum grid size (not needed), a group variable(probably not needed), and a screen variable for animation purposes
    """
    def __init__(self,x,y,max,screen):
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
        self.max = max
        self.group = ""
        self.screen = screen

    """
    Draws a new "mouse" based on the direction input
    """
    def turn(self,direction):
        self.direction = direction
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


    """
    Mose the centerx/centery based on the direction
    Checks if it is line with the centre of any cell, if so, checks if there is a wall based on their direction
    Returns false if there is a wall in it's way
    Moves the centerx/centery if no wall in the way
    """
    def move(self,cell_grid): 
        curr_cell = self.get_current_cell(cell_grid)
        if curr_cell:
            wall = self.check_wall(curr_cell)
            if wall:
                return False
        if self.direction ==1:
            self.rect.centerx +=5
        elif self.direction ==2:
            self.rect.centery +=5
        elif self.direction == 3:
            self.rect.centerx -=5
        elif self.direction ==4:
            self.rect.centery -=5
        return True
          
    

    """
    Checks if the mouse is at the center of any cell and if so, returns the cell for a wall check
    """
    def get_current_cell(self,cell_grid):
            for row in cell_grid:
                for cell in row:
                    if py.Rect.colliderect(self.rect,cell.rect) and (self.rect.centerx,self.rect.centery)==(cell.rect.centerx,cell.rect.centery):
                        return cell
            return False
            
    """
    Checks if there is a wall in the way of the mouse based on the mouse's direction and the current cell it is on
    """
    

    def check_wall(self, cell):
        if self.direction==1 and cell.walls[1] == 1:
            return True
        elif self.direction==2 and cell.walls[3] == 1:
            return True
        elif self.direction==3 and cell.walls[0] == 1:
            return True
        elif self.direction==4 and cell.walls[2] == 1:
            return True
        return False
        
       
