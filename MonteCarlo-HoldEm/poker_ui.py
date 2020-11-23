import pygame
import pathlib
import sys
from poker_game import *
'''
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
    K_0,
    K_1,
    K_2,
    K_3,
    K_4,
    K_5,
    K_6,
    K_7,
    K_8,
    K_9,
    K_RETURN
)
'''
pygame.init()

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
font_title = pygame.font.SysFont("Comic Sans MS", 50)
font_heading_1 = pygame.font.SysFont("Lucida Console", 40)
font_heading_2 = pygame.font.SysFont("Trebuchet MS", 40)
font_body_1 = pygame.font.SysFont("Microsoft Sans Serif", 20)
font_body_2 = pygame.font.SysFont("Courier New", 20)
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
working_directory = pathlib.Path().absolute()
print(working_directory)

#https://stackoverflow.com/questions/37420908/how-to-centre-an-image-in-pygame
sprite_library = {}
def get_sprite(filename):
    sprite = sprite_library.get(filename)
    if sprite == None:
            sprite = pygame.sprite.load(working_directory + "\Sprites\\" + filename)
            sprite_library[filename] = sprite
    return sprite

def in_game(player_count):
    players = []
    for i in range(player_count):
        players.append(Player(100))

    for event in pygame.event.get():
        
    text_surf = font_title.render("!!! WELCOME to BLACKJACK !!!", False, (black))
    screen.blit(text_surf, (SCREEN_WIDTH-text_surf.get_width()/2, SCREEN_WIDTH-text_surf.get_height()/2))
    pygame.display.flip()
    
    return False



running = True

#main menu
while running:
    screen.fill(green)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        #need to build buttons which get response
        elif event.type == pygame.MOUSEBUTTONDOWN:
            #game returns true when returning to main menu, false when quitting, pass in players
            if in_game(2):
                pass
            else:
                running = False
    text_surf = font_title.render("!!! WELCOME to BLACKJACK !!!", False, (black))
    screen.blit(text_surf, (SCREEN_WIDTH-text_surf.get_width()/2, SCREEN_WIDTH-text_surf.get_height()/2))
    pygame.display.flip()
    clock.tick(60)

screen.fill(green)
text_surf = font_title.render("Bye", False, (black))
screen.blit(text_surf, (0, 0))
pygame.display.flip()
pygame.time.delay(1000)