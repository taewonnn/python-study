# dictionary {key : value}
# 키와 값의 한 쌍으로 구성된 요소들을 저장

# - 키 : 불변 객체 사용 가능
# - 값 : 모든 종류의 데이터 저장 가능


# 딕셔너리 생성 및 초기화
my_dict = {"name": "Alice", "age": 25, "city": "New York", "job": "designer"}

# 요소 추가 및 수정
my_dict["email"] = "alice@example.com"  # 새로운 요소 추가
my_dict["age"] = 26  # 기존 요소 수정

pass


# 키 유무 확인 - in
key_exists_1 = "name" in my_dict  # True
key_exists_2 = "bloodtype" in my_dict  # False

# 요소 접근
age1 = my_dict["age"] # 26
age2 = my_dict.get("age") # 26

# 💡 없는 요소에 접근시
# bloodtype = my_dict["bloodtype"] # 이 방식으로 하면 오류 발생
bloodtype = my_dict.get("bloodtype") # None

# 요소 삭제
deleted_value = my_dict.pop("city")  # 'city' 키를 가진 요소를 삭제하며 반환
del my_dict["job"] # 삭제만 하고 그 값을 반환하지는 않음



# 키, 값, 아이템
# dict_ = 묶음 자료형
# 💡 dict_keys, dict_values, dict_items 자료형 반환

keys = my_dict.keys()
print('keys',keys) # dict_keys(['name', 'age', 'email'])

values = my_dict.values()
print('values',values) # dict_values(['Alice', 26, 'alice@example.com'])

# dic -> 튜플로 묶어서 - items()
items = my_dict.items()
print('items',items)   # keys dict_items([('name', 'Alice'), ('age', 26), ('email', 'alice@example.com')])


for key in keys:
    print('key 출력', key)

# key 출력 name
# key 출력 age
# key 출력 email


# dict_(묶음 자료형)을 리스트로 변환
keys_list = list(keys)
print('keys_list',keys_list) # ['name', 'age', 'email']

values_list = list(values)
print('values_list',values_list) # ['Alice', 26, 'alice@example.com']

items_list = list(items)
print('items_list',items_list) # [('name', 'Alice'), ('age', 26), ('email', 'alice@example.com')]

# 💡 items()로 반환된 각 쌍의 자료형 확인
item_type = str(type(items_list[0]))
print('item_type',item_type)  # <class 'tuple'>



# dictionary copy
my_dict_copy = my_dict.copy()

# 다른 dictionary로부터 아이템 가져오기
another_dict = {3.14: 'PI', ('test', 'test1'): 'brother' }
my_dict.update(another_dict)

# 두 개 id값 상이
print('copy', id(my_dict_copy))
print('copy', id(my_dict))

print('!',my_dict) # {'name': 'Alice', 'age': 26, 'email': 'alice@example.com', 3.14: 'PI', ('test', 'test1'): 'brother'}
