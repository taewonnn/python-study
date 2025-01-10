
# open

# 'w' 파일 열 떄 없으면 만들어서 open
file = open('a.txt', 'w')
file.close()


# write 
file1 = open('b.txt', 'w')
file1.write('test file')
file1.close()


# 'a' append모드 - 추가
file1 = open('b.txt','a')
file1.write('\naddd')
file1.close()

# close - file 열었으면 꼭 닫아줘아함


file3 = open('b.txt', 'r')
print(file3.read()) # test file
file3.close()



