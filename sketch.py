from microbit import *

x, y = 0, 0

def move():
    global x, y
    x += 1
    if x == 5:
        x, y = 0, y+1
    if y == 5:
        y = 0

pixel = 0
while True:
    if button_a.was_pressed():
        display.set_pixel(x, y, pixel)
        move()
        pixel = display.get_pixel(x, y)

    if button_b.was_pressed():
        if pixel == 9:
            display.set_pixel(x, y, 0)
        else:
            display.set_pixel(x, y, 9)
            
        move()
        pixel = display.get_pixel(x, y)
    
    display.set_pixel(x, y, 9)
    sleep(200)
    display.set_pixel(x, y, 0)
    sleep(200)
