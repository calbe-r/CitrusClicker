import pygame, sys
from pygame.locals import *

#screen size
screen_width = 640
screen_height = 480

FPS = pygame.time.Clock()
FPS.tick(60)

def main():
    pygame.init()

    pygame.display.set_mode(size=(screen_width,screen_height))



