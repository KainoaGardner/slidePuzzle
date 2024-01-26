import pygame

pygame.init()

TILESIZE = 200
MARGINGAP = TILESIZE // 2
WIDTH = MARGINGAP * 2 + TILESIZE * 4
HEIGHT = MARGINGAP * 2 + TILESIZE * 4
FPS = 60

screen = pygame.display.set_mode((WIDTH,HEIGHT))
clock = pygame.time.Clock()
board = [[],[],[],[]]
font = pygame.font.SysFont("Bahnschrift",TILESIZE // 2,False)
textFont = pygame.font.SysFont("Bahnschrift",TILESIZE // 3,False)
highLight = pygame.surface.Surface((TILESIZE,TILESIZE))
highLight.fill("#b2bec3")
pygame.Surface.set_alpha(highLight,100)

winText = textFont.render("You Win!",True,"#2d3436")
winTextRect = winText.get_rect()
winTextRect.center = (WIDTH // 2, MARGINGAP // 2)
restartText = textFont.render("Press R to Reset",True,"#2d3436")
restartTextRect = restartText.get_rect()
restartTextRect.center = (WIDTH // 2, HEIGHT - MARGINGAP // 2)

