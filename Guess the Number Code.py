# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
import simplegui
import math
import random 

num = 7
current_game = 1

# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global current_game
    current_game = 1
    print
    print "New Game. Range is from 0 - 100 "
    print "You have 7 guesses remaining"
    global secret_number
    secret_number = random.randrange(0,100)
    global num
    num = 7
    

def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global current_game
    current_game = 2
    print
    print "New Game. Range is from 0 - 1000 "
    print "You have 10 guesses remaining"
    global secret_number
    secret_number = random.randrange(0,1000)
    global num
    num = 10 
   
    
def input_guess(guess):
    # main game logic goes here
    flag = 0
    print
    player_guess = int(guess)
    print "Guess was", player_guess
    if player_guess < secret_number:
        print "Higher!"
    elif player_guess > secret_number:
        print "Lower!"
    else:
        print "Correct!"
        flag = 1
    global num
    num = num - 1    
    print "You have", num, "guesses remaining"    
    if flag == 1:
        if current_game == 1:
            range100()
        else:
            range1000()
    elif num == 0:
        print "You lost!"
        if current_game == 1:
            range100()
        else:
            range1000()
        

    
# create frame
f = simplegui.create_frame("Guess the number", 200, 200)

# register event handlers for control elements and start frame
f.add_button("Range is [0, 100)", range100, 200)
f.add_button("Range is [0, 1000)", range1000, 200)
f.add_input("Player input", input_guess, 200)
f.start()

# call range100 
range100()


# always remember to check your completed program against the grading rubric
