from pico2d import *

import game_framework
import MarioBros_Stage1

from MarioBros_BossStage_Background import *

from MarioBros_BossStage_Coin import *

from MarioBros_Enemies_Boss import *

from MarioBros_Mario import *
from MarioBros_Mario_FireBall import *

import server
import collision

name = "MarioBros_BossStage"

STAGE_WIDTH, STAGE_HEIGHT = 800, 600
# 변수 ------------------------------------------------------------------------------------------------------------------

# 함수 -----------------------------------------------------------------------------------------------------------------
def enter():
    # initialization code : 초기화
    server.background = Background()  # 배경 생성
    server.grounds_up = [Ground(413, 1095, 16, 17, 8 + 16 * i, 349 + 17 * j) for i in range(0, 60) for j in range(0, 12)] \
                        + [Ground(413, 1095, 16, 17, 968, 349 - 68 + 17 * i) for i in range(0, 16)] \
                        + [Ground(413, 1095, 16, 17, 968 + 16 * i, 349 + 17 * 5 + 17 * j) for i in range(0, 28) for j in range(0, 7)] \
                        + [Ground(413, 1095, 16, 17, 1416, 349 - 68 + 17 * i) for i in range(0, 16)] \
                        + [Ground(413, 1095, 16, 17, 1416 + 16 * i, 349 - 68 + 17 * j) for i in range(0, 50) for j in range(0, 16)] \
                        + [Ground(413, 1095, 16, 17, 2216 + 16 * i, 349 + 17 * j) for i in range(0, 87) for j in range(0, 12)] # 땅 생성
    server.grounds_down = [Ground(413, 1095, 16, 17, 8 + 16 * i, 124 + 34 * 2) for i in range(0, 11)] \
                          + [Ground(413, 1095, 16, 17, 8 + 16 * i, 124 + 34 + 17) for i in range(0, 11)] \
                          + [Ground(413, 1095, 16, 17, 8 + 16 * i, 124 + 34) for i in range(0, 13)] \
                          + [Ground(413, 1095, 16, 17, 8 + 16 * i, 124 + 17) for i in range(0, 13)]\
                          + [Ground(413, 1095, 16, 17, 8 + 16 * i, 124) for i in range(0, 15)] \
                          + [Ground(413, 1095, 16, 17, 8 + 16 * i, 5 + 17 * j) for i in range(0, 40) for j in range(0, 6)] \
                          + [Ground(413, 1095, 16, 17, 680 + 16 * i, 5 + 17 * j) for i in range(0, 25) for j in range(0, 6)] \
                          + [Ground(413, 1095, 16, 17, 1112 + 16 * i, 5 + 17 * j) for i in range(0, 10) for j in range(0, 6)] \
                          + [Ground(413, 1095, 16, 17, 1304 + 16 * i, 5 + 17 * j) for i in range(0, 75) for j in range(0, 6)] \
                          + [Ground(413, 1095, 16, 17, 2866 + 16 * i, 124) for i in range(0, 5)] \
                          + [Ground(413, 1095, 16, 17, 2866 + 16 * i, 5 + 17 * j) for i in range(0, 5) for j in range(0, 6)] \
                          + [Ground(413, 1095, 16, 17, 2946 + 16 * i, 5 + 17 * j) for i in range(0, 42) for j in range(0, 6)]  # 땅 생성
    server.grounds_down_top = [Ground(413, 1095, 16, 17, 8 + 16 * i, 124 + 34 * 2 + 17) for i in range(0, 11)] \
                              + [Ground(413, 1095, 16, 17, 8 + 16 * i, 124 + 34 + 17) for i in range(11, 13)] \
                              + [Ground(413, 1095, 16, 17, 8 + 16 * i, 124 + 17) for i in range(13, 15)] \
                              + [Ground(413, 1095, 16, 17, 8 + 16 * i, 5 + 17 * 6) for i in range(0, 40)] \
                              + [Ground(413, 1095, 16, 17, 680 + 16 * i, 5 + 17 * 6) for i in range(0, 25)] \
                              + [Ground(413, 1095, 16, 17, 1112 + 16 * i, 5 + 17 * 6) for i in range(0, 10)] \
                              + [Ground(413, 1095, 16, 17, 1304 + 16 * i, 5 + 17 * 6) for i in range(0, 75)] \
                              + [Ground(413, 1095, 16, 17, 2866 + 16 * i, 124 + 17) for i in range(0, 5)] \
                              + [Ground(413, 1095, 16, 17, 2866 + 16 * i, 5 + 17 * 6) for i in range(0, 5)] \
                              + [Ground(413, 1095, 16, 17, 2946 + 16 * i, 5 + 17 * 6) for i in range(0, 42)]  # 땅 생성

    server.firegrounds = [FireGround(620, 755, 35, 35, 656, 10), FireGround(620, 755, 35, 35, 656, 30), FireGround(620, 792, 35, 12, 656, 54),
                          FireGround(620, 755, 35, 35, 1088, 10), FireGround(620, 755, 35, 35, 1088, 30), FireGround(620, 792, 35, 12, 1088, 54),
                          FireGround(620, 755, 35, 35, 1280, 10), FireGround(620, 755, 35, 35, 1280, 30), FireGround(620, 792, 35, 12, 1280, 54)]  # 불 생성

    server.bridgegrounds = [BridgeGround(580, 770, 25, 15, 2507 + 18 * i, 107) for i in range(0, 20)]
    server.bridgeground_up = BridgeGroundUp(140, 1200, 40, 10, 2700, 157)  # 다리 생성


    server.bricks = [Brick(373, 1095, 16, 17, 968, 264),
                     Brick(373, 1095, 16, 17, 1180, 264),
                     Brick(373, 1095, 16, 17, 1416, 264), Brick(373, 1095, 16, 17, 1630, 264),
                     Brick(373, 1095, 16, 17, 1844, 264), Brick(373, 1095, 16, 17, 2058, 264)]  # 벽돌 생성

    server.boss = Boss(0, 10, 40, 50, 2820, 130)  # 보스 생성

    server.mario = Mario(2500, 100)  # 캐릭터 생성

    game_world.add_object(server.background, 0)

    for ground_up in server.grounds_up:
        game_world.add_object(ground_up, 0)
    for ground_down in server.grounds_down:
        game_world.add_object(ground_down, 0)
    for ground_down_top in server.grounds_down_top:
        game_world.add_object(ground_down_top, 0)

    for fireground in server.firegrounds:
        game_world.add_object(fireground, 0)
    for bridgeground in server.bridgegrounds:
        game_world.add_object(bridgeground, 0)
    game_world.add_object(server.bridgeground_up, 0)

    for brick in server.bricks:
        game_world.add_object(brick, 0)

    game_world.add_object(server.boss, 1)

    game_world.add_object(server.mario, 1)

    server.mario.mario_in_bonusstage = False

def exit():
    game_world.clear()

def update():
    for game_object in game_world.all_objects():
        game_object.update()

    # 충돌 체크 및 충돌 처리
    # 마리오 - 땅
    for ground_down_top in server.grounds_down_top:
        if collision.collide(ground_down_top, server.mario):
            left, bottom, right, top = ground_down_top.get_bb()
            collide_loc = top + 10

            server.mario.stop(collide_loc)

    # 마리오 - 다리
    for bridgeground in server.bridgegrounds:
        if collision.collide(bridgeground, server.mario):
            left, bottom, right, top = bridgeground.get_bb()
            collide_loc = top + 10

            server.mario.stop(collide_loc)

    # 마리오 - 다리
    if collision.collide(server.bridgeground_up, server.mario):
        left, bottom, right, top = server.bridgeground_up.get_bb()
        collide_loc = top + 10

        server.mario.stop(collide_loc)

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
        else:
            server.mario.handle_event(event)

