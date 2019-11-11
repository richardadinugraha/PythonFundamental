# #Python : lambda function > anonymous function

# x = lambda a,b,c:a+b+c
# print (x(2,3,4))

# def myfunction (x):
#     return lambda a:a**x
# pangkat3 = myfunction (3)

# # untuk memasukan fungsi anonim di dlam function

# x = lambda a:True if a %2 ==0 else False

# print (x(4))

# x=  lambda a: 'Angka Genap' if a%2==0 else 'Angka Ganjil'

# print (x(5))

#Map Phyton
# '''
# def y(a):
#     return len (a)

# a= ['Andi','Budi', 'Caca']
# x= map(y,a)
# print (x)
# print (list(x))
# '''

# a = ['Cokelat', 'Kiwi', 'Melon', 'Nanas']
# b = ['Apel', 'Jeruk', 'Nangka']
# def combi(a,b):
#     return a +' '+b
# x= map(combi,a,b)
# print(x)
# print(list(x))
''''''                                                                                                                                                                                                                              
# x = [2,4,6,8,10]
# def pangkat2(a):
#     return a ** 2
# y= map ([pangkat2],x)
# print (y)

# z= map (lambda a:a**2, x)
# print (list(z))

''''''
# x=range(11)

# def kurangLima(x):
#     if x<5:
#         return True
#     else:
#         return False
# y = filter (kurangLima, x)
# print (list (y))
# ''''''
# z= filter (lambda a:True if a>=5 else False, x)
# print (list(z))
''''''
# x = pow (2,2)
# y = pow (3,3)
# print (x)
# print (y)

# z= list(map(pow, [2,3],[2,3]))
# print (z)
# ''''''
# x=[1,2,3,4,99,10]
# y=[2,3,4,5,6,7]

# z= list(filter(lambda a:a in x, y))
# print (z)
# ''''''
from functools import reduce
# atau 
# import functools

angka = [1,2,3,4]
z = reduce(lambda x, y: str(x)+str(y), angka)

# z = fuunctools.reduce(lambda x, y: x*y, angka)
print (z)

kata = ['ini', 'ibu', 'budi']
print (''.join(kata))
z = reduce (lambda x,y:x+y, kata)
print (z)

z= list(filter(lambda a: a>3, map(lambda a : a*2, angka)))
print (z)


seratus = list(range (-100,101))
z = reduce(lambda a,b : a+b, map(lambda a:a*2, filter(lambda a : a%2==0,seratus)))
print (z)

# # import
# import functools 

z= list(filter (lambda a: a%5 or a==5, filter(lambda a: a%3 or a==3, filter(lambda a: a%2 or a==2, filter(lambda a: a>1,seratus)))))
print (z)

z= list(filter (lambda a: (a%7 or a==7) and (a%5 or a==5) and (a%3 or a==3) and (a%2 or a==2) and a>1,seratus))
print (z)

def prima(x):
    if x>1:
        for i in range (2,x):
            if x%i==0:
                return False
                break
            else:
                return True

def prima1(num):
   if num > 1:
       for i in range(2,num):
           if (num % i) == 0:
               return False
               break
       else:
           return True

print (prima1(81))
z= list (filter(prima1,range (1000)))
print (z)