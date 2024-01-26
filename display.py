import pygame
from settings import *
from board import *
from gameLoop import *
def display(clicked,win,timer):
    screen.fill("#b38b6d")
    drawBoard()
    if win == False:
        showClicked(clicked)
    displayTimer(timer)
    checkWin()
    drawNumbers()
    drawLines()
    pygame.display.update()
    clock.tick(FPS)

def displayTimer(timer):
    timerText = textFont.render(f"{timer // FPS}.{timer // 6 % 10}", True, "#2d3436")
    timerTextRect = timerText.get_rect()
    timerTextRect.midleft = (WIDTH - TILESIZE, MARGINGAP // 2)
    screen.blit(timerText,timerTextRect)


