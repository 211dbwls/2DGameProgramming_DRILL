import game_framework
import MarioBros_Stage1

from pico2d import *

name = "MarioBros_StartState"
image_back = None
image_title = None
image_cloud = None
image_mountain = None
image_ground = None
image_Mario = None

def enter():
    global image_back
    global image_title
    global image_cloud
    global image_mountain
    global image_ground
    global image_Mario

    image_back = load_image('Back.png')
    image_title = load_image('Start_Title.png')
    image_cloud = load_image('ScenerySprites.gif')
    image_mountain = load_image('ScenerySprites.gif')
    image_ground = load_image('Ground.png')
    image_Mario = load_image('MarioAnimationSheet.png')

def exit():
    global image_back
    global image_title
    global image_cloud
    global image_mountain
    global image_ground
    global image_Mario

    del(image_back)
    del(image_title)
    del (image_cloud)
    del (image_mountain)
    del (image_ground)
    del (image_Mario)


def update():
    pass


def draw():
    global image_back
    global image_title
    global image_cloud
    global image_mountain
    global image_ground
    global image_Mario

    clear_canvas()

    image_back.draw(400, 300)
    image_cloud.clip_draw(140, 850, 70, 40, 550, 300)
    image_mountain.clip_draw(80, 900, 90,  60, 200,  60)


    for i in range(0, 3):
        image_ground.clip_draw(2, 155 + 17 * i, 16, 17, 8, 7 + 16 * i)
    x = 8
    for i in range(0, 53):
        x += 15
        for j in range(0, 3):
            image_ground.clip_draw(18, 155 + 17 * j, 16, 17, x, 7 + 16 * j)

    image_Mario.clip_draw(200, 170, 30, 30, 30, 60)

    image_title.draw(400, 400)

    update_canvas()

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
                game_framework.change_state(MarioBros_Stage1)

