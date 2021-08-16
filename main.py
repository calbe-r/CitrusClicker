import pygame, sys, os, time
from pygame.locals import *

black = (255,255,255)
white = (0,0,0)

class Clicker(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.sprites = []
        self.sprites.append(pygame.image.load('assets/f_citrus.png').convert_alpha())
        self.sprites.append(pygame.image.load('assets/f_citruscls.png').convert_alpha())
        self.clicking = False
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]
        self.rect = self.image.get_rect()
        self.click_sound = pygame.mixer.Sound('assets/Click_effect')

    def handle_event(self, event):
        global money, active_cps

        if event.type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos):
            self.clicking = True
            self.current_sprite = 1
            
        if event.type == pygame.MOUSEBUTTONUP and self.clicking == True:
            if self.rect.collidepoint(event.pos):
                money += active_cps
                print(money)
            self.clicking = False
            self.current_sprite = 0
            self.click_sound.play()


    def update(self):
        self.handle_event(event)
        self.image = self.sprites[self.current_sprite]

class Generator_Button(pygame.sprite.Sprite):

    def __init__(self,price,multiplier,type_index,x,y):
        super().__init__()
        #There has to be a better way istg
        self.clicking = False
        self.multi = multiplier
        self.current_price = price
        self.index = type_index
        self.x = x
        self.y = y
        self.current_sprite = 0
        self.click_sound = pygame.mixer.Sound('assets/Generator_effect')

        if(type_index == 0):
            self.sprites = []
            self.sprites.append(pygame.image.load('assets/farmer.jpg').convert_alpha())
            self.sprites.append(pygame.image.load('assets/farmcl.jpg').convert_alpha())
        elif(type_index == 1):
            self.sprites = []
            self.sprites.append(pygame.image.load('assets/lemon_bush.jpg').convert_alpha())
            self.sprites.append(pygame.image.load('assets/lemon_bushcl.jpg').convert_alpha())
        elif(type_index == 2):
            self.sprites = []
            self.sprites.append(pygame.image.load('assets/orange_tree.jpg').convert_alpha())
            self.sprites.append(pygame.image.load('assets/orange_treecl.jpg').convert_alpha())
        elif(type_index == 3):
            self.sprites = []
            self.sprites.append(pygame.image.load('assets/grapefruit_orchard.jpg').convert_alpha())
            self.sprites.append(pygame.image.load('assets/grapefruit_orchardcl.jpg').convert_alpha())
        else:
            self.sprites = []
            self.sprites.append(pygame.image.load('assets/Lime_replicator.jpg').convert_alpha())
            self.sprites.append(pygame.image.load('assets/Lime_replicatorcl.jpg').convert_alpha())

        self.image = self.sprites[self.current_sprite]
        self.rect = self.image.get_rect(topleft = (x,y))

    def handle_event(self, event):
        global money, farmers, lemon, orange, grapefruit, lime

        if event.type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos) and money >= self.current_price:
            self.clicking = True
            self.current_sprite = 1
            
        if event.type == pygame.MOUSEBUTTONUP and self.clicking == True:                      
            if self.rect.collidepoint(event.pos) and money >= self.current_price:
                money -= self.current_price
                self.current_price = round(self.current_price*self.multi)

                if(self.index == 0):
                    farmers += 1
                elif(self.index == 1):
                    lemon += 1
                elif(self.index == 2):
                    orange += 1
                elif(self.index == 3):
                    grapefruit += 1
                else:
                    lime += 1

            self.clicking = False                     
            self.current_sprite = 0 
            self.click_sound.play()
            print(money)


    def update(self):
        self.handle_event(event)
        self.image = self.sprites[self.current_sprite]
        cost_box = cost_font.render(f'{self.current_price}',True, black)
        cost_rect = cost_box.get_rect(topleft = (self.x + 7,self.y + 80))        
        screen.blit(cost_box,cost_rect)

class Upgrade_Button(pygame.sprite.Sprite):

    def __init__(self, price, multiplier, type_index, x, y):
        super().__init__()
        self.clicking = False
        self.multi = multiplier
        self.current_price = price
        self.index = type_index
        self.x = x
        self.y = y
        self.current_sprite = 0
        self.click_sound = pygame.mixer.Sound('assets/Upgrade_effect')

        if(type_index == 0):
            self.sprites = []
            self.sprites.append(pygame.image.load('assets/roided_farmer.jpg').convert_alpha())
            self.sprites.append(pygame.image.load('assets/roided_farmercl.jpg').convert_alpha())
        elif(type_index == 1):
            self.sprites = []
            self.sprites.append(pygame.image.load('assets/shears.jpg').convert_alpha())
            self.sprites.append(pygame.image.load('assets/shearscl.jpg').convert_alpha())
        elif(type_index == 2):
            self.sprites = []
            self.sprites.append(pygame.image.load('assets/branch_graffting.jpg').convert_alpha())
            self.sprites.append(pygame.image.load('assets/branch_grafftingcl.jpg').convert_alpha())
        elif(type_index == 3):
            self.sprites = []
            self.sprites.append(pygame.image.load('assets/pesticide.jpg').convert_alpha())
            self.sprites.append(pygame.image.load('assets/pesticidecl.jpg').convert_alpha())
        elif(type_index == 4):
            self.sprites = []
            self.sprites.append(pygame.image.load('assets/lime_tech.jpg').convert_alpha())
            self.sprites.append(pygame.image.load('assets/lime_techcl.jpg').convert_alpha())
        elif(type_index == 5):
            self.sprites = []
            self.sprites.append(pygame.image.load('assets/bigger_orange.jpg').convert_alpha())
            self.sprites.append(pygame.image.load('assets/bigger_orangecl.jpg').convert_alpha())
        elif(type_index == 6):
            self.sprites = []
            self.sprites.append(pygame.image.load('assets/fat_orange.jpg').convert_alpha())
            self.sprites.append(pygame.image.load('assets/fat_orangecl.jpg').convert_alpha())
        elif(type_index == 7):
            self.sprites = []
            self.sprites.append(pygame.image.load('assets/price_gouging.jpg').convert_alpha())
            self.sprites.append(pygame.image.load('assets/price_gougingcl.jpg').convert_alpha())
        else:
            self.sprites = []
            self.sprites.append(pygame.image.load('assets/finale.jpg').convert_alpha())
            self.sprites.append(pygame.image.load('assets/finalecl.jpg').convert_alpha())

        self.image = self.sprites[self.current_sprite]
        self.rect = self.image.get_rect(topleft = (x,y))                  

    def handle_event(self,event):
        global money, farmer_upg, lemon_upg, orange_upg, grapefruit_upg, lime_upg, bigger_upg, fat_upg, gouging_upg, game_active

        if event.type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos) and money >= self.current_price:
            self.clicking = True
            self.current_sprite = 1

        if event.type == pygame.MOUSEBUTTONUP and self.clicking == True:                      
            if self.rect.collidepoint(event.pos) and money >= self.current_price:
                money -= self.current_price
                self.current_price = round(self.current_price*self.multi)

                if(self.index == 0):
                    farmer_upg += 1
                elif(self.index == 1):
                    lemon_upg += 1
                elif(self.index == 2):
                    orange_upg += 1
                elif(self.index == 3):
                    grapefruit_upg += 1
                elif(self.index == 4):
                    lime_upg += 1
                elif(self.index == 5):
                    bigger_upg += 1
                elif(self.index == 6):
                    fat_upg += 1
                elif(self.index == 7):
                    gouging_upg += 1
                else:
                    game_active = False
            self.clicking = False
            self.current_sprite = 0
            self.click_sound.play()
            print(money)

    def update(self):
        self.handle_event(event)
        self.image = self.sprites[self.current_sprite]
        cost_box = cost_font.render(f'{self.current_price}',True, black)
        cost_rect = cost_box.get_rect(topleft = (self.x + 7,self.y + 80))       
        screen.blit(cost_box,cost_rect)

def display_score():
    money_box = score_font.render(f'{money}', True, white)
    money_rect = money_box.get_rect(center = (50,50))
    screen.blit(money_box,money_rect)
    cps_box = score_font.render(f'{passive_cps} CPS', True, white)
    cps_rect = cps_box.get_rect(center = (430,50))
    screen.blit(cps_box,cps_rect)

def calculate_citruses():
    global money, passive_cps, farmers, lemon, orange, grapefruit, lime
    passive_cps = (((farmers)*2**farmer_upg) + ((lemon*5)*2**lemon_upg) + ((orange*15)*2**orange_upg) + ((grapefruit*40)*2**grapefruit_upg) + ((lime*100)*2**lime_upg))*2**gouging_upg
    money += (passive_cps)

def calculate_click_value():
    global active_cps
    active_cps = (1*2**bigger_upg)*3**fat_upg

pygame.init()
screen = pygame.display.set_mode((640,480))
pygame.display.set_caption('Citrus Clicker')
clock = pygame.time.Clock()
score_font = pygame.font.Font('font/Pixeltype.ttf', 35)
cost_font = pygame.font.Font('font/Pixeltype.ttf', 25)
game_active = True

#Modifiable Global Variables
frame = 0
money = 0
passive_cps = 0
active_cps = 1

farmers = 0
lemon = 0
orange = 0
grapefruit = 0
lime = 0

farmer_upg = 0
lemon_upg = 0
orange_upg = 0
grapefruit_upg = 0
lime_upg = 0
bigger_upg = 0
fat_upg = 0
gouging_upg = 0

oranges = pygame.sprite.GroupSingle()
oranges.add(Clicker())

generators = pygame.sprite.Group()
generators.add(Generator_Button(25,1.15,0,0,384),Generator_Button(100,1.15,1,96,384),Generator_Button(350,1.15,2,192,384),Generator_Button(1000,1.15,3,288,384),Generator_Button(3000,1.15,4,384,384))

upgrades = pygame.sprite.Group()
upgrades.add(Upgrade_Button(150,2.4,0,480,0), Upgrade_Button(350,2.4,1,560,0), Upgrade_Button(600,2.4,2,480,96), Upgrade_Button(1800,2.4,3,560,96), Upgrade_Button(4500,2.4,4,480,192), Upgrade_Button(100,3,5,480,288), Upgrade_Button(650,3,6,560,288), Upgrade_Button(5000,2.4,7,560,192), Upgrade_Button(5000000,2.4,8,480,384))

bg_surface = pygame.image.load('assets/backgroundv2.jpg').convert()
win_surface = pygame.image.load('assets/win_screen.jpg').convert()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        
    if game_active:   
        screen.blit(bg_surface,(0,0))
        display_score()
        oranges.draw(screen)
        generators.draw(screen)
        upgrades.draw(screen)
        oranges.update()
        generators.update()
        upgrades.update()
        calculate_click_value()
        if(frame % 60 == 0):
            calculate_citruses()                
        #print(clicking)
    else:
        screen.fill((255,165,0))
        screen.blit(win_surface,(0,0))

    pygame.display.update()
    clock.tick(60)
    frame += 1




