# None
# "값이 없음”을 나타내기 위한 자료형

non = None
non_type = str(type(non))
print(non) # None


# `None` 은 싱글턴 singleton
#
# - 메모리상 단 한 곳에만 존재한다는 의미
# - `None` 값을 갖는 변수들은 모두 같은 주소를 가리킴

non_1 = None
non_1_id = id(non_1)

non_2 = None
non_2_id = id(non_2)

non_3 = None
non_3_id = id(non_3)

# 때문에 값이 None인 것들끼리는 is()가 True 반환
all_same = non_1 is non_2 is non_3


# None 인가 여부 확인은 == 대신 is 함수 권장
# ==보다 간단한 로직으로 확인하기 떄문에! is 권장
var_1 = None
var_2 = 1

is_none_1 = var_1 is None
is_none_2 = var_2 is None


