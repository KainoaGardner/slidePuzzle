import pygame
import random
from settings import *

def shuffleBoard():
    numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
    numbers = random.sample(numbers,len(numbers))
    numbers.append(0)
    for i in range(len(board)):
        for j in range(4):
            board[i].append(numbers[j + i * 4])

def drawBoard():
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 0:
                pygame.draw.rect(screen,"#b2bec3",pygame.Rect(MARGINGAP + TILESIZE * j,MARGINGAP + TILESIZE * i,TILESIZE,TILESIZE))
            else:
                pygame.draw.rect(screen, "#ecf0f1",pygame.Rect(MARGINGAP + TILESIZE * j, MARGINGAP + TILESIZE * i, TILESIZE, TILESIZE))

def drawLines():
    for i in range(5):
        pygame.draw.line(screen,"#2d3436",(MARGINGAP + TILESIZE * i,MARGINGAP),(MARGINGAP + TILESIZE * i,HEIGHT - MARGINGAP),5)
    for i in range(5):
        pygame.draw.line(screen,"#2d3436",(MARGINGAP,MARGINGAP + TILESIZE * i),(WIDTH - MARGINGAP,MARGINGAP + TILESIZE * i),5)

def drawNumbers():
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] != 0:
                number = font.render(f"{board[i][j]}",True,"#2d3436")
                numberRect = number.get_rect()
                numberRect.center = (MARGINGAP + TILESIZE * j + TILESIZE // 2,MARGINGAP + TILESIZE * i + TILESIZE // 2)
                screen.blit(number,numberRect)

def drawHightLight(clicked):
    screen.blit(highLight,(clicked[0][0] * TILESIZE + MARGINGAP,clicked[0][1] * TILESIZE + MARGINGAP))


def swapTiles(clicked):
    if board[clicked[1][1]][clicked[1][0]] == 0:
        if clicked[0] in [(clicked[1][0] -1,clicked[1][1]),(clicked[1][0] + 1,clicked[1][1]),(clicked[1][0],clicked[1][1] - 1),(clicked[1][0],clicked[1][1] + 1)]:
            temp = board[clicked[0][1]][clicked[0][0]]
            board[clicked[0][1]][clicked[0][0]] = board[clicked[1][1]][clicked[1][0]]
            board[clicked[1][1]][clicked[1][0]] = temp

def showClicked(clicked):
    if len(clicked) == 1:
        drawHightLight(clicked)
    elif len(clicked) == 2:
        swapTiles(clicked)

def checkWin():
    if board == [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,0]]:
        screen.blit(winText,winTextRect)
        screen.blit(restartText,restartTextRect)
        return True
    else:
        return False

def changeBoard():
    board = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,0]]

def getEmptyTile():
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 0:
                return (j,i)