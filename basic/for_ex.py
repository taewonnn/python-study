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


# 리스트 거꾸로 순회
arr = [1, 2, 3, 4, 5]
for num in reversed(arr):
    print(num)

#결과
# 5
# 4
# 3
# 2
# 1


# 두개 리스트 동시에 순회
names = ["Alice", "Bob", "Charlie"]
scores = [90, 80, 85]

for name, score in zip(names, scores):
    print(f"{name}: {score}")
    
#결과 
# Alice: 90
# Bob: 80
# Charlie: 85


# 리스트에서 특정 조건값만 찾기
arr = [5, 10, 15, 20, 25]
for num in arr:
    if num > 10:
        print(num)
        

#결과
15
20
25


# 리스트 내포(List Comprehension)로 빠르게 필터링
arr = [5, 10, 15, 20, 25]
filtered = [num for num in arr if num > 10]
print(filtered)

# 결과 : [15, 20, 25]



# dictionary 순회
data = {"Alice": 90, "Bob": 80, "Charlie": 85}
for key, value in data.items():
    print(f"{key}: {value}")
    

#결과
# Alice: 90
# Bob: 80
# Charlie: 85



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


# 이중 for문
for i in range(1, 10):
  for a in range(1, 10):
    print(a * i)
    
    

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for row in matrix:
    for num in row:
        print(num, end=" ")
        
        
# 결과 1 2 3 4 5 6 7 8 9
