# set {}
# 중복되지 않으며 순서가 없는 요소들의 집합

# 선언 및 초기화
# 빈 set 생성
empty_set = set()

# 요소가 있는 set 생성
fruits = {"apple", "apple", "cherry","banana", "cherry"} #  {'apple', 'cherry', 'banana'}

# set의 요소 개수 확인
number_of_fruits = len(fruits) #3

pass


# set에 요소 추가
fruits.add("orange")

# 중복으로 추가되지 않음
fruits.add("apple")

# set에서 요소 제거
fruits.discard("banana")

# set에서 💡무작위 요소 제거 및 반환
removed_item = fruits.pop()


# 교집합 - &
set_1 = {1, 2, 3}
set_2 = {2, 3, 4}
intersection_1 = set_1 & set_2
intersection_2 = set_1.intersection(set_2)

# 합집합 - |
union_1 = set_1 | set_2
union_2 = set_1.union(set_2)

# 차집합 - difference
difference_1 = set_1 - set_2
difference_2 = set_1.difference(set_2)

# 대칭 차집합 (합집합에서 교집합을 뺀 부분) - ^
symmetric_difference_1 = set_1 ^ set_2
symmetric_difference_2 = set_1.symmetric_difference(set_2)

pass



# 리스트를 이용한 set 생성
list_example = [1, 2, 3, 2, 1]
set_from_list = set(list_example) # {1, 2, 3}

# 중복이 제거된 리스트 생성
list_without_dup = list(set_from_list)

# 튜플을 이용한 set 생성
tuple_example = (1, 2, 3, 2, 1)
set_from_tuple = set(tuple_example)   # {1, 2, 3}

# 중복이 제거된 튜플 생성
tuple_without_dup = tuple(set_from_tuple) # (1, 2, 3)

# 문자열을 이용한 set 생성
string_example = "hello"
set_from_string = set(string_example) # {'e', 'h', 'l', 'o'}

pass


# discard vs remove
fruits = {"apple", "banana", "cherry"}
fruits.remove("orange") # ⚠️ 없는 요소를 빼려 하면 오류 발생

fruits = {"apple", "banana", "cherry"}
fruits.discard("orange") # 없으면 그냥 넘어감


# frozenset
# set 과 같지만 수정이 불가능

fs_1 = frozenset([1, 2, 3, 4])
fs_2 = frozenset([3, 4, 5, 6])

# 합집합
union = fs_1 | fs_2

# 교집합
intersection = fs_1 & fs_2

# 차집합
difference = fs_1 - fs_2

# 대칭 차집합
symmetric_difference = fs_1 ^ fs_2

# 멤버십 테스트
if 2 in fs_1:
    print("2는 fs_1의 원소입니다.")

# frozenset 길이
fs_1_length = len(fs_1)

fs_items = []
# frozenset 반복
for item in fs_1:
    fs_items.append(item)

# ⚠️ frozenset은 수정 불가
# fs_1.add(5)
# fs_1.remove(1)

pass