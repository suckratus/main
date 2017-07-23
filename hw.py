import math
print("~"*30)
print("task1 a+b*(c/2)")
a = 2
b = 2
c = 4
x = a+b*(c/2)
print("result of is %d" %(x))
print("~"*30)
print("task2 (a+b)/12*c%4+b")
a = 2
b = 17
x = (a**2+b**2)%2
print("result  is %.d" %(x))
print("~"*30)
print("task3 (a+b)/12*c%4+b")
a = 2
b = 4
c = 2
x = (a+b)/12*c%4+b
print("result is %d " %(x))
print("~"*30)
print("task4 (a-b*c)/(a+b)%c")
a = 4
b = 3
c = 5
x = (a-b*c)/(a+b)%c
print(("result is %.2f" %(x)))
print("~"*30)
print("task5 |a-b|/(a+b)**3-cos(c)")
a = 10
b = 3
c = 7
if a > b and a != b:
    x = math.factorial(a - b) / (a + b) ** 3 - math.cos(c)
    print("result is %.2f" % (x))
else:
    print("error")
print("~" * 30)
print("task6 (ln(1+c)/-b)**4+|a|")
a = -1
b = 4
c = 8
if a >= 0 :
    x = (math.log(1+c)/-b)**4 +math.factorial(a)
    print("result si %.2f" % (x))
else:
    print("error")
print("~"*30)