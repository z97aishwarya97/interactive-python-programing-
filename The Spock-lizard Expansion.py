# Rock-paper-scissors-lizard-Spock template
# Greetings!

# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions

def name_to_number(name):
    if name == "rock":
        return 0
    elif name == "Spock":
        return 1
    elif name == "paper":
        return 2
    elif name == "lizard":
        return 3
    elif name == "scissors":
        return 4
    else:
        return "Error Error Error"
    

def number_to_name(number):
     if number == 0:
        return "rock"
     elif number == 1:
        return "Spock"
     elif number == 2:
        return "paper"
     elif number == 3:
        return "lizard"
     elif number == 4:
        return "scissors"
     else:
        return "Error Error Error"
    
    
    # convert number to a name using if/elif/else
    # don't forget to return the result!
    
import random
def rpsls(player_choice):
    player_number = name_to_number(player_choice)
    comp_number = random.randrange(0, 5)
    difference = (player_number - comp_number) % 5
    
    #To convert the answer which is a number to the corresponding name
    
    print "Player chooses", number_to_name (player_number)
    print "Computer chooses", number_to_name (comp_number)
    if difference == 0:
        print "Player and Computer tie!"
    elif difference == 1:
        print "Player Wins!"
    elif difference == 2:
        print "Player Wins!"
    else:
        print "Computer Wins!"
    return ""
    
    # print a blank line to separate consecutive games

    # print out the message for the player's choice

    # convert the player's choice to player_number using the function name_to_number()

    # compute random guess for comp_number using random.randrange()

    # convert comp_number to comp_choice using the function number_to_name()
    
    # print out the message for computer's choice

    # compute difference of comp_number and player_number modulo five

    # use if/elif/else to determine winner, print winner message

    
# test your code - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE
# to test code use format print rpsls("your_choice")


