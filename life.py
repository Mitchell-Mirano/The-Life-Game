import pygame
import sys
import numpy as np
import time
pygame.init()
width, height =1920,1080
color = 25, 25, 25

screen = pygame.display.set_mode((width, height),pygame.RESIZABLE)
screen.fill(color)

n_cells_x,n_cells_y=100,100

cell_width=width/n_cells_x
cell_height=height/n_cells_y


GameState=np.zeros((n_cells_x,n_cells_y))

pause_execution=False

while True:
    NewGameState=np.copy(GameState)
    screen.fill(color)
    

    events=pygame.event.get()

    for event in events:
        if event.type == pygame.KEYDOWN:
            pause_execution=not pause_execution
        if event.type == pygame.QUIT:
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
                n_neighbors=GameState[(x-1)%n_cells_x,(y-1)%n_cells_y] +\
                            GameState[(x)%n_cells_x,(y-1)%n_cells_y] +\
                            GameState[(x+1)%n_cells_x,(y-1)%n_cells_y] +\
                            GameState[(x-1)%n_cells_x,(y)%n_cells_y] +\
                            GameState[(x+1)%n_cells_x,(y)%n_cells_y] +\
                            GameState[(x-1)%n_cells_x,(y+1)%n_cells_y] +\
                            GameState[(x)%n_cells_x,(y+1)%n_cells_y] +\
                            GameState[(x+1)%n_cells_x,(y+1)%n_cells_y]

                #Rule 1
                if GameState[x,y]==0 and n_neighbors==3:
                    NewGameState[x,y]=1

                #Rule 2
                if GameState[x,y]==1 and (n_neighbors<2 or n_neighbors>3):
                    NewGameState[x,y]=0

            poly=[(x*cell_width,y*cell_height),
                ((x+1)*cell_width,y*cell_height),
                ((x+1)*cell_width,(y+1)*cell_height),
                (x*cell_width,(y+1)*cell_height)]

            if NewGameState[x,y]==0:
                pygame.draw.polygon(screen,(128,128,128),poly,1)
            else:
                pygame.draw.polygon(screen,(255,255,255),poly,0)

    GameState=np.copy(NewGameState)

    pygame.display.flip()
