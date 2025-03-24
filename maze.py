import pygame
from time import sleep
import pygame.sprite
from cell import Cell
from create_maze import Maze
start_x = 50
start_y = 50
grid_size = 11
pygame.init()


#functions
def create_grid(start_x,start_y):
  ordered_grid = []
  for i in range(0,grid_size):
    row = []
    for k in range(0, grid_size):
      cell = Cell(start_x,start_y,[k,i])
      start_x+=30
      row.append(cell)
    ordered_grid.append(row)
    start_y += 30
    start_x = 50
  return ordered_grid

def redraw_borders(cells):
  for cell in cells:
    
    cell.draw_borders()
    all_cells.update()
    all_cells.draw(screen)
    pygame.display.update()
    sleep(0.8)


#height, width, and colour numeric values
width, height = 400, 400
backgroundColor = 100, 0, 150

#setting our screen and filling our background
screen = pygame.display.set_mode((width, height))
screen.fill(backgroundColor)

#updating our screen
pygame.display.flip()

ordered_grid = create_grid(start_x,start_y)

maze = Maze(ordered_grid,grid_size)
cells = maze.create_maze()
all_cells = pygame.sprite.Group()
for cell in cells:
  for c in cell:
    all_cells.add(c)
redraw_borders(all_cells)

while True:
  all_cells.update()
  all_cells.draw(screen)
  pygame.display.update()
  sleep(10/1000)