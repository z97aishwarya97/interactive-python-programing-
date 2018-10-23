# implementation of card game - Memory
#import modules
import simplegui
import random

# helper function to initialize globals
def new_game():    
    global list, exposed, state, turns
    turns = 0
    list = [i%8 for i in range(16)]
    random.shuffle(list)
    exposed = [False for i in range (16)]
    state = 0 
    label.set_text("Turns = 0")
    pass  

     
# define event handlers
def mouseclick(pos):
    # add game state logic here
    global state, exposed, click1, click2, turns, list 
    choice = int(pos[0] / 50)
    if state == 0:
        state = 1
        click1 = choice
        exposed[click1] = True
    elif state == 1:
        if not exposed[choice]:
            state = 2
            click2 = choice
            exposed[click2] = True
            turns += 1
    elif state == 2:
        if not exposed[choice]:
            if list[click1] == list[click2]:
                pass
            else:
                exposed[click1] = False
                exposed[click2] = False
            click1 = choice
            exposed[click1] = True
            state = 1       
    label.set_text("Turns = " + str(turns))
                  
    pass
    
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    for i in range (16):
        if exposed[i]:
            canvas.draw_text(str(list[i]), (50*i+10, 60), 40, "white")
        else:
            canvas.draw_polygon([(50*i, 0), (50*i, 100), (50*i + 50, 0), (50*i + 50, 100)], 2, "black", "teal")
    pass


# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label('Turns = 0')

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric