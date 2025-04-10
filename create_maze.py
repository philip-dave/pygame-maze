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
        sleep(0.2)

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
        if left not in self.frontier and left[1]>=0 and left not in self.maze:
            self.frontier.append(left)
            self.grid[left[0]][left[1]].is_front = True
        if right not in self.frontier and right[1]<self.max and right not in self.maze:
            self.frontier.append(right)
            self.grid[right[0]][right[1]].is_front = True
        if top not in self.frontier and top[0]>=0 and top not in self.maze:
            self.frontier.append(top)
            self.grid[top[0]][top[1]].is_front = True
        if bottom not in self.frontier and bottom[0]<self.max and bottom not in self.maze:
            self.frontier.append(bottom)
            self.grid[bottom[0]][bottom[1]].is_front = True

     
    def get_random_neighbour(self,cell,is_first):
        maze_neigh = []
        neighbours = []
        left = [cell[0],cell[1]-1]
        right = [cell[0],cell[1]+1]
        top = [cell[0]-1,cell[1]]
        bottom = [cell[0]+1,cell[1]]
        neighbours.append(left)
        neighbours.append(right)
        neighbours.append(top)
        neighbours.append(bottom)
        if is_first:
            for neighbour in neighbours:
                if neighbour[0]>=0 and neighbour[0]<self.max and neighbour[1]>=0 and neighbour[1]<self.max:
                    maze_neigh.append(neighbour)
            return maze_neigh[randint(0,len(maze_neigh)-1)]
        else:
            for neighbour in neighbours:
                if neighbour in self.maze:
                    maze_neigh.append(neighbour)
        
        return maze_neigh[randint(0,len(maze_neigh)-1)]
    """
    Removing walls from the random neighbour
    Checking if the neighbor is left, right, top or bottom and removing appropriate walls
    """
    def remove_walls(self,cell,neighbour):        
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
        position = [self.max//2,self.max//2]
        self.grid[position[0]][position[1]].is_current = True 
        
        self.get_new_frontier(position)
        self.draw_borders()
        self.maze.append(position)  
        is_first = True
        while len(self.frontier)>0:
            self.draw_borders()
            cell = position
            neighbour = self.get_random_neighbour(cell,is_first)
            is_first = False
            self.maze.append(cell)
            self.maze.append(neighbour)
            self.remove_walls(cell,neighbour)
            self.draw_borders()
            if cell in self.frontier:
                self.frontier.remove(cell)
            if neighbour in self.frontier:
                self.frontier.remove(neighbour)
            self.get_new_frontier(cell)
            self.grid[cell[0]][cell[1]].is_current = False
            self.grid[cell[0]][cell[1]].is_front = False
            self.grid[neighbour[0]][neighbour[1]].is_front = False
            self.draw_borders()
            self.grid[cell[0]][cell[1]].is_current = False
            self.grid[cell[0]][cell[1]].is_front = False
            self.grid[neighbour[0]][neighbour[1]].is_front = False
            if len(self.frontier)>0:
                position = self.frontier[randint(0,len(self.frontier)-1)]
                self.grid[position[0]][position[1]].is_current = True
        return self.grid