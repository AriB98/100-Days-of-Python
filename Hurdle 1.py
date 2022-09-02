def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump_hurdle():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    
for i in range(1,7):
    jump_hurdle()
    
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
