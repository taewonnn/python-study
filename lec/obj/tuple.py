# Tuple ()
# 튜플은 리스트처럼 순서가 있는 다양한/다수의 값을 담을 수 있지만
# 수정, 추가, 삭제 등의 변경이 불가능하다는 차이가 있습니다.


# 튜플 생성
# 여러 자료형 포함 가능
my_tuple = (1, 2, 3, True, 'ABC', [1, 2, 3], (4, 5, 6))
type_tuple = str(type(my_tuple))

# ‼️Error -> tuple은 안에 값을 변경할 수 없음
# my_tuple[0] = 2

# 튜플의 요소 접근 - list와 동일
first_element = my_tuple[0]  # 1


# 튜플의 길이 구하기
tuple_length = len(my_tuple)  # 7

pass


# 튜플을 사용한 다중 할당
# 개수가 맞아야 함
a, b, c, d, e, f, g = my_tuple

# 요소 포함 여부 확인
element_exists_1 = 2 in my_tuple # True
element_exists_2 = 4 in my_tuple # False
element_exists_3 = 4 in my_tuple[-1] # True


# 연산자
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

combined_tuple = tuple1 + tuple2

repeated_tuple = tuple1 * 2

pass


# slice

my_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

sliced_tuple1 = my_tuple[:3]
sliced_tuple2 = my_tuple[3:]
sliced_tuple3 = my_tuple[3:7]
sliced_tuple4 = my_tuple[::2]

pass



