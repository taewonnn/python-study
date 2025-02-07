# match
# 주어진 값에 따라 다양한 동작을 지정 가능
# 타 언어의 switch 문과 유사 / 차이점 존재

# 타 언어 `switch` 문과의 차이
# - 패턴 매칭 사용 가능
# - `break` 문 없음


# 값으로 매칭
# case _ : 위의 case 들 중 어느 곳에도 속하지 않는 값일 때
# 맨 마지막에 사용
person = "Alice"
match person:
    case "Alice":
        print("Alice!!")
    case "Bob":
        print("Bob!!!")
    case _:
        print("welcome.")



# or  매칭 & if  가드 사용

x = 0
y = 5

match x:
    case 0:
        print("Case A")
    case  1 | 2 | 3:
        print("Case B")
    case 4 if x < y:
        print("Case C")
    case _ if x > y:
        print("Case D")
    case _:
        print("Case E")


# 자료형으로 매칭
# bool은 int의 한 종류이므로, int() 가 위에 있으면 True 와 False 가 그곳에 매칭됨

var = 1

match var:
    case bool():
        print('bool!')
    case int():
        print('int!')
    case float():
        print('float')
    case str():
        print('str!')
    case _:
        print('etc')


# 패턴으로 매칭

# my_list = []
# my_list = ["apple"]
# my_list = ["apple", "banana"]
my_list = ["apple", "banana", "orange", "mango"]


match my_list:
    case []:
        print('empty list')
    case [a]:
        print(f"{a} element")
    case [a,b]:
        print(f"{a},{b}!!")
    case [a, *rest]:
        print(f'{a}, 나머지:{rest}') # apple, 나머지:['banana', 'orange', 'mango']
    case _:
        print('XX')



# point = (0, 0)
# point = (2, 0)
# point = (0, 3)
# point = (4, 5)
point = 1

match point:
    case (0, 0):
        print("원점")
    case (x, 0):
        print(f"X={x}")
    case (0, y):
        print(f"Y={y}")
    case (x, y):
        print(f"X={x}, Y={y})")
    case _:
        print("좌표 X")


# my_dict = {}
# my_dict = {"name": "홍길동", "age": 30}
# my_dict = {"school": "엄석대", "major": "컴퓨터공학"}
my_dict = {"job": "개발자", "position": "팀장", "years": "5"}

match my_dict:
    case {"name": name, "age": age}:
        print(f"인적 정보 - {name}({age})세")
    case {"school": school, "major": major}:
        print(f"학력 정보 - {school} 졸업 ({major} 전공)")
    case {"job": job, **rest}:
        print(f"직업 정보 - {job}") # 직업 정보 - 개발자
    case {}:
        print("빈 딕셔너리")



