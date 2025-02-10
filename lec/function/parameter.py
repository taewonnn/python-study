# Parameter

# 기본값을 가진 매개변수
# 💡 기본값 매개변수는 무조건 뒤쪽에 있어야 함
def make_coffee(cup, type="아메리카노"):
    return f"{type} {cup}잔 준비되었습니다."

# 기본값 매개변수 사용
coffee_result = make_coffee(2)
coffee_result_latte = make_coffee(1, "라떼")
print(coffee_result_latte)

pass


# 정해지지 않은 수의 매개변수 튜플로 받기  *
def add_numbers(*numbers):
  print(numbers, type(numbers).__name__)
  total = 0
  for number in numbers :
    total +=number
  return total

print('@',add_numbers(1,2,3,4)) # 10


# 키워드 매개변수
# 실행부에 매개변수의 이름을 적어 인자의 대상 특정
# 이를 적지 않고 매개변수의 순서를 기준으로 하는 것은 위치 매개변수라고 함

def create_profile(name, age, job):
    return f"이름: {name}, 나이: {age}, 직업: {job}"


# 키워드 매개변수 사용
prof_1 = create_profile(name="지훈", age=30, job="개발자")

# 키워드 매개변수는 순서를 바꾸어도 정상 작동
prof_2 = create_profile(job="디자이너", age=25, name="수민")

# 일부만 키워드 매개변수로 사용 가능
prof_3 = create_profile("영희", job="교사", age=28)

# ⚠️ 위치 매개변수는 앞쪽의 것을 사용해야 함 - 매개변수의 위치를 기준으로 
# prof_4 = create_profile("개발자", name="돌준", age=22)

pass



# 💡 * 뒤로 오는 매개변수는 키워드 전용
def create_user(name, age, *, email, phone=None):
    user_info = {
        "name": name,
        "age": age,
        "email": email,
        "phone": phone
    }
    return user_info


# 키워드 전용 매개변수는 반드시 키워드로 호출
user1 = create_user("김철수", 30, email="kcs@***.com")
user2 = create_user("이영희", 25, email="lyh@***.com", phone="123-4567")

# ⚠️ 어길 시 오류 발생
# user3 = create_user("박돌준", 27, "pdj@***.com", "234-5678")

pass

# 모든 매개변수가 키워드 전용
def calculate_area(*, width, height):
    return width * height
  
  
# ⚠️ 오류 Traceback (most recent call last)
#  area1 = calculate_area(3,4)

area2 = calculate_area(width=3, height=4)
print(area2) # 12



# 가변 키워드 매개변수 **
# 정해지지 않은 키워드와 개수의 인자를 딕셔너리 형태로 받음
def build_profile(**info):
    info_type = type(info).__name__
    return info # 🔴


profile_result = build_profile(name="지훈", age=30, job="개발자")

pass


# 위치 매개변수와 가변 키워드 매개변수 함께 사용
# 마땅한 이름이 없을 시 관례적으로 각각 *args 와 **kwargs 사용
def print_args_and_kwargs(*args, **kwargs):
    print(f"위치 인자들: {args}")
    for arg in args:
        print(arg)

    print(f"\n키워드 인자들: {kwargs}")
    for key, value in kwargs.items():
        print(f"{key}: {value}")


print_args_and_kwargs('apple', 'banana', 'cherry', name='김돌준', age=30, country='대한민국')