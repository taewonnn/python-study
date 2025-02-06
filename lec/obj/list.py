# List 리스트
# 리스트는 0개 이상의 값을 담을 수 있는 주머니

# - 요소들에는 순서가 있음
# - 여러 자료형의 값들을 담을 수 있음
# - 값의 추가 및 제거가 가능


# 리스트 초기화
my_list = [10, 20, 30, 40, 50, 60]

empty_list = []

list_type = str(type(my_list))
list_size = len(my_list)

pass


# 단일 요소 접근
single_element = my_list[1]

# 슬라이싱으로 부분 리스트 가져오기
sub_list = my_list[1:3] # 20 30

# 음수 인덱스로 끝에서부터 요소에 접근
negative_index_element = my_list[-1]  # 60



# 단계별 슬라이싱
step_slicing_1 = my_list[::2]  # [10, 30, 50]  2칸씩
step_slicing_2 = my_list[::3]  # [10, 40]  3칸씩
step_slicing_3 = my_list[1::2]  # [20, 40, 60] index 1에서 시작해서 두 칸씩


# 전체 리스트 복사 - 두 방법들
# 💡 이후 변화 비교
items_moved = my_list[:] # 그대로 복사해서 반환 / 집 안에 있는 요소(가구)만 복사해서 새집에 넣어주는거
another_list = my_list # 🔴  집 주소를 변경  #

# 리스트의 특정 요소 수정
my_list[0] = 15  # []
my_list[2] = 35  # []


print(items_moved) # [10, 20, 30, 40, 50, 60]
print(another_list)  # [15, 20, 35, 40, 50, 60]




# 연산자

# 리스트 정의
list_1 = [1, 2, 3]
list_1_b = [1, 2, 3]
list_2 = [4, 5, 6]

# + : 연결
combined_list = list_1 + list_2 # [1, 2, 3, 4, 5, 6]

# * : 반복
repeated_list = list_1 * 2 # [1, 2, 3, 1, 2, 3]

# del : 항목 삭제
del combined_list[4]  # [1, 2, 3, 4, 6]

# 💡 == : 비교 ('내용이' 동일한지)
is_equal = list_1 == list_1_b   # True

# 💡 is : 비교 (같은 리스트인지 : 메모리상 같은 위치인지 id를 비교)
is_same = list_1 is list_1_b   # False

# != : 리스트 비교 (다른지)
is_not_equal = list_2 != [4, 5, 6]  # False

# in : 포함 여부
in_list_1_a = 3 in list_1 # True
in_list_1_b = 4 in list_1 # False
in_list_1_c = 4 not in list_1 # True

pass


# method

# 리스트 초기화
# 💡 여러 자료형 포함 가능
exp_list = [1, 2.0, "삼", [4, 5]] # 🔴 스텝오버하며 디버깅

pass

# append: 리스트 끝에 항목 추가
exp_list.append(6) # [1, 2.0, '삼', [4, 5], 6]

# extend: 다른 리스트의 모든 항목을 추가
exp_list.extend([7, 8, 9])   # [1, 2.0, '삼', [4, 5], 6, 7, 8, 9]

# append로 배열을 넣으면 배열 그대로 추가됨
exp_list.append([10,11,12])  # [1, 2.0, '삼', [4, 5], 6, 7, 8, 9, [10, 11, 12]]

# insert: 지정된 위치에 항목 삽입
exp_list.insert(1, 'a') # [1, 'a', 2.0, '삼', [4, 5], 6, 7, 8, 9, [10, 11, 12]]

# remove: 리스트에서 항목 제거
exp_list.remove('a') # [1, 2.0, '삼', [4, 5], 6, 7, 8, 9, [10, 11, 12]]

# pop: 리스트의 마지막 항목을 제거하고 그 항목을 반환
pop_result = exp_list.pop() # pop_result : [10, 11, 12]

# clear: 리스트의 모든 항목 제거
exp_list.clear()




# index / count
num_list = [1, 4, 2, 4, 3, 4, 5]

# index: 항목의 첫 위치(index) 반환
index_result = num_list.index(3) # 없는 값일 시 오류
print('!', index_result)  # 4

# count: 리스트에서 항목의 개수 반환
count_result = num_list.count(4)
print('!!', count_result) # 3

pass


# sort: 리스트 정렬(오름 차순)
# 💡 해당 리스트 자체를 정렬 : sorted와는 다름
num_list.sort()
sort_result = num_list
print('sort',sort_result) # [1, 2, 3, 4, 4, 4, 5]

# reverse: 리스트 항목 순서를 역순으로 배치 - reversed와 다름
num_list.reverse() # ⭐️ sort_result의 내용 확인

# copy: 리스트 복사
copy_result = num_list.copy()

num_list.reverse() # ⭐️ 여기부터 sort_result와 copy_result의 내용 확인
num_list.append(6)
num_list.clear()

pass

# join : 문자열의 리스트를 하나의 문자로
str_list = ["a", "b", "c", "d", "efg"]

str_join = "".join(str_list)
str_join_w_sp = " ".join(str_list)
str_join_w_cm = ", ".join(str_list)


