import time
import sys
import random

g_forest = 10
g_turn = 1
g_hit = 5
g_health = 100
g_gold = 10
g_wallet = 0
g_direction = 0
g_last_direction = 0
random.seed(time.clock())

def initalize_game(forest):
    
    input_flag = False
    
    print "Welcome to Ghostly Grove. \n", "Please enter a difficulty rating from 1-10.\n"
    
    while(input_flag == False):
        
        difficulty = input("Difficulty: ")
        
        if difficulty <1 or difficulty >10:
            print "Invalid input angers the spooky spectres \n"
            
        else:
            input_flag = True
    
    return forest * difficulty
    
    
def tutorial():
    print "Lone adventurer, you fell asleep in a strange forest. Now that you are awake"
    print "you see that night has fallen and you are lost in this Ghostly Grove."
    print "Use the cardinal directions to blindly stumble your way out, hopefully you can survive whatever you encounter here. \n"
        

def input_direction():
    input_flag = False
    
    print "Please enter 1, 2, 3, or 4 to choose a direction. \n"
    
    while(input_flag == False):
        g_direction = input("Direction: ")
        
        if g_direction == 1 or g_direction == 2 or g_direction == 3 or g_direction == 4:
            input_flag = True
       
        else:
            print "Invalid input angers the spookie spectres."

    return g_direction
    

def player_turn(last_direction, forest, health, wallet, hit, gold, turn):
    
    global g_last_direction
    
    direction = input_direction()
    
    if direction == last_direction:
        dice = random.randint(1,4)
        if dice == 1:
            print "Back-tracking is risky, but this time it seems to be clear. \n"
            
        elif dice == 2:
            print "Back-tracking is risky, but you found some gold that you missed! \n"
            wallet = wallet + gold
            
        else: 
            print "You just came from there, and the spooky spectre that was following you attacked!"
            print "Health -5 \n"
            health = health - hit
    
    else:
        dice = random.randint(1,10)
        if dice <= 3:
            print "You've been attacked by a spookie spectre!"
            print "Health -5 \n"
            health = health - hit
        
        elif dice == 4 or 5:
            print "You hear a startling noise ahead, better wait for it to pass. \n"
            for index in range(1,10):
                print "*********** \n"
                time.sleep(1)
                
        elif dice == 6 or 7:
            print "You found a clearing with some gold on the ground. How lucky! \n"
            wallet = wallet + gold
            
        else:
            print "You seem to be moving in the right direction. \n"
    
    forest = forest - turn
    
    g_last_direction = direction
    

    
    print "============================================================================ \n"
    print "Health:", health, "Gold:", wallet, "Turns Remaining:", forest, "\n"
    print "============================================================================ \n"
    
    
            
        
    


g_forest = initalize_game(g_forest)

print g_forest

tutorial()

while(True):
    
    player_turn(g_last_direction, g_forest, g_health, g_wallet, g_hit, g_gold, g_turn)
    
    if g_health == 0:
        print "You have become a spooky spectre. Game Over \n"
        break
    
    if  g_forest == 0:
        print "Congratulations, you made it out of the Ghost Grove! \n"
        break





    

