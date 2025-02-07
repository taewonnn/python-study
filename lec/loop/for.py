# 반복문 for
# 반복 작업

# 기본 사용: 0부터 4까지의 숫자 반복
for i in range(5):
    print(f'test {i}')


# 값 사용 없이 단순반복시 : _ 사용 (컨벤션)
for _ in range(5):
    print("print")


# 시작과 끝 지정: 2부터 5까지의 숫자 반복
for i in range(2, 6):
    # i는 1부터 5까지 순차적으로 증가
    print(f"시작과 끝 지정: {i}")


# 증가폭 지정: 0부터 10까지 2씩 증가하며 숫자 반복
for i in range(0, 11, 2):
    # i는 0부터 시작하여 2씩 증가하며 10까지 이동
    print(f"증가폭 지정: {i}")


# 감소하는 범위: 5부터 1까지 역순으로 숫자 반복
for i in range(5, 0, -1):
    # i는 5부터 시작하여 1씩 감소하며 1까지 이동
    print(f"감소하는 범위: {i}")


# 중첩 사용 - 구구단
for i in range(1, 10):
    for j in range(1, 10):
        print(f"{i} x {j} = {i * j}")
    if i < 9:
        print("- - - - -")


# range() 의 반환값
my_range = range(5)
print(my_range) # range(0, 5)


# 문자열 및 자료구조 내 반복

# 문자열의 문자 순회
my_str = 'test python string'
for i in my_str:
    print(i)

# 리스트 요소 순회
fruits_test = ['apple', 'orange', 'strawberry', 'banana']
for fruit in fruits_test:
    print(f'fruit: {fruit}')


# dictionary 키 순회
person = {"이름": "홍길동", "나이": 30, "키": 179.9}
for key in person:
    print(f"{key}: {person[key]}")


# tuple 순회
tup_test= (1, 2, 3, [5, 6],4)
for item in tup_test:
    print(f"item: {item}")


# set 순화
set_test = {1, 2, 3, 4, 6}
for item in set_test:
    print(f"item: {item}")



# 다중 순환
my_li = ['abc', (1,2,3), {4, 5}, {6: 7, 8: 9}]

for sub in my_li:
    for item in sub :
        print(item)
    print('----')


# a
# b
# c
# ----
# 1
# 2
# 3
# ----
# 4
# 5
# ----
# 6
# 8
# ----


# 인덱스와 함께 순회 - enumerate
# enumerate : 각 요소의 순서와 값을 튜플로 묶음
fruits = ['apple', 'orange', 'strawberry', 'banana']


for fruit in enumerate(fruits):
    print(f"{fruit}")

# (0, 'apple')
# (1, 'orange')
# (2, 'strawberry')
# (3, 'banana')


# 튜플로 반환하는 것을 index, fruit으로 언패킹
for index, fruit in enumerate(fruits):
    print(f"인덱스 {index}: {fruit}")

# 인덱스 0: apple
# 인덱스 1: orange
# 인덱스 2: strawberry
# 인덱스 3: banana


# break / continue

# break : 반복을 종료
for i in range(1, 10):
    if i == 5:
        break
    print(i)
# 4까지만

# continue : 다음 턴으로 건너뜀
for i in range(1, 10):
    #  i가 짝수라면
    if not i % 2:
        continue
    if i == 9:
        break
    print(i)

# 1
# 3
# 5
# 7
