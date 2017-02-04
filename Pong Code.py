# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True
INC = 4

# initialize ball_pos and ball_vel for new bal in middle of table
ball_pos = [WIDTH / 2, HEIGHT / 2]
ball_vel = [1, 2]

# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = [WIDTH / 2, HEIGHT / 2]
    ball_vel = [1, -2]
    if direction == True :
        ball_vel[0] = random.randrange(2, 4)
        ball_vel[1] = - random.randrange(1, 3)
    elif direction == False :
        ball_vel[0] = - random.randrange(2, 4)
        ball_vel[1] = - random.randrange(1, 3)
    

# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    #spawn_ball()
    spawn_ball(LEFT)
    paddle1_pos = HEIGHT / 2
    paddle2_pos = HEIGHT / 2
    paddle1_vel = 0
    paddle2_vel = 0
    score1 = 0
    score2 = 0
    
   
def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
 
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # update ball
    if ball_pos[1] <= BALL_RADIUS :
        ball_vel[1] = - ball_vel[1] 
        
    elif ball_pos[1] >= (HEIGHT - 1) - BALL_RADIUS :
        ball_vel[1] = - ball_vel[1]
        
    if ball_pos[0] <= BALL_RADIUS + PAD_WIDTH :
        if paddle1_pos - HALF_PAD_HEIGHT <= ball_pos[1] <= paddle1_pos + HALF_PAD_HEIGHT:
            ball_vel[0] = - ball_vel[0]
            ball_vel[0] += (0.1 * ball_vel[0])
        else:
            spawn_ball(RIGHT)
            score2 += 1
     
    elif ball_pos[0] >= (WIDTH - 1) - BALL_RADIUS - PAD_WIDTH :
        if paddle2_pos - HALF_PAD_HEIGHT <= ball_pos[1] <= paddle2_pos + HALF_PAD_HEIGHT:
            ball_vel[0] = - ball_vel[0]
            ball_vel[0] += (0.1 * ball_vel[0])
        else:
            spawn_ball(LEFT)
            score1 += 1

    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    
    # draw ball
    canvas.draw_circle((ball_pos[0], ball_pos[1]), BALL_RADIUS, 2, "Silver", "Silver")
    
    # update paddle's vertical position, keep paddle on the screen
    if paddle1_vel < 0:
        if paddle1_pos <= HALF_PAD_HEIGHT:
            paddle1_pos = HALF_PAD_HEIGHT
        paddle1_pos += paddle1_vel    
    elif paddle1_vel >= 0:
        if (HEIGHT - paddle1_pos) <= HALF_PAD_HEIGHT:
            paddle1_pos = HEIGHT - HALF_PAD_HEIGHT
        paddle1_pos += paddle1_vel    
        
    if paddle2_vel < 0:
        if paddle2_pos <= HALF_PAD_HEIGHT:
            paddle2_pos = HALF_PAD_HEIGHT
        paddle2_pos += paddle2_vel
    elif paddle2_vel >= 0:
        if (HEIGHT - paddle2_pos) <= HALF_PAD_HEIGHT:
            paddle2_pos = HEIGHT - HALF_PAD_HEIGHT
        paddle2_pos += paddle2_vel    
            
    
    # draw paddles
    canvas.draw_polygon([(0, paddle1_pos - HALF_PAD_HEIGHT), 
                         (PAD_WIDTH, paddle1_pos - HALF_PAD_HEIGHT),
                         (PAD_WIDTH, paddle1_pos + HALF_PAD_HEIGHT),
                         (0, paddle1_pos + HALF_PAD_HEIGHT)], 2, "Teal", "Teal")
    
    canvas.draw_polygon([(WIDTH, paddle2_pos - HALF_PAD_HEIGHT), 
                         (WIDTH, paddle2_pos + HALF_PAD_HEIGHT), 
                         (WIDTH - PAD_WIDTH, paddle2_pos + HALF_PAD_HEIGHT),
                         (WIDTH - PAD_WIDTH, paddle2_pos - HALF_PAD_HEIGHT)], 2, "Teal", "Teal")
    
 
    # draw scores
    canvas.draw_text(str(score1), [130, 70], 40, "Orange")
    canvas.draw_text(str(score2), [430, 70], 40, "Orange")
    
def keydown(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP['w']:
        paddle1_vel = -INC
    if key == simplegui.KEY_MAP['s']:
        paddle1_vel = INC
    elif key == simplegui.KEY_MAP['up']:
        paddle2_vel = -INC
    elif key == simplegui.KEY_MAP['down']:
        paddle2_vel = INC
   
def keyup(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP['w'] or key == simplegui.KEY_MAP['s']:
        paddle1_vel = 0
    elif key == simplegui.KEY_MAP['up'] or key == simplegui.KEY_MAP['down']:
        paddle2_vel = 0    
    

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("New Game", new_game, 110)


# start frame
new_game()
frame.start()