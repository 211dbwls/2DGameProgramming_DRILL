from pico2d import *

STAGE_WIDTH, STAGE_HEIGHT = 1920, 1080

def handle_event():  # 입력처리
    global running

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:  # 종료 버튼
            playing = False
        elif event.type == SDL_KEYDOWN:  # 키 눌렀을 때
            if event.key == SDLK_d:  # D키_앞으로 이동
                pass
            if event.key == SDLK_ESCAPE:  # esc 키_종료
                playing = False
        elif event.type == SDL_KEYUP:  # 키 뗐을 때
            if event.key == SDLK_d:  # D키_앞으로 이동
                pass


open_canvas(STAGE_WIDTH, STAGE_HEIGHT)

# 이미지 로드
background = load_image('Back.png')
character = load_image('Mario.png')

# 변수
playing = True
running = True
x, y = STAGE_WIDTH // 2, STAGE_HEIGHT // 2
frame = 0

while playing:
    clear_canvas()

    background.draw(STAGE_WIDTH // 2, STAGE_HEIGHT // 2)
    character.clip_draw(frame * 100, 100, 60, 60, x, y)

    update_canvas()

    handle_event()

clear_canvas()


