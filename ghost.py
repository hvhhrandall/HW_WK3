import time
import sys
import random

g_forest = 10
g_turn = 1
g_difficulty = 1
g_hit = 5
g_health = 100
g_gold = 10
g_wallet = 0
g_direction = 0
g_last_direction = 0


def initalize_game():
    
    input_flag = False
    
    print "Welcome to Ghostly Grove. \n", "Please enter a difficulty rating from 1-10.\n"
    
    while(input_flag == False):
        
        g_difficulty = input("Difficulty: ")
        
        if g_difficulty <1 or g_difficulty >10:
            print "Invalid input angers the spooky spectres \n"
            
        else:
            input_flag = True
    
    return g_forest * g_difficulty
    
    
def tutorial():
    print "Lone adventurer, you fell asleep in a strange forest. Now that you are awake"
    print "you see that night has fallen and you are lost in this Ghostly Grove."
    print "Use the cardinal directions to blindly stumble your way out, hopefully you can survive whatever you encounter here. \n"
        

def input_direction():
    input_flag = False
    
    print "Please enter 1, 2, 3, or 4 to choose a direction. \n"
    
    while(input_flag == False):
        g_direction = input("Direction: ")
        
        if g_direction == 1 or 2 or 3 or 4:
            input_flag = True
       
        else:
            print "Invalid input angers the spookie spectres."

    return g_direction
    

def player_turn():
    
    g_direction = input_direction()
    
    if g_direction == g_last_direction:
        dice = random.randomint(1,4)
        if dice == 1:
            print "Back-tracking is risky, but this time it seems to be clear. \n"
            
        elif dice == 2:
            print "Back-tracking is risky, but you found some gold that you missed! \n"
            g_wallet = g_wallet + g_gold
            
        else: 
            print "You just came from there, and the spooky spectre that was following you attacked!"
            print "Health -5 \n"
            g_health = g_health - g_hit
    
    else:
        dice = random.randomint(1,10)
        if dice <= 3:
            print "You've been attacked by a spookie spectre!"
            print "Health -5 \n"
            g_health = g_health - g_hit
        
        elif dice == 4 or 5:
            print "You hear a startling noise ahead, better wait for it to pass. \n"
            for index in range(1,10):
                print "*********** \n"
                time.sleep(1)
                
        elif dice == 6 or 7:
            print "You found a clearing with some gold on the ground. How lucky! \n"
            g_wallet = g_wallet + g_gold
            
        else:
            print "You seem to be moving in the right direction. \n"
    
    g_forest = g_forest - g_turn
    
    g_last_direction = g_direction
    

    
    print "============================================================================ \n"
    print "Health: ", g_health, "Gold: ", g_wallet, "Turns Remaining: ", g_forest, "\n"
    print "============================================================================ \n"
    
    
            
        
    


g_forest = initalize_game()

tutorial()

while(True):
    
    player_turn()
    
    if g_health == 0:
        print "You have become a spooky spectre. Game Over \n"
        break
    
    if g_forest == 0:
        print "Congratulations, you made it out of the Ghost Grove! \n"
        break





    

