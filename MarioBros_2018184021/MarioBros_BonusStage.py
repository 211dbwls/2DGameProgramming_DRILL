from pico2d import *

import game_framework
import game_world

import MarioBros_Stage1

from MarioBros_BonusStage_Background import *

from MarioBros_BonusStage_Pipe import *
from MarioBros_BonusStage_Brick import *

from MarioBros_BonusStage_Coin import *

from MarioBros_Mario import *
from MarioBros_Mario_FireBall import *

name = "MarioBros_BonusStage"

STAGE_WIDTH, STAGE_HEIGHT = 800, 600
# 변수 ------------------------------------------------------------------------------------------------------------------
background = None
collision_grounds = []
grounds = []

lpipe = None
brick = None

coins = []

mario = None


# 함수 -----------------------------------------------------------------------------------------------------------------
def collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    # 충돌이 안 일어나는 상황을 먼저 체크
    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False

    return True

def enter():
    global background, collision_grounds, grounds
    global lpipe, brick
    global coins
    global mario

    # initialization code : 초기화
    background = Background()  # 배경 생성
    collision_grounds = [Ground(392, 1112, 16, 17, 24 + 16 * i, 5 + 34)for i in range(0, 48)]
    grounds = [Ground(392, 1112, 16, 17, 24 + 16 * i, 5)for i in range(0, 48)] \
              + [Ground(392, 1112, 16, 17, 24 + 16 * i, 5 + 17)for i in range(0, 48)]

    lpipe = LPipe(50, 500, 100, 130, 750, 110)  # 파이프 생성
    brick = Brick()  # 벽돌 생성

    coins = [Coin(120, 0, 30, 30, 260 + 30 * i, 140) for i in range(0, 11)] \
        + [Coin(120, 0, 30, 30, 260 + 30 * i, 140 + 30) for i in range(0, 11)] \
        + [Coin(120, 0, 30, 30,  260 + 30 * i + 30, 140 + 60) for i in range(0, 9)]  # 코인 생성

    mario = Mario(90, 60)  # 캐릭터 생성

    game_world.add_object(background, 0)
    for collision_ground in collision_grounds:
        game_world.add_object(collision_ground, 0)
    for ground in grounds:
        game_world.add_object(ground, 0)

    game_world.add_object(lpipe, 0)
    game_world.add_object(brick, 0)

    for coin in coins:
        game_world.add_object(coin, 0)

    game_world.add_object(mario, 1)


def exit():
    game_world.clear()

def update():
    for game_object in game_world.all_objects():
        game_object.update()

    # 충돌 체크 및 충돌 처리
    # 마리오 - 땅
    ground_collision = False
    for collision_ground in collision_grounds:
        if collide(collision_ground, mario):
            ground_collision = True
    if ground_collision == True:
        mario.stop()
    else:
        mario.fall()

    # 마리오 - 코인
    for coin in coins:
        if collide(coin, mario):  # 코인과 충돌했을 경우
            mario.addCoin()  # 획득 코인 수 추가
            mario.addScore(200)  # 점수 추가
            coins.remove(coin)  # 코인 충돌 검사하는 리스트에서 제거
            game_world.remove_object(coin)  # 충돌한 코인 삭제

    # 마리오 - 파이프
    if collide(lpipe, mario):  # 파이프와 충돌했을 경우
        from MarioBros_Mario import Mario_in_BonusStage
        global Mario_in_BonusStage
        Mario_in_BonusStage = False
        game_framework.change_state(MarioBros_Stage1)  # stage1으로 이동

def draw():
    clear_canvas()

    for game_object in game_world.all_objects():
        game_object.draw()

    font = load_font('SuperMario256.ttf', 16)
    numfont = load_font('SuperMario256.ttf', 18)

    from MarioBros_Mario import Mario_score
    font.draw(30, 570, 'MARIO', (255, 255, 255))
    numfont.draw(100, 570, '%06d' % Mario_score, (255, 255, 255))

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
        else:
            mario.handle_event(event)


