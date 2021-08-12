import pygame, sys, os, time
from pygame.locals import *

class Clicker(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        clicker_surface = pygame.image.load('assets/f_citrus.png').convert_alpha()
        self.image = clicker_surface
        self.rect = self.image.get_rect()

    def handle_event(self, event):
        global money, active_cps, clicking

        if event.type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos):
            clicking = True
            
        if event.type == pygame.MOUSEBUTTONUP and clicking == True:
            if self.rect.collidepoint(event.pos):
                money += active_cps
                print(money)
            clicking = False

    def update(self):
        self.handle_event(event)

#class Button(pygame.sprite.Sprite):

#def display_score():

pygame.init()
screen = pygame.display.set_mode((640,480))
pygame.display.set_caption('Citrus Clicker')
clock = pygame.time.Clock()
test_font = pygame.font.Font('font/Pixeltype.ttf', 50)
game_active = True

clicking = False
money = 0
passive_cps = 0
active_cps = 1
farmer_worth = 1
lemon_worth = 5 
orange_worth = 15
grape_worth = 40
lime_worth = 100

orange = pygame.sprite.GroupSingle()
orange.add(Clicker())

bg_surface = pygame.image.load('assets/background.jpg').convert()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    if game_active:   
        screen.blit(bg_surface,(0,0))
        orange.draw(screen)
        orange.update()
    else:
        screen.fill((255,165,0))

    pygame.display.update()
    clock.tick(60)




