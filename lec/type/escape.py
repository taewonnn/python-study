# escape sequences 탈출 문자


# ‼️오류 '
# print('It's a sunny day')


# 작은따옴표 (Single Quote) =>  \'
print('It\'s a sunny day')

# 큰따옴표 (Double Quote) => \"
print("He said, \"Python is awesome!\"")




# 새 줄 (New Line) => \n
print("Hello\nWorld")

# 탭 (Tab) => \t
print("Hello\tWorld")

# 백슬래시 (Backslash) => \\
print("Backslash: \\") # 💡 백슬래시 하나만 하면 오류

# 백스페이스 (Backspace)
print("Hello\bWorld")

# 캐리지 리턴 (Carriage Return)
print("Hello\rWorld")



#  문자열 포매팅
#  문자열 내 지정된 위치에 데이터를 삽입하는 방식

room_no = 7        # 정수
temp = 21.2     # 실수
label = 'A'       # 문자
owner = 'Alice'   # 문자열


# 방식1
format_4 = "방번호: {}, 온도: {:.2f}°C, 라벨: '{}', 주인: {}.".format(room_no, temp, label, owner)


# 방식2
format_5 = f"방번호: {room_no}, 온도: {temp:.1f}°C, 라벨: '{label}', 주인: {owner}."
