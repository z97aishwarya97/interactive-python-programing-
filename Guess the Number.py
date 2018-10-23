# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

#MAY THE FORCE BE WITH YOU

#import all the necessary modules
import simplegui
import random
import math

# initialize global variables used in your code
num_range = 100
secretno = 0
user_guess = 0
num_guesses = 7

# helper function to start and restart the game
def new_game():
    global secretno, num_range, num_guesses
    secretno = random.randrange(0, num_range)
    
    # setting range
    if num_range == 100:
        num_guesses = 7
    elif num_range == 1000:
        num_guesses = 10
    else:
        print "Please choose a range."
    
    # to display starting a new game
    print ""
    print "A new game has started! Range is from 0 to " + str(num_range)
    print "You have " + str(num_guesses) + " guesses "

# helper function for number of guesses
def decrement_guesses():
    global num_guesses
    num_guesses = num_guesses - 1
    if num_guesses > 0:
        print "Remaining guesses: " + str(num_guesses)
    else:
        print "Wrong guess, you have turned to the Dark Side! The number was " + str(secretno) + "."
        new_game()

# define event handlers for control panel
def range100():
    # button that changes range to range [0,100) and restarts
    global num_range
    num_range = 100
    new_game()

def range1000():
    # button that changes range to range [0,1000) and restarts
    global num_range
    num_range = 1000
    new_game()
    
def input_guess(guess):
    ## Compares the user's guess to the secret answer ##
    global secret, user_guess
    user_guess = int(guess)
    print ""
    if user_guess == secretno:
        print "Your guess was " + str(user_guess)
        print "Correct! The Force is strong with this one!"
        new_game()
    elif user_guess > secretno:
        print "Your guess was " + str(user_guess)
        print "Go lower!"
    elif user_guess < secretno:
        print "Your guess was " + str(user_guess)
        print "Go higher!"
    else:
        print "Something went terribly wrong!"
    decrement_guesses()
    
# create frame
frame = simplegui.create_frame("Guess the number", 200, 200)


# register event handlers for control elements
frame.add_button('Range [0, 100]', range100, 200)
frame.add_button('Range [0, 1000]', range1000, 200)

frame.add_input('Enter your guess below!', input_guess, 100)

# call new_game and start frame
new_game()
frame.start()


