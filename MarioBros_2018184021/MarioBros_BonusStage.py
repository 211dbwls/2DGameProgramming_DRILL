from pico2d import *

import game_framework
import MarioBros_Stage1

from MarioBros_BonusStage_Background import *

from MarioBros_BonusStage_Pipe import *
from MarioBros_BonusStage_Brick import *

from MarioBros_BonusStage_Coin import *

from MarioBros_Mario import *

name = "MarioBros_BonusStage"

STAGE_WIDTH, STAGE_HEIGHT = 800, 600
# 변수 ------------------------------------------------------------------------------------------------------------------
background = None
ground = None

lpipe = None
brick = None

coin = None

mario = None

# 함수 -----------------------------------------------------------------------------------------------------------------
def enter():
    global background, ground
    global lpipe, brick
    global coin
    global mario

    # initialization code : 초기화
    background = Background()  # 배경 생성
    ground = Ground()  # 땅 생성

    lpipe = LPipe()  # 파이프 생성
    brick = Brick()  # 벽돌 생성

    coin = Coin()  # 코인 생성

    mario = Mario(90, 60)  # 캐릭터 생성


def exit():
    global background, ground
    global lpipe, brick
    global coin
    global mario

    del (background)
    del (ground)

    del (lpipe)
    del (brick)

    del (coin)

    del (mario)

def update():
    mario.update()

    coin.update()

def draw():
    clear_canvas()

    background.draw()
    ground.draw()

    lpipe.draw()
    brick.draw()

    coin.draw()

    mario.draw()

    font = load_font('SuperMario256.ttf', 16)
    numfont = load_font('SuperMario256.ttf', 18)

    font.draw(30, 570, 'MARIO', (255, 255, 255))

    numfont.draw(100, 570, '000000', (255, 255, 255))

    numfont.draw(405, 569, 'x', (255, 255, 255))
    numfont.draw(420, 569, '00', (255, 255, 255))

    font.draw(660, 570, 'TIME', (255, 255, 255))
    numfont.draw(720, 570, '%3.0f' % (400 - get_time()), (255, 255, 255))

    update_canvas()
    delay(0.07)

def handle_events():  # 입력처리
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:  # 종료 버튼
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:  # esc키
            game_framework.change_state(MarioBros_Stage1)  # 이전 화면으로 이동
        else:
            mario.handle_events(event)


