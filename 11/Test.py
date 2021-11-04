class Star:
    # 클래스 변수
    type = 'Star'
    x = 100

    def change():  # 클래스 함수
        x = 200  # 로컬 변수
        print('x is ', x)

# 객체 생성없이 클래스 안의 변수, 함수 호출 가능
print('x is ', Star.x)  # x is 100
Star.change()  # x is 200
print('x is ', Star.x)  # x is 100

star = Star()
print('x is ', star.x)  # x is 100
star.change()  # Error - 인자가 1개 있어야 하는 데 없음
# -> star라는 객체의 원래 클래스 Star가 가지는 change 함수 호출하면서 객체를 넘겨줌
#     Star.change(star)
# 파이썬은 객체를 호출하면 첫번째 파리미터로 본인이 호출되도록 함
# 관습적으로 self를 사용하지만 본인이 원하는 것을 써도 상관없음

# 생성자 함수가 없음 -> 파이썬에는 생성자 함수가 없어도 됨
# self가 없음

# 일반적인 클래스 : 객체를 찍어내는 용도
# 싱글톤 : 어떤 클래스로 만들어진 유일한 객체 -> 한 번만 찍어내는 객체
#         전역적으로 관리하는 객체를 만들 때 사용
# self없는 클래스 : 싱글톤처럼 사용 가능


# 클래스 변수는 객체 변수처럼 액세스 가능

