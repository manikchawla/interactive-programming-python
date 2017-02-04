# template for "Stopwatch: The Game"
import simplegui

# define global variables
time = 0
no_of_success = 0
no_of_stops = 0
run_check = False

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    if t <= 99:
        return str(0) + ":" + str(0) + str(t / 10) + "." + str(t % 10)
    elif (t > 99) and (t <= 599):
        return str(0) + ":" + str(t / 10) + "." + str(t % 10)
    elif (t > 599):
        if (t % 600 == 0):
            return str(t/600) + ":" + str(0) + str(0) + "." + str(t % 10)
        elif (t < 999):
            a = t - (600 *(t/600))
            b = a / 10
            return str(t/600) + ":" + str(0) + str(b) + "." + str(t % 10)
        else:
            a = t - (600 *(t/600))
            b = a / 10
            return str(t/600) + ":" + str(b) + "." + str(t % 10)
    
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start_handler():
    global run_check
    timer.start()
    run_check = True
def stop_handler():
    global no_of_stops, no_of_success, run_check
    if(run_check == True):
        no_of_stops += 1
        if(time % 10 == 0):
            no_of_success += 1
    run_check = False
    timer.stop()
def reset_handler():
    global time, run_check, no_of_stops, no_of_success
    no_of_success = 0
    no_of_stops = 0
    timer.stop()
    time = 0
    

# define event handler for timer with 0.1 sec interval
def timer_handler():
    global time
    time += 1

# define draw handler
def draw_handler(canvas):
    canvas.draw_text(format(time), (110,110), 36, "White")
    canvas.draw_text(str(no_of_success) + "/" + str(no_of_stops), (230,30), 30, "Red")
    
# create frame
frame = simplegui.create_frame("Stopwatch",300,200)
timer = simplegui.create_timer(100, timer_handler)

# register event handlers
frame.set_draw_handler(draw_handler)
frame.add_button("Start", start_handler, 50)
frame.add_button("Stop", stop_handler, 50)
frame.add_button("Reset", reset_handler, 50)



# start frame
frame.start()

# Please remember to review the grading rubric
