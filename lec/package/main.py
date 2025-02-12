# myutils폴더에서 ~ import 파일명, 파일명
from myutils import greetings, arithmetics

hello_to_cheolsu = greetings.hello_to("철수")
add_3_4 = arithmetics.add(3, 4)

pass



# from myutils.greetings import *
# from myutils.arithmetics import add, subtract

# hello_to_cheolsu = hello_to("철수")
# add_3_4 = add(3, 4)
# subt_3_4 = subtract(3, 4)

# pass


from myutils.subutils import arith_print
from myutils.subutils.cars import Car

arith_print.divide(10, 3)
print(Car("삼성", "SM3").drive())