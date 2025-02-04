# 무한대 inf

import sys

# 양수 무한대와 음수 무한대
inf_pos = float('inf')
inf_neg = float('-inf')

pos_neg = inf_pos == -inf_neg # true

int_type= str(type(inf_pos))    # float

pass



# nan - 숫자 아닌 것(무효한 숫자)
# float 자료형
nan_1 = float('nan')
nan_2 = float('nan')

nan_type = str(type(nan_1))

nan_are_same = nan_1 == nan_2


# complex - 복소수

cpx_a = 2 + 3j
cpx_b = 1 - 1j

cpx_type = str(type(cpx_a))

cpx_c = cpx_a * cpx_b

pass


# 숫자 자료형 관련 기본 함수

# 절대값
num = -10
absolute_value = abs(num)
print(absolute_value) # 10

# 몫과 나머지
quotient, remainder = divmod(7, 2)
print(quotient, remainder)  # 3 1

# 제곱
pow_result = pow(2, 3)
print(pow_result) # 8

# 최대값 최소값
max_num = max(3,2,5,1,4)
min_num = min(3,2,5,1,4)
print(max_num, min_num)  # 5 1

# round() 예시
round_1 = round(3.6, 0)
round_2 = round(3.1415926535, 2)
round_3 = round(3.1415926535, 4)
print(round_1, round_2, round_3)  # 4.0 3.14 3.1416


