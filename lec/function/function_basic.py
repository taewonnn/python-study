# function

# 1. 반복될 수 있는 작업을 정의
# 2. input을 받아 output을 반환


def my_func():
    print("!!")
    print("~~")
    

my_func()
my_func()
my_func()



# parameter
def mult_5_and_print(x):
    print(x *5)
    

mult_5_and_print(3)  # 15
mult_5_and_print('ha')  # hahahahaha



def add(x, y):
    print(f"{x}와 {y}를 더합니다.")
    return x + y


add_1 = add(2, 3) # 5
add_2 = add("hi", "YYY")

add_3 = add(add(2, 3), add(4, 5))
print(add_3) # 14



# 주어진 리스트 중 정수만 골라 총합, 개수, 평균 반환
def get_stats(lst):

    total = 0
    item_count = 0

    for item in lst:
        if not isinstance(item, int):
            continue
        total += item
        item_count += 1
    average = total / item_count

    # 튜플로 반환
    return item_count, total, average


my_list = [1, 2, "가", 3, 3.14, 4, (1, 2), 5, "Hello"]
l_count, l_total, l_avg = get_stats(my_list)

print(get_stats(my_list)) # (5, 15, 3.0)
