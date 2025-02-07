# 조건문 if else

if True:
    print("ture!!") # true!!

if False:
    print("false!")


if 4 % 2:
    print("4는 홀수?")
else:
    print("4는 짝수?")

# 4는 짝수?


letter = "c"
if len(letter) == 1 and ("A" <= letter <= "Z" or "a" <= letter <= "z"):
    print("알파벳")
else:
    print("알파벳 X")

# 알파벳 문자입니다.


# elif
number = 12
if number < 0:
    print("음수")
elif number == 0:
    print("영")
elif number < 10:
    print("한 자리 숫자")
elif number < 100:
    print("두 자리 숫자")
else:
    print("세 자리 이상 숫자")


num = int(input('number: \n'))
if num < 0:
    print('음수')
elif num == 0:
    print('0')
elif num > 0:
    print('양수')
else:
    print('!!')




# 중첩 if문
age = 21
is_student = False

if age >= 20:
    if is_student:
        print("할인가")
    else:
        print("정가")
else:
    print("판매제한")

#정가