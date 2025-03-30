import pygame
from random import randint
import pdb

neighbour_list = {1:"top",2:"bottom",3:"left",4:"right"}
class Maze(pygame.sprite.Sprite):

    def __init__(self,initial_grid, max_size):
        self.grid = initial_grid
        self.maze = []
        self.max = max_size
        self.frontier = []
        

    
    def get_new_frontier(self,position):
        neighbor_set = []
        left = [position[0]-1,position[1]]
        right = [position[0]+1,position[1]]
        top = [position[0],position[1]-1]
        bottom = [position[0],position[1]+1]
        
        # pdb.set_trace()

        print(f"Left: [{left[0]},{left[1]}], Right: [{right[0]},{right[1]}], Top: [{top[0]},{top[1]}], Bottom: [{bottom[0]},{bottom[1]}]")

        if left not in self.maze and left[0]>=0 and left not in self.frontier:
            print("Set Left 1")
            self.frontier.append(left)
            neighbor_set.append(left)            
        elif left[0]>=0:
            print("Set Left 2")
            neighbor_set.append(left)
        if right not in self.maze and right[0]<self.max-1 and right not in self.frontier:
            print("Set Right 1")
            self.frontier.append(right)
            neighbor_set.append(right)
        elif right[0]<self.max-1:
            print("Set Right 2")
            neighbor_set.append(right)
        if top not in self.maze and top[1]>=0 and top not in self.frontier:
            print("Set Top 1")
            self.frontier.append(top)
            neighbor_set.append(top)
        elif top[1]>=0:
            print("Set Top 2")
            neighbor_set.append(top)
        if bottom not in self.maze and bottom[1]!=self.max-1 and bottom not in self.frontier:
            print("Set Bottom 1")
            self.frontier.append(bottom)
            neighbor_set.append(bottom)
        elif position[1]<self.max-1:
            print("Set Bottom 2")
            neighbor_set.append(bottom)
        return neighbor_set

     
    def get_random_neighbour(self,neighbours):
        new_neighbours = neighbours[randint(0,len(neighbours)-1)]
        # print(new_neighbours)
        return new_neighbours
    
    def remove_walls(self,cell,neighbour):
        # print(f"Cell: [{cell[0]}, {cell[1]}], Neighbour: [{neighbour[0]}, {neighbour[1]}]")
        if cell[0]-1==neighbour[0]:
            # print(f"First: {cell[0]-1} : {neighbour[0]}")
            self.grid[cell[0]][cell[1]].walls[0] = 0
            self.grid[neighbour[0]][neighbour[1]].walls[1] = 0
        elif cell[0]+1==neighbour[0]:
            # print(f"Second:  {cell[0]+1} : {neighbour[0]}")
            self.grid[cell[0]][cell[1]].walls[1] = 0
            self.grid[neighbour[0]][neighbour[1]].walls[0] = 0
        elif cell[1]-1==neighbour[1]:
            # print(f"Third:  {cell[1]-1} : {neighbour[1]}")
            self.grid[cell[0]][cell[1]].walls[2] = 0
            self.grid[neighbour[0]][neighbour[1]].walls[3] = 0
        elif cell[1]+1==neighbour[1]:
            # print(f"Fourth:  {cell[0]+1} : {neighbour[1]}")
            self.grid[cell[0]][cell[1]].walls[3] = 0
            self.grid[neighbour[0]][neighbour[1]].walls[2] = 0
        

    def create_maze(self):
        position = [randint(1, 8), randint(1, 8)]        
        self.maze.append(position)
        
        neighbours = self.get_new_frontier(position)
        while len(self.frontier)>0:
            cell = position
            neighbour = self.get_random_neighbour(neighbours)
            self.remove_walls(cell,neighbour)
            self.maze.append(cell)
            if cell in self.frontier:
                self.frontier.remove(cell)
            
            if len(self.frontier)>0:
                position = self.frontier[randint(0,len(self.frontier)-1)]
                neighbours = self.get_new_frontier(position)
         
        
        return self.grid