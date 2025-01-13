# csv

file = open("data.csv", "w")
file.write("김,이,박")
file.write("\n한,송,노")
file.close()


# Ex.
list = ["samsung", "kakao", "naver", "yahoo"]

file2 = open("list.txt", "w")
for i in list:
    file2.write(i + "\n")

file2.close()
