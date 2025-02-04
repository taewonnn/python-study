# string 문자열

hello_1 = "Hello"
hello_2 = 'Hello'

hello_3 = "hello"

hello_1_type = str(type(hello_1))
hello_2_type = str(type(hello_2))

comp_1 = hello_1 == hello_2 # 큰따옴표와 작은따옴표는 같게 취급
comp_2 = hello_1 == hello_3 # 대소문자 구분

pass

# """ \n """
str_multline = """여러줄의
문자열을 이렇게
작성해보겠습니다."""

print(str_multline)


str_plus = "더하기 연산자는 " + '문자열을 이어줍니다.'

str_mult = "🐶 " + "멍! " * 3

pass


# 다른 자료형을 더할떄
# ⚠️ 오류! 문자열과 숫자를 그냥 더할 수 없음
# comb_0 = "123" + 45

# 아래와 같이 형변환해야 함
comb_1 = "123" + str(45)  # "12345"  str
comb_2 = int("123") + 45  # 168 int

pass

true_str = str(True)  # "True"
pi_str = str(3.14)    # "'"3.14"
img_str = str(1 + 2j) # "(1+2j)"

pass


# in / not in
# 앞의 문자열이 뒤의 문자열에 포함되는가 여부
# 포함되어 있는지 True / False로 반환

string = "헬로, 파이썬!"

contain_1 = "파이썬" in string # True
contain_2 = "Python" in string # False

contain_3 = "헬로" not in string   # False
contain_4 = "Hello" not in string  # True

pass


# 비교 연산자
comp_0 = "안녕하세요" == "반갑습니다."
comp_1 = "안녕하세요" != "반갑습니다."

# 💡 사전순으로 앞에 오는 문자열이 더 작다고 간주
comp_2 = "apple" < "banana"   # True
comp_3 = "가나다" <= "라마바"   # True
comp_4 = "홍길동" > "홍" # True

pass


# index / slice

my_str = "헬로, Python!"

letter_0 = my_str[0] # '헬'
letter_1 = my_str[4] # 'P'
letter_2 = my_str[-1] # !"   -는 뒤에서부터

# ⚠️ IndexError
# letter_3 = my_str[12]

pass

phone_no = "010-1234-5678"

# 앞/뒤에서 ~번째 문자
# 앞에서는 0부터, 뒤에서는 -1부터
first_letter = phone_no[0]  # 0
last_letter = phone_no[-1] # 8

# 앞에서부터 ~번째까지 문자들
first_piece_1 = phone_no[0:3] # 010
first_piece_2 = phone_no[:3] # 010

# ~번째부터 ~번째까지 문자들
middle_piece = phone_no[4:8] # 1234
last_piece_1 = phone_no[9:13] # 5678

# ~번째부터 끝까지 문자들
last_piece_2 = phone_no[9:] # 5678
last_piece_3 = phone_no[-4:] # 5678

pass