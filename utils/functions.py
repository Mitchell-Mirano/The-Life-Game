
import numpy as np

def get_cell_points(x:int, y:int,cell_width:float,cell_height:float):

    poly=[(x*cell_width,y*cell_height),
        ((x+1)*cell_width,y*cell_height),
        ((x+1)*cell_width,(y+1)*cell_height),
        (x*cell_width,(y+1)*cell_height)]

    return poly

def get_neighbors_number(GameState:np.array,x:int,y:int,n_cells_x:int,n_cells_y:int):

    n_neighbors=GameState[(x-1)%n_cells_x,(y-1)%n_cells_y] +\
            GameState[(x)%n_cells_x,(y-1)%n_cells_y] +\
            GameState[(x+1)%n_cells_x,(y-1)%n_cells_y] +\
            GameState[(x-1)%n_cells_x,(y)%n_cells_y] +\
            GameState[(x+1)%n_cells_x,(y)%n_cells_y] +\
            GameState[(x-1)%n_cells_x,(y+1)%n_cells_y] +\
            GameState[(x)%n_cells_x,(y+1)%n_cells_y] +\
            GameState[(x+1)%n_cells_x,(y+1)%n_cells_y]

    return n_neighbors
    