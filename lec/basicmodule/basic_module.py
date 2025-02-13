# basic_module


# math
import math

# 파이와 자연상수
pi_value = math.pi # 3.131592...
e_value = math.e # 2.718...

# 절대값
abs_value = math.fabs(-10.5) # 10.5

# 올림
ceil_value = math.ceil(3.4) # 4

# 내림
floor_value = math.floor(3.7) # 3

# 제곱근
sqrt_value = math.sqrt(16) # 4.0

# 지수 함수
exp_value = math.exp(1)  # e^1   # 2.718...

# 로그 함수
log_value = math.log(2.7183)  # 자연 로그, e를 밑으로 함
log10_value = math.log(100, 10)  # 밑이 10인 로그

# 삼각 함수
sin_value = math.sin(math.pi / 2)
cos_value = math.cos(math.pi)
tan_value = math.tan(math.pi / 4)

# 최대공약수
gcd_value = math.gcd(48, 180)   # 12

# 최소공배수
lcm_value = math.lcm(12, 15)   # 60

# 팩토리얼
factorial_value = math.factorial(5)   # 120


pass



# random

import random

# 💡 시드 설정
# 아래를 활성화하고 값을 바꿔가며 반복 실행해 볼 것
# random.seed(10)

# 임의의 실수 생성
random_float = random.random()

# 범위 내 임의의 정수 생성
random_int = random.randint(1, 10) # 1 ~ 10 사이 랜덤 정수

# 범위와 스텝을 지정한 임의의 정수
random_range = random.randrange(0, 101, 5)   # 0 ~ 101 사이 5를 간격으로 랜덤

# 시퀀스의 임의의 요소 선택
choice_from_list = random.choice(['apple', 'banana', 'cherry', 'date'])

# 시퀀스를 무작위로 섞기
list_to_shuffle = [1, 2, 3, 4, 5]
random.shuffle(list_to_shuffle)

# 시퀀스에서 지정된 개수의 요소를 무작위로 선택
sample_from_list = random.sample([10, 20, 30, 40, 50], 3)

pass



# datetime
# 1. date : 연, 월, 일을 다룹니다.
# 2. time : 시, 분, 초, 마이크로초를 다룹니다.
# 3. datetime : 날짜와 시간을 동시에 다룹니다.
# 4. timedelta : 두 날짜나 시간 사이의 기간을 다룹니다.

from datetime import date, time, datetime, timedelta

# 오늘 날짜
today = date.today()
t_year, t_monty, t_day = today.year, today.month, today.day

# weekday 메소드 : 0(월)~6(일) 반환
t_weekday = '월화수목금토일'[today.weekday()]

# 특정 날짜 생성
some_date = date(2024, 2, 5)
s_year, s_month, s_day = some_date.year, some_date.month, some_date.day

pass


# 현재 시간
now = datetime.now()
n_hr, n_mnt, n_snd, n_msnd = now.hour, now.minute, now.second, now.microsecond

# 특정 시간 생성
some_time = time(14, 30)

# 날짜와 시간의 조합
some_datetime = datetime(2024, 2, 5, 14, 30)


# collections 
# 기본 컬렉션보다 강력한 기능들을 제공하는 특수 컨테이너 타입들을 갖습니다.

from collections import Counter

# Counter : 딕셔너리의 서브클래스로
# 주어진 컬렉션의 요소의 개수를 세는데 유용

fruits = ["apple", "orange", "apple", "pear", "orange", "banana", "orange"]
fruit_counter = Counter(fruits)

apples = fruit_counter.get("apple")
most_common_fruit = fruit_counter.most_common(1) # 몇위까지 표시할지

pass