# for - 반복문

# 기본 구조
# for 변수 in 리스트(또는 튜플, 문자열):
#     수행할_문장1
#     수행할_문장2
#     ...


# 기본적인 리스트 순회
arr = [1,2,3,4]
for num in arr:
    print(num)
    

# index랑 같이 가져오기 - enumerate()
arr = ["apple", "banana", "cherry"]
for idx, value in enumerate(arr):
    print(f"Index: {idx}, Value: {value}")

#결과
# Index: 0, Value: apple
# Index: 1, Value: banana
# Index: 2, Value: cherry


# 리스트의 짝수 요소만 가져오기

# range(start, stop, step)

# start: 시작 숫자 (포함됨)
# stop: 끝 숫자 (포함되지 않음)
# step: 증가하는 값 (기본값은 1)

arr = [10, 20, 30, 40, 50, 60]
for i in range(0, len(arr), 2):
    print(arr[i])


# 결과
# 10
# 30
# 50



def solution(n):
    total = 0
    for i in range(2, n + 1, 2):  # 2부터 n까지 2씩 증가 (짝수만)
        total += i  # total에 더하기
    return total

# ✅ 코드 실행 과정 (n = 10일 때)
i = 2, total = 2
i = 4, total = 2 + 4 = 6
i = 6, total = 6 + 6 = 12
i = 8, total = 12 + 8 = 20
i = 10, total = 20 + 10 = 30


# range(start, stop, step)

# start: 시작 숫자 (포함됨)
# stop: 끝 숫자 (포함되지 않음)
# step: 증가하는 값 (기본값은 1)







# for i in range(반복횟수)
message = "bmw!!"

for i in range(10):
    print(i)
    print(message)


# 0
# bmw!!
# 1
# bmw!!
# 2
# bmw!!
# 3
# bmw!!
# 4
# bmw!!
# 5
# bmw!!
# 6
# bmw!!
# 7
# bmw!!
# 8
# bmw!!
# 9
# bmw!!


# list / dictionary 하나씩
list = ["bmw", "k5", "genesis"]


# list length만큼 반복
for i in list:
    print(i)

# bmw
# k5
# genesis


for car in list:
    print(car + "!!!!")

# bmw!!!!
# k5!!!!
# genesis!!!!


# 0부터 3까지
for car in range(0, 3):
    print("안녕")

# 안녕
# 안녕
# 안녕


dic = {
    "1": 111,
    "2": 222,
    "3": 333,
}

for u in dic:
    print(u)

# 1
# 2
# 3


# Ex.

print("==========")
for i in range(1, 10):
    print(i * 2)

print("==========")


# 이중 for문
for i in range(1, 10):
    for a in range(1, 10):
        print(a * i)


# f-string
for i in range(1, 10):
    for a in range(1, 10):
        print(f"{i} * {a} = {i *a}")
