# # Translator bahasa > morse dan sebaliknya

# def star(x):
#     output =''
#     for i in range(x):
#         output += ('*')
#         print (output)

# star(5)

# def rstar (x):
#     star = ''
#     for i in range (x):
#         star = '*'* (x-i)
#         print(star)

# rstar(5)

# def hitung(x):
#     hitung=[]
#     for i in range (x+1):
#         hitung.append(i)
#         b = ''
#         for a in str(hitung):
#             b += a
#         print (b)
# hitung(5)

# def iseng(x,y):
#     a= ''
#     for i in range (x,y+1):
#         a += str(i)
#         print (a)


# def iseng2 (x,y):
#     for i in range (x,y+1):
#         a = (str(i)+' ') * i
#         print (a)
# iseng2 (1,5)

# def terbalik(x,y):
#     a = 0
#     for i in range (x,y):
#         a = y-i
#         print (a* (a+1))
# terbalik(0,5)

# import math
# print (math.pow(2,3))
def power (x,y):
    a= y
    x1 = x
    while a!= 1:
        x1 = x1*x
        a-=1
    print (x1)

power(2,3)

# recursive function
def pangkatB(x,y):
    if (y==1):
        return x
    else:
        return x * pangkatB(x,y-1)
print (pangkatB(2,3))

# faktorial
def faktorial(x):
    if (x==1 or x==0):
        return 1
    else:
        return x * faktorial(x-1)
print (faktorial(6))

import math
print (math.factorial(6))