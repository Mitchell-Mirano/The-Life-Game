from map.game_map import GameMap
from cells.game_cell import Cell

if __name__=="__main__":
    cell0=Cell(position_x=7,position_y=8,state=1)
    cell1=Cell(position_x=8,position_y=7,state=1)
    cell2=Cell(position_x=8,position_y=8,state=1)
    cell3=Cell(position_x=8,position_y=9,state=1)
    cell4=Cell(position_x=9,position_y=9,state=1)

    cells=[cell0,cell1,cell2,cell3,cell4]

    game=GameMap(size_x=30,size_y=30)
    game.initialize_population(cells)
    game.start_game()