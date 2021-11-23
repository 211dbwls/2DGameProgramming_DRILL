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

import server
import collision

name = "MarioBros_BonusStage"

STAGE_WIDTH, STAGE_HEIGHT = 800, 600
# 변수 ------------------------------------------------------------------------------------------------------------------

# 함수 -----------------------------------------------------------------------------------------------------------------
def enter():
    # initialization code : 초기화
    server.background = Background()  # 배경 생성
    server.collision_grounds = [Ground(392, 1112, 16, 17, 24 + 16 * i, 5 + 34)for i in range(0, 48)]
    server.grounds = [Ground(392, 1112, 16, 17, 24 + 16 * i, 5)for i in range(0, 48)] \
              + [Ground(392, 1112, 16, 17, 24 + 16 * i, 5 + 17)for i in range(0, 48)]

    server.lpipe = LPipe(50, 500, 100, 130, 750, 110)  # 파이프 생성
    server.bricks = [Brick(393, 1134, 15, 16, 25, 56 + 16 * i) for i in range(0, 30)] \
                    + [Brick(393, 1134, 15, 16, 25 + 15, 56 + 16 * i) for i in range(0, 30)] \
                    + [Brick(393, 1134, 15, 16, 250 + 15 * i, 56) for i in range(1, 21)] \
                    + [Brick(393, 1134, 15, 16, 250 + 15 * i, 56 + 16) for i in range(1, 21)] \
                    + [Brick(393, 1134, 15, 16, 250 + 15 * i, 56 + 32) for i in range(1, 21)] \
                    + [Brick(393, 1134, 15, 16, 250 + 15 * i, 56 + 48) for i in range(1, 21)] \
                    + [Brick(393, 1134, 15, 16, 250 + 15 * i, 485 + 16) for i in range(0, 22)] \
                    + [Brick(393, 1134, 15, 16, 250 + 15 * i, 485 + 16) for i in range(0, 22)] \
                    + [Brick(393, 1134, 15, 16, 250 + 15 * i, 485 + 32) for i in range(0, 22)]  # 벽돌 생성
    server.collision_bricks_left = [Brick(393, 1134, 15, 16, 250, 56 + 16 * i) for i in range(0, 4)]
    server.collision_bricks_right = [Brick(393, 1134, 15, 16, 25 + 30, 56 + 16 * i) for i in range(0, 30)] \
                                    + [Brick(393, 1134, 15, 16, 250 + 15 * 21, 56 + 16 * i) for i in range(0, 4)]
    server.collision_bricks_top = [Brick(393, 1134, 15, 16, 250 + 15 * i, 56 + 64) for i in range(0, 22)]

    server.coins = [Coin(120, 0, 30, 30, 260 + 30 * i, 140) for i in range(0, 11)] \
        + [Coin(120, 0, 30, 30, 260 + 30 * i, 140 + 30) for i in range(0, 11)] \
        + [Coin(120, 0, 30, 30,  260 + 30 * i + 30, 140 + 60) for i in range(0, 9)]  # 코인 생성

    server.mario = Mario(700, 300)  # 캐릭터 생성 90 60

    game_world.add_object(server.background, 0)
    for collision_ground in server.collision_grounds:
        game_world.add_object(collision_ground, 0)
    for ground in server.grounds:
        game_world.add_object(ground, 0)

    game_world.add_object(server.lpipe, 0)
    for brick in server.bricks:
        game_world.add_object(brick, 0)
    for collision_brick_left in server.collision_bricks_left:
        game_world.add_object(collision_brick_left, 0)
    for collision_brick_right in server.collision_bricks_right:
        game_world.add_object(collision_brick_right, 0)
    for collision_brick_top in server.collision_bricks_top:
        game_world.add_object(collision_brick_top, 0)

    for coin in server.coins:
        game_world.add_object(coin, 0)

    game_world.add_object(server.mario, 1)

    server.mario.mario_in_bonusstage = True

def exit():
    game_world.clear()

def update():
    for game_object in game_world.all_objects():
        game_object.update()

    # 충돌 체크 및 충돌 처리
    # 마리오 - 땅
    ground_collision = False
    for collision_ground in server.collision_grounds:
        if collision.collide(collision_ground, server.mario):
            ground_collision = True

            left, bottom, right, top = collision_ground.get_bb()
            collide_loc = top + 30

    if ground_collision == True:
        server.mario.stop(collide_loc)
    else:
        server.mario.fall()

    # 마리오 - 벽돌
    for collision_brick_left in server.collision_bricks_left:
        if collision.collide(collision_brick_left, server.mario):  # 벽돌과 충돌했을 경우
            left, bottom, right, top = collision_brick_left.get_bb()
            collide_loc_left = left - 10
            server.mario.cantgo_left(collide_loc_left)  # 앞으로 못 감
    for collision_brick_right in server.collision_bricks_right:
        if collision.collide(collision_brick_right, server.mario):  # 벽돌과 충돌했을 경우
            left, bottom, right, top = collision_brick_right.get_bb()
            collide_loc_right = right + 11
            server.mario.cantgo_right(collide_loc_right)  # 앞으로 못 감
    collision_brick_top_ing = False
    for collision_brick_top in server.collision_bricks_top:
        if collision.collide(collision_brick_top, server.mario):  # 벽돌과 충돌했을 경우
            collision_brick_top_ing = True

            left, bottom, right, top = collision_brick_right.get_bb()
            collide_loc_top = top + 30

    if collision_brick_top_ing == True:
        server.mario.stop(collide_loc_top)
    else:
        server.mario.fall()
    # 마리오 - 코인
    for coin in server.coins:
        if collision.collide(coin, server.mario):  # 코인과 충돌했을 경우
            server.mario.addCoin()  # 획득 코인 수 추가
            server.mario.addScore(200)  # 점수 추가
            server.coins.remove(coin)  # 코인 충돌 검사하는 리스트에서 제거
            game_world.remove_object(coin)  # 충돌한 코인 삭제

    # 마리오 - 파이프
    if collision.collide(server.lpipe, server.mario):  # 파이프와 충돌했을 경우
        # from MarioBros_Mario import Mario_in_BonusStage
        # global Mario_in_BonusStage
        # Mario_in_BonusStage = False
        game_framework.change_state(MarioBros_Stage1)  # stage1으로 이동

def draw():
    clear_canvas()

    for game_object in game_world.all_objects():
        game_object.draw()

    font = load_font('SuperMario256.ttf', 16)
    numfont = load_font('SuperMario256.ttf', 18)

    from MarioBros_Mario import Mario_score, Mario_life
    font.draw(30, 570, 'MARIO', (255, 255, 255))
    numfont.draw(100, 570, '%06d' % Mario_score, (255, 255, 255))
    numfont.draw(100, 550, 'x', (255, 255, 255))
    numfont.draw(115, 550, '%02d' % Mario_life, (255, 255, 255))

    if server.coin_image == None:
        server.coin_image = load_image('ItemsSheet.png')
    server.coin_image.clip_draw(120, 0, 30, 30, 400, 575)  # 코인 개수 이미지

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
        if event.type == SDLK_ESCAPE:
            game_framework.change_state(MarioBros_Stage1)
        else:
            server.mario.handle_event(event)


