import time

# time
a = time.time()
print(a)

# longtime
1000+121212131331313131

b = time.time()
print(b)
print(b-a)



# time.ctime()
c = time.time()
print(time.ctime(c))  # Tue Feb 18 15:52:15 2025




# time.localtime
print(time.localtime())  # time.struct_time(tm_year=2025, tm_mon=2, tm_mday=18, tm_hour=15, tm_min=55, tm_sec=23, tm_wday=1, tm_yday=49, tm_isdst=0)

print(time.localtime().tm_hour)
print(time.localtime().tm_year)
print(time.localtime().tm_min)




# time.strftime()
print(time.strftime())

