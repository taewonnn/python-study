# 캐스팅 casting - 데이터의 자료형을 바꾸는 것

# int
a = 24
a_type = str(type(a))
# float으로 캐스팅
b = float(a)
b_type = str(type(b))
print(b_type) # <class 'float'>


# 다시 int로 캐스팅
c = int(b)
c_type = str(type(c))

# 💡 float을 int로 캐스팅하면 자동 내림
d = int(3.14)  # 3
d_type = str(type(d))

pass

# ⚠️ ValueError 발생
# wrong_1 = int("hello")
# wrong_2 = float("world")
# wrong_3 = int("3.14")