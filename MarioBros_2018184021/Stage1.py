from pico2d import *


def handle_event():  # 입력처리
    pass


background = load_image('Background.png')
character = load_image('Mario.png')

open_canvas()

background.clip_draw(0, 150, 250, 149, 250 // 2, 149 // 2)

update_canvas()

delay(10)
