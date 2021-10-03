from pico2d import *

open_canvas()

background = load_image('Background.png')
character = load_image('Mario.png')

# clip_draw(
character.clip_draw(50, 50)
background.draw_now(0, 0)

delay(10)