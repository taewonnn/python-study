# 중첩 / 재귀


# 함수의 중첩
# 함수 안에 다른 함수 정의

def outer_function(outer_arg):
    # 외부 함수

    def inner_function(inner_arg):
        # 내부 함수 - 스코프가 외부함수 내로 제한됨
        return inner_arg * 2

    return inner_function(outer_arg)


result_1 = outer_function(5)
# result_2 = inner_function(5) # ⚠️ 오류

pass


# 스코프 scope
# 💡 변수, 함수, 객체 등이 “유효한”(접근 가능한) 범위

outer = 0
def outer_function():
    in_outer = 1

    def inner_function():
        in_inner = 2
        print(outer)
        print(in_outer)
        print(in_inner)

    inner_function()

    print(in_outer)
    # print(in_inner) # ⚠️


outer_function()

# print(in_outer) # ⚠️
# print(in_inner) # ⚠️



# 쉐도잉 shadowing
# 바깥쪽 스코프의 변수가 안쪽 스코프의 동명 변수에 의해 가려짐
def outer_scope():
    king = "사자"
    lord = "늑대"
    print(f"바깥: {king} {lord}") # 사자 늑대

    def middle_scope():
        king = "여우"
        print(f"중간: {king} {lord}") # 여우 늑대

        def inner_scope():
            king = "고양이"
            lord = "쥐"
            print(f"안쪽: {king} {lord}") # 고양이 쥐

        inner_scope()
    middle_scope()

outer_scope()


# 쉐도잉을 하지 않고 바깥 것을 그대로 사용하려면 nonlocal 연산자 사용
def outer():
    x = "local"

    def inner():
        nonlocal x  # 💡 바깥의 x를 그대로 사용
        x = "nonlocal"
        print("inner:", x)

    inner()
    print("outer:", x)


outer()


# 전역의 변수를 그대로 사용하려면 global 연산자 사용
x = 0  # 전역 변수

def my_function():
    global x  # 💡 전역의 x를 그대로 사용
    x = 10

my_function()
print(x)


# 재귀함수
# 함수가 자기 자신을 호출하여 실행


# 카운트다운
def countdown(n):
    if n <= 0:
        print("카운트다운 종료!")
    else:
        print(n)
        countdown(n - 1) # 함수 안에서 나를 또 실행


countdown(5)
# 5
# 4
# 3
# 2
# 1
# 카운트다운 종료!


# 팩토리얼
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(5))

# 피보나치
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(10))



# 파이썬에는 위에 설명한 재귀함수의 문제를 해결하기 위해, 재귀의 최대 반복 회수를 제한하는 기능을 제공
import sys

# 현재 재귀 호출 횟수 제한
cur_rec_limit = sys.getrecursionlimit()


def rec_func(count):
    print(f"재귀 {cur_rec_limit - count}회")
    if count > 1:
        rec_func(count - 1)


# 💡 -1을 빼고 실행하면 제한에 걸려 오류가 발생합니다.
rec_func(cur_rec_limit - 1)

# 제한 횟수 수정하고 다시 실행해보기
# 이 코드를 import 바로 아래줄에 붙여넣고 다시 실행
sys.setrecursionlimit(50)
