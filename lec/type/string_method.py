# string method

exp_str = "Hi, This is Python class. Thanks!"

# 문자열 길이 반환 len(variable)
length = len(exp_str)
print(length)  # 33

len_type = str(len(exp_str)) # len_type = <class 'int'>


# 대문자 / 소문자 변환 - upper() / lower()

upper_case = exp_str.upper()
print(upper_case)  # HI, THIS IS PYTHON CLASS. THANKS!
lower_case = exp_str.lower()
print(lower_case)  # hi, this is python class. thanks!


# 문자열 치환 - replace('기존', '변경')
# 원본을 바꾸진 않는다!

replace_str = exp_str.replace('Python', 'javaScript')
print('replace: ',replace_str, 'original: ', exp_str)
# replace:  Hi, This is javaScript class. Thanks! original:  Hi, This is Python class. Thanks!


# 문자열 분할 split('기준') -> list로 반환
split_str = exp_str.split(',')
print(split_str) # ['Hi', ' This is Python class. Thanks!']


# 문자열 시작 문자열 확인
starts_with = exp_str.startswith('Python')
print(starts_with)  # False

# 문자열 종료 문자열 확인
ends_with = exp_str.endswith('!')
print(ends_with)  # True


# 위치
text_to_search = "Python"

# 문자열 내에 주어신 문자열의 첫 번째 위치 반환
find_result = text_to_search.find(text_to_search)  # 7
index_result = text_to_search.index(text_to_search) # 7
print(find_result, index_result)   # 0 0


# 찾고자 하는 문자열이 없을 때,
# find -> 없으면 -1
# index -> 없으면 Error

find_text = 'Java'
index_result2 = text_to_search.find(find_text)
print(index_result2) # -1


# 뒤에서부터 찾기 rfind(value)
rfind_reuslt = exp_str.rfind(text_to_search)
print(rfind_reuslt) # 12



# 공백 제거
original_text = "     Hello, python!  "

stripped_str = original_text.strip()

left_stripped_str = original_text.lstrip()

right_stripped_str = original_text.rstrip()