from pico2d import *

import game_framework
import MarioBros_Stage1

from MarioBros_BossStage_Background import *

from MarioBros_BossStage_Coin import *

from MarioBros_Enemies_Boss import *

from MarioBros_Mario import *
from MarioBros_Mario_FireBall import *

name = "MarioBros_BossStage"

STAGE_WIDTH, STAGE_HEIGHT = 800, 600
# 변수 ------------------------------------------------------------------------------------------------------------------
background = None
ground = None
fireground = None
bridgeground = None

brick = None

coin = None

boss = None

mario = None

# 함수 -----------------------------------------------------------------------------------------------------------------
def enter():
    global background, ground, fireground, bridgeground
    global brick
    global coin
    global boss
    global mario

    # initialization code : 초기화
    background = Background()  # 배경 생성
    ground = Ground()  # 땅 생성
    fireground = FireGround()  # 불 생성
    bridgeground = BridgeGround()  # 다리 생성

    brick = Brick()  # 벽돌 생성

    coin = Coin()  # 코인 생성

    boss = Boss()  # 보스 생성

    mario = Mario(30, 228)  # 캐릭터 생성

def exit():
    global background, ground, fireground, bridgeground
    global brick
    global coin
    global boss
    global mario

    del (background)
    del (ground)
    del (fireground)
    del (bridgeground)

    del (brick)

    del (coin)

    del (boss)

    del (mario)

def update():
    mario.update()

    coin.update()

    boss.update()

def draw():
    clear_canvas()

    background.draw()
    fireground.draw()
    ground.draw()
    bridgeground.draw()

    brick.draw()

    coin.draw()

    boss.draw()

    mario.draw()

    font = load_font('SuperMario256.ttf', 16)
    numfont = load_font('SuperMario256.ttf', 18)

    from MarioBros_Mario import Mario_score, Mario_life
    font.draw(30, 570, 'MARIO', (255, 255, 255))
    numfont.draw(100, 570, '%06d' % Mario_score, (255, 255, 255))
    numfont.draw(100, 550, 'x', (255, 255, 255))
    numfont.draw(115, 550, '%02d' % Mario_life, (255, 255, 255))

    from MarioBros_Mario import Mario_coins
    numfont.draw(405, 569, 'x', (255, 255, 255))
    numfont.draw(420, 569, '%02d' % Mario_coins, (255, 255, 255))

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

