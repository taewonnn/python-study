# for - 반복문

# for i in range(반복횟수)
message = 'bmw!!'

for i in range(10):
  print(i)
  print(message)

# 0
# bmw!!
# 1
# bmw!!
# 2
# bmw!!
# 3
# bmw!!
# 4
# bmw!!
# 5
# bmw!!
# 6
# bmw!!
# 7
# bmw!!
# 8
# bmw!!
# 9
# bmw!!


# list / dictionary 하나씩 
list = ['bmw', 'k5', 'genesis']


# list length만큼 반복
for i in list:
  print(i)

# bmw
# k5
# genesis


for car in list:
  print(car + '!!!!')

# bmw!!!!
# k5!!!!
# genesis!!!!


# 0부터 3까지
for car in range(0,3):
  print('안녕')
  
# 안녕
# 안녕
# 안녕


dic = {
  '1': 111,
  '2': 222,
  '3': 333,
}

for u in dic:
  print(u)
  
# 1
# 2
# 3



# Ex.

print('==========')
for i in range(1,10):
  print(i *2)

print('==========')



# 이중 for문
for i in range(1,10):
  for a in range(1,10):
    print(a * i)

