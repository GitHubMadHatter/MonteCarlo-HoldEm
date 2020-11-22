#Initialising
import random
import pygame

pygame.init()
#pygame.font.init()
my_font = pygame.font.SysFont("Comic Sans MS", 30)

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

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

#Need cards with values, could have used a dict or list but wanted to try creating a deck in python
class Card:
    def __init__(self, num, suit):
        self.suit = suit
        self.num = num
        self.id = str(num) + suit[0]
        if num > 10:
            self.val = 10
        else:
            self.val = num
    def __str__(self):
        if self.num == 1:
            return 'Ace' + ' of ' + self.suit
        if self.num == 11:
            return 'Jack' + ' of ' + self.suit
        if self.num == 12:
            return 'Queen' + ' of ' + self.suit
        if self.num == 13:
            return 'King' + ' of ' + self.suit
        return str(self.num) + ' of ' + self.suit

#Making it easier to centre text and just update the screen
#-1 means centred, -2 means first third, -3 means last third
def updateScreen(surf, x_coord, y_coord):
    if x_coord == (-1):
        x_coord = (SCREEN_WIDTH-surf.get_width())/2
    elif x_coord == (-2):
        x_coord = (SCREEN_WIDTH-surf.get_width())/3
    elif x_coord == (-3):
        x_coord = ((SCREEN_WIDTH-surf.get_width())/3) * 2
        
    if y_coord == (-1):
        y_coord = (SCREEN_HEIGHT-surf.get_height())/2
    elif y_coord == (-2):
        y_coord = (SCREEN_WIDTH-surf.get_width())/3
    elif y_coord == (-3):
        y_coord = ((SCREEN_WIDTH-surf.get_width())/3) * 2
    print(x_coord, y_coord)

    screen.blit(surf, (x_coord, y_coord))
    pygame.display.flip()

#implemented list comprehension
suits = ["Hearts","Diamonds","Spades","Clubs"]
deck = [Card(i,j) for i in range(1, 14) for j in suits]

for item in deck:
    print(item)

running = True
updateScreen(my_font.render("!!! WELCOME to BLACKJACK !!!", False, (255,255,255)), -2, -2)

#game loop
while running:
    players = 1 #int(input("\nHow many players? "))
    totals = []
    random.shuffle(deck)
    cur_card = 0

    for event in pygame.event.get():
        if event.type == KEYDOWN:
            # If the Esc key is pressed, then exit the main loop
            if event.key == K_ESCAPE:
                running = False
        # Check for QUIT event. If QUIT, then set running to false.
        elif event.type == QUIT:
            running = False

    #Each players turn
    for i in range(players):
        print(f"\nPlayer {i+1} hand: ")
        total = 0
        total_cards = 0
        ace_flag = False

        #first two cards
        
        print(deck[cur_card])
        #aces can be 1 or 11, add 11 if possible otherwise add 1
        if deck[cur_card].num == 1 and total + 11 <= 21:
            total += 11
            ace_flag = True
        else:
            total += deck[cur_card].val
        cur_card += 1
        total_cards += 1
        print(deck[cur_card])
        #aces can be 1 or 11, add 11 if possible otherwise add 1
        if deck[cur_card].num == 1 and total + 11 <= 21:
            total += 11
            ace_flag = True
        else:
            total += deck[cur_card].val
        cur_card += 1
        total_cards += 1

        #while hand is legal (<= 21) and not finished (21 is highest legal so no reason to hit; if you have 5 cards and are under 21 you win), allow the player to hit or stand
        while total < 21 and total_cards < 5 and input(f"Your total: {total}, hit? ") == "y":
            print(deck[cur_card])

            #aces can be 1 or 11, add 11 if possible otherwise add 1
            if deck[cur_card].num == 1 and total + 11 <= 21:
                total += 11
                ace_flag = True
            else:
                total += deck[cur_card].val
            
            #If the hand is bust but a previous card is an ace (11) make it 1 now as that is favourable
            if ace_flag == True and total > 21:
                total -= 10
                ace_flag = False

            cur_card += 1
            total_cards += 1

        #turn end
        if total > 21:
            print(f"Bust! ({total})")
            totals.append(total)

        elif total_cards > 4:
            print("5 and under!")
            #number that is bigger than max possible hand value (30)
            totals.append(45)

        elif total < 21:
            print(f"Total: {total}")
            totals.append(total)

        elif total == 21:
            print("Blackjack!")
            totals.append(total)
        
    #results
    print("\nResults:")
    p = 0
    while p < len(totals):
        if totals[p] > 40:
            print(f"Player {p + 1}: 5 and under ({totals[p]})", end = "")
        else:
            print(f"Player {p + 1}: {totals[p]}", end = "")

        if totals[p] == max(totals) and (totals[p] <= 21 or totals[p] > 40):
            print("\t! Winner !")
        else:
            print()
        p += 1
    

    

    
