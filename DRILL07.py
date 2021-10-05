import random

from pico2d import *


KPU_WIDTH, KPU_HEIGHT = 1280, 1024

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

def hand_random():
    global randomx, randomy
    randomx = random.randint(0, 1280)
    randomy = random.randint(0, 1024)

def charceter_move():
    global x, y
    x, y = randomx, KPU_HEIGHT - 1 - randomy

open_canvas(KPU_WIDTH, KPU_HEIGHT)

kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')
hand = load_image('hand_arrow.png')

running = True
x, y = KPU_WIDTH // 2, KPU_HEIGHT // 2
frame = 0

hand_random()

while running:
    clear_canvas()
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)

    if x != randomx and y != randomy:
        charceter_move()
    else:
        hand_random()

    character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
    hand.draw(randomx, randomy)

    update_canvas()
    frame = (frame + 1) % 8

    handle_events()

close_canvas()




