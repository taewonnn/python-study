# 변수

last_name ='park'
first_name = 'taewon'
age = 20
married = False

print(last_name, first_name, age, married)


# f"{}"
print(f"저는 {age}살입니다.")
print(f"만으로는 {age - 1}살이죠.")
print("자격 : " + ("있음" if age > 20 else "없음"))
for candle in range(age):
    print("🕯️", end="")