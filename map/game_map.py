import numpy as np
from typing import List
import time
import os
from cells.game_cell import Cell


class GameMap():
    def __init__(self,size_x:int=10,size_y:int=10):
        self.size_x = size_x
        self.size_y = size_y
        self.map_state=np.zeros([self.size_x,self.size_y])
        self.game_cells={}
        

    def string_game_map(self):
        string_game=""
        for row in self.map_state:
            string_game += " ".join([str(int(value))+" " for value in row]) + "\n"
        return string_game

    def initialize_population(self,list_of_cells:List[Cell]):
        for cell in list_of_cells:
            self.map_state[cell.position_y][cell.position_x]=1
            self.game_cells[f"({cell.position_x},{cell.position_y})"]=cell


    def neighbors_positions(self,cell:Cell):
        x=cell.position_x
        y=cell.position_y
        return [(x,y+1),(x,y-1),(x+1,y),(x-1,y),(x+1,y+1),(x+1,y-1),(x-1,y-1),(x-1,y+1)]

    
    def cell_neighbors(self,cell:Cell)->int:
        n_neighbors=0
        for x,y in self.neighbors_positions(cell):
            if self.map_state[y][x]==1:
                n_neighbors=n_neighbors+1
        return n_neighbors


    def future_state_of_cell(self, cell:Cell):
        living_neighbors_number=self.cell_neighbors(cell)

        future_state=0
        if cell.state==0 and living_neighbors_number==3:
            future_state=1

        if cell.state==1 and living_neighbors_number in [2,3]:
            future_state=1

        return future_state

    def posible_cells(self):
        for cell in list(self.game_cells.values()):
            current_cell_neighbors_positions=self.neighbors_positions(cell)
            for position in current_cell_neighbors_positions:
                current_position=f"({position[0]},{position[1]})"
                if current_position not in list(self.game_cells.keys()):
                    new_cell=Cell(position_x=position[0],position_y=position[1],state=0)
                    self.game_cells[current_position]=new_cell
    


    def a_cell_is_born(self, cell:Cell):
        self.map_state[cell.position_y][cell.position_x]=1

    def a_cell_dies(self, cell:Cell):
        self.map_state[cell.position_y][cell.position_x]=0
        del self.game_cells[f"({cell.position_x},{cell.position_y})"]

    def start_game(self):
        for i in range(30):
            print(self.string_game_map())
            print()
            self.posible_cells()
            for cell in list(self.game_cells.values()):
                future_state=self.future_state_of_cell(cell)
                if future_state==0:
                    self.game_cells[f"({cell.position_x},{cell.position_y})"].state=0

                if future_state==1:
                    self.game_cells[f"({cell.position_x},{cell.position_y})"].state=1
            
            for cell in list(self.game_cells.values()):
                if cell.state==0:
                    self.a_cell_dies(cell)

                if cell.state==1:
                    self.a_cell_is_born(cell)

            time.sleep(1)
            os.system("clear")