from pico2d import *
import math

def draw(x, y):
    clear_canvas_now()
    grass.draw_now(400, 30)
    character.draw_now(x, y)


def rect(x, y):
    while x < 750 and y == 90:
        draw(x, y)
        x += 2
        delay(0.01)
    while x == 750 and y < 550:
        draw(x, y)
        y += 2
        delay(0.01)
    while x > 10 and y == 550:
        draw(x, y)
        x -= 2
        delay(0.01)
    while x == 10 and y > 90:
        draw(x, y)
        y -= 2
        delay(0.01)
    while x < 400 and y == 90:
        draw(x, y)
        x += 2
        delay(0.01)

def circle(a, b, r):
    for ang in range(-90, 270):
        x = a + r * math.cos(2 * math.pi / 360 * ang)
        y = b + r * math.sin(2 * math.pi / 360 * ang)
        draw(x, y)
        ang += 2
        delay(0.02)

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

x = 400
y = 90
r = 200

while True:
    rect(x, y)
    circle(400, 290, r)
        
