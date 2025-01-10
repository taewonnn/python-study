# list - 자료형
students = ["egoing", "sori", "maru"]


print(students) # ['egoing', 'sori', 'maru']

grades = [2, 10 , 4, 10]

print(grades) # [2, 10, 4, 10]
print('grades[1]',grades[1]) #10

# len() 길이
print(len(grades)) # 4

# min() 최소값
print(min(grades)) # 2

# max() 최대값
print(max(grades)) # 10

print('-----')

car = ['k5', 'white', ['5000', '6000']]
print(car)
print(car[0]) # k5
print(car[1]) # white
print(car[2]) # ['5000', '6000']

car[1] = 'black'

print(car) # ['k5', 'black', ['5000', '6000']]


car2 = ['bmw 520','red', '100000']
print(car2.pop()) # 100000



# Dictionary - 객체
car3 = {
  'brand': 'kia',
  'model':'ddd', 
  'price':'10000' 
}

print(car3['brand']) # kia





# 통계 statistics
import statistics

# statistics.mean 평균값 
print(statistics.mean(grades)) # 6.5



# 랜덤 random
import random

print(random.choice(students)) # students 배열에 랜덤으로 하나 뽑아줌




