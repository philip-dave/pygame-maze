import pygame
from random import randint
from time import sleep
neighbour_list = {1:"top",2:"bottom",3:"left",4:"right"}
class Maze(pygame.sprite.Sprite):

    def __init__(self,initial_grid, max_size,screen):
        self.grid = initial_grid
        self.maze = []
        self.max = max_size
        self.frontier = []
        self.screen = screen
        self.all_cells = pygame.sprite.Group()
        self.set_group()
    
    def set_group(self):
        for i in range(self.max):
            for k in range(self.max):
                self.all_cells.add(self.grid[i][k])

    """
    Drawing borders in real time to see maze progress
    """
    def draw_borders(self):
        self.screen.fill((100, 0, 150))
        pygame.display.flip()
        self.all_cells.empty()
        self.set_group()
        for cell in self.all_cells:
            #self.screen.fill((100, 0, 150))
            #pygame.display.flip()
            cell.draw_borders()
        self.all_cells.update()
        self.all_cells.draw(self.screen)
        pygame.display.update()
        pygame.display.flip()
        sleep(0.8)

    """
    Gets the new frontier from the current position
    Left, Right, Top, Bottom
    Invalid positions are not added
    Added ones must not be in the frontier already
    Added ones must not already have been used by cell before (bad logic here)
    """
    def get_new_frontier(self,position):
        neighbor_set = []
        left = [position[0],position[1]-1]
        right = [position[0],position[1]+1]
        top = [position[0]-1,position[1]]
        bottom = [position[0]+1,position[1]]
        used_neighbours = self.grid[position[0]][position[1]].used_neighbours
        if left not in self.maze and left[1]>=0 and left not in self.frontier and left not in used_neighbours:
            self.grid[left[0]][left[1]].is_front = True
            self.frontier.append(left)
            neighbor_set.append(left)
        elif left[1]>=0 and left not in used_neighbours:
            #self.grid[left[1]][left[0]].is_front = True
            neighbor_set.append(left)
        if right not in self.maze and right[1]<self.max and right not in self.frontier and  right not in used_neighbours:
            self.grid[right[0]][right[1]].is_front = True
            self.frontier.append(right)
            neighbor_set.append(right)
        elif right[1]<self.max-1 and  right not in used_neighbours:
            #self.grid[right[1]][right[0]].is_front = True
            neighbor_set.append(right)
        if top not in self.maze and top[0]>=0 and top not in self.frontier and top not in used_neighbours:
            self.grid[top[0]][top[1]].is_front = True
            self.frontier.append(top)
            neighbor_set.append(top)
        elif top[0]>=0 and top not in used_neighbours:
            #self.grid[top[1]][top[0]].is_front = True
            neighbor_set.append(top)
        if bottom not in self.maze and bottom[0]!=self.max and bottom not in self.frontier and bottom not in used_neighbours:
            self.grid[bottom[0]][bottom[1]].is_front = True
            self.frontier.append(bottom)
            neighbor_set.append(bottom)
        elif bottom[0]<self.max-1 and bottom not in used_neighbours:
            #self.grid[bottom[1]][bottom[0]].is_front = True
            neighbor_set.append(bottom)
        return neighbor_set

     
    def get_random_neighbour(self,neighbours,cell):
        return neighbours[randint(0,len(neighbours)-1)]
    """
    Removing walls from the random neighbour
    Checking if the neighbor is left, right, top or bottom and removing appropriate walls
    """
    def remove_walls(self,cell,neighbour):
        bad_walls = [1,1,1,1]
        
        if cell[0]-1==neighbour[0]:
            self.grid[cell[0]][cell[1]].walls[2] = 0
            self.grid[neighbour[0]][neighbour[1]].walls[3] = 0
        elif cell[0]+1==neighbour[0]:
            self.grid[cell[0]][cell[1]].walls[3] = 0
            self.grid[neighbour[0]][neighbour[1]].walls[2] = 0
        elif cell[1]-1==neighbour[1]:
            self.grid[cell[0]][cell[1]].walls[0] = 0
            self.grid[neighbour[0]][neighbour[1]].walls[1] = 0
        elif cell[1]+1==neighbour[1]:
            self.grid[cell[0]][cell[1]].walls[1] = 0
            self.grid[neighbour[0]][neighbour[1]].walls[0] = 0
        

    def create_maze(self):
        position = [5,5]
        self.maze.append([5,5])
        
        neighbours = self.get_new_frontier(position)
        while len(self.frontier)>0:
            cell = position
            self.grid[cell[0]][cell[1]].is_current = True
            self.draw_borders()
            if cell in self.frontier:
                
                self.frontier.remove(cell)
                self.maze.append(cell)
            if len(neighbours)!=0:
                
                neighbour = self.get_random_neighbour(neighbours,cell)
                self.grid[cell[0]][cell[1]].used_neighbours.append(neighbour)
                self.grid[neighbour[0]][neighbour[1]].used_neighbours.append(cell)
                self.remove_walls(cell,neighbour)
                self.maze.append(cell)
            
            
            self.grid[cell[0]][cell[1]].is_front = False
            self.grid[cell[0]][cell[1]].is_current = False
            if len(self.frontier)>0:
                position = self.frontier[randint(0,len(self.frontier)-1)]
                
                neighbours = self.get_new_frontier(position)
         
            
        return self.grid