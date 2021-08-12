import pygame, sys, os
from pygame.locals import *

all_sprites = pygame.sprite.Group()
pygame.init()
screen = pygame.display.set_mode((640,480))
pygame.display.set_caption('Citrus Clicker')
clock = pygame.time.Clock()

#loading in images
bg_surface = pygame.image.load('assets/background.jpg').convert()

#orange clicker
clicker_surface = pygame.image.load('assets/f_citrus.png').convert_alpha()

class Clicker(pygame.sprite.Sprite):

    def __init__(self,width,height):
        super().__init__(all_sprites)
        self.image = clicker_surface
        self.rect = self.image.get_rect()

    def draw(self):
        screen.blit(self.image,self.rect)


money = 0
passive_cps = 0
active_cps = 1

#base values of generators
farmer_worth = 1
lemon_worth = 5 
orange_worth = 15
grape_worth = 40
lime_worth = 100

clicker = Clicker(0,0)

while True:
    for event in pygame.event.get():

        #close the game
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        #check for mouse clicks
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()



    screen.blit(bg_surface,(0,0))
    
    all_sprites.draw(screen)

    pygame.display.update()
    clock.tick(60)




