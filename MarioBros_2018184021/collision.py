def collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    # 충돌이 안 일어나는 상황을 먼저 체크
    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False

    return True

def collide_head_foot(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb_head()
    left_b, bottom_b, right_b, top_b = b.get_bb_foot()

    # 충돌이 안 일어나는 상황을 먼저 체크
    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False

    return True

def collide_all_head(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb_head()

    # 충돌이 안 일어나는 상황을 먼저 체크
    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False

    return True

def collide_left_all(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb_left()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    # 충돌이 안 일어나는 상황을 먼저 체크
    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False

    return True

def collide_right_all(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb_right()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    # 충돌이 안 일어나는 상황을 먼저 체크
    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False

    return True
