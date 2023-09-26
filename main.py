from curses import window
import pygame
import sys
import numpy as np

from src.functions import get_cell_points, get_neighbors_number
from src.settings import get_game_settings


pygame.init()

game_settings=get_game_settings()

color_window = game_settings.background_color

stats_font =pygame.font.SysFont("Arial",20)

n_cells_x,n_cells_y=game_settings.n_cells_x,game_settings.n_cells_y
cell_width=game_settings.width/n_cells_x
cell_height=game_settings.height/n_cells_y
GameState=np.zeros((n_cells_x,n_cells_y))

window = pygame.display.set_mode((game_settings.width, game_settings.height),pygame.RESIZABLE)
pygame.display.set_caption("The Life Game")

pause_execution=False


while True:
    NewGameState=np.copy(GameState)
    window.fill(color_window)

    events=pygame.event.get()

    for event in events:
        if event.type == pygame.KEYDOWN:
            pause_execution=not pause_execution
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        mouseClick=pygame.mouse.get_pressed()
        mouseClick=[int(i) for i in mouseClick]
        if sum(mouseClick)>0:
            pos_x,pos_y=pygame.mouse.get_pos()
            cell_x,cell_y=int(np.floor(pos_x/cell_width)),int(np.floor(pos_y/cell_height))
            NewGameState[cell_x,cell_y]=not mouseClick[2]

    for y in range(0,n_cells_x):
        for x in range(0,n_cells_y):
            if not pause_execution:

                n_neighbors=get_neighbors_number(GameState,x,y,n_cells_x,n_cells_y)

                #Rule 1
                if GameState[x,y]==0 and n_neighbors==3:
                    NewGameState[x,y]=1

                #Rule 2
                if GameState[x,y]==1 and (n_neighbors<2 or n_neighbors>3):
                    NewGameState[x,y]=0



            cell=get_cell_points(x,y,cell_width,cell_height)

            if NewGameState[x,y]==0:
                pygame.draw.polygon(window,(0,0,128),cell,1)
            else:
                pygame.draw.polygon(window,(255,255,255),cell,0)


    population=stats_font.render(f"Population: {np.sum(NewGameState)}",0,(255,0,0))
    window.blit(population,(10,30))



    GameState=np.copy(NewGameState)

    pygame.display.update()
