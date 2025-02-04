# boolean
# 참과 거짓 둘 중 하나의 값만 갖는 자료형

bool1 = True
bool2 = False

# not 연산자 : 불리언의 값을 반전
bool3 = not bool1
bool4 = not bool2

bool5 = not (1 < 2)  # False
bool6 = not(not (1 < 2)) # True

pass


# and 와 or
# - `and` : 양쪽 모두 `True` 일 때만 `True` 반환
# - `or` : 양쪽 중 하나만 `True` 면 `True` 반환

bl_1 = True and True # True
bl_2 = True and False # False
bl_3 = False and True # False
bl_4 = False and False # False

bl_5 = True or True # True
bl_6 = True or False # Ture
bl_7 = False or True # True
bl_8 = False or False # False

pass


bl_1 = 3 < 4
bl_2 = 3 < 4 <= 5 > 1
bl_3 = 3 < 4 <= 5 > 7

bl_4 = (1 + 5) == (2 * 3) == (1 * 6)
bl_5 = (1 + 5) == (2 * 3) == (1 * 7)

pass



# Truthy & Falsy
# 💡 참/거짓을 따지는 맥락에서 각각 True 또는 False 로 간주되는 값

# - Truthy : `True`
#     - 0을 제외한 모든 숫자(양수 및 음수)
#     - 요소/글자가 하나라도 있는 문자열, 리스트, 튜플, 딕셔너리, 세트
# - Falsy : `False`
#     - 0과 그 변형: 0, 0.0, 0j
#     - 빈 컬렉션: '' (빈 문자열), [] (빈 리스트), () (빈 튜플), {} (빈 딕셔너리), set() (빈 세트)
#     - None


# 삼항 연산자 Ternary Operators
# {참일 때 값} if {조건} else {거짓일 때 값}

ternary_1 = 1 if True else 2

use_kor = True
ternary_2 = "안녕" if use_kor else "Hello"

num = 12
ternary_3 = "홀수" if num % 2 else "짝수"

pass