import game_framework
from pico2d import *

name = "MarioBros_StartState"
image_back = None
image_logo = None
logo_time = 0.0

def enter():
    global image_back
    global image_logo

    image_back = load_image('WhiteBack.png')
    image_logo = load_image('StartLogo.png')

def exit():
    global image_back
    global image_logo

    del(image_back)
    del(image_logo)

def update():
    global logo_time

    if(logo_time > 1.0):
        logo_time = 0
        game_framework.quit()
    delay(0.01)
    logo_time += 0.01

def draw():
    global image_back
    global image_logo

    clear_canvas()
    image_back.draw(400, 300)
    image_logo.draw(400, 300)
    update_canvas()

def handle_events():
    events = get_events()
    pass
