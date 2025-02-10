# while
# 주어진 조건을 충족시키는 동안 작업을 반복

i = 0

while i < 5:
    print(i)
    i += 1

# 0
# 1
# 2
# 3
# 4


my_list = ["apple", "banana", "cherry"]
i = 0

while i < len(my_list):
    print(my_list[i])
    i += 1
    
    

# break와 continue 사용 가능
i = 0

while i < 20:
    i += 1
    if i % 2 == 0:
        continue
    if i > 10:
        break
    print(i)
    
