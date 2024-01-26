import pygame
from display import display
from board import *

def run():
    pygame.init()
    shuffleBoard()
    run = True
    clicked = []
    win = False
    timer = 0
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mousePos = pygame.mouse.get_pos()
                if win == False:
                    if MARGINGAP <= mousePos[0] <= WIDTH - MARGINGAP and MARGINGAP <= mousePos[1] <= HEIGHT - MARGINGAP:
                        tile = ((mousePos[0] - MARGINGAP) // TILESIZE, (mousePos[1] - MARGINGAP) // TILESIZE)
                        if len(clicked) >= 2 and tile != getEmptyTile():
                            clicked.clear()
                            clicked.append(tile)
                        elif len(clicked) == 0 and tile != getEmptyTile():
                            clicked.append(tile)
                        else:
                            clicked.append(tile)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    board.clear()
                    for _ in range(4):
                        board.append([])
                    shuffleBoard()
                    timer = 0
                    clicked = []
                    win = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    board.clear()
                    for row in [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,0]]:
                        board.append(row)

        if checkWin() != None:
            win = checkWin()
        if win == False:
            timer += 1
        display(clicked,win,timer)


    pygame.quit()