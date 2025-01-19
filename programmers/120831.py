# https://school.programmers.co.kr/learn/courses/30/lessons/120831

# 정수 n이 주어질 때, n이하의 짝수를 모두 더한 값을 return 하도록 solution 함수를 작성해주세요.

# 제한사항
# 0 < n ≤ 1000

# 입출력 예
# n	result
# 10	30
# 4	6
# 입출력 예 설명
# 입출력 예 #1

# n이 10이므로 2 + 4 + 6 + 8 + 10 = 30을 return 합니다.
# 입출력 예 #2

# n이 4이므로 2 + 4 = 6을 return 합니다.



def solution(n):
  return sum([i for i in range(2, n + 1, 2)])


# range(2, n + 1, 2): 2부터 n까지 짝수만 생성 (2, 4, 6, 8, ...)
# [i for i in ...]: 리스트를 생성 ([2, 4, 6, 8, ...])
# sum(...): 리스트에 있는 모든 숫자를 더함



# for문
def solution2(n):
    total = 0
    for i in range(2, n + 1, 2):  # 2부터 n까지 2씩 증가 (짝수만)
        total += i  # total에 더하기
    return total