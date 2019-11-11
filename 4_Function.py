#variabel , list, tuple, set, frozen set, dictionary
# if statement, loop
#function
# f(x) = 2x+2
# f(3) = 2(3) + 2

# def namafunction():
#     print ('Hello world')

# namafunction();namafunction();namafunction();
''' function yang bisa berhitung'''
# def mathfunction(x):  # x adalah parameter
#     print(x**2)
# mathfunction(2);mathfunction(3);mathfunction(4);
'''function bisa > 1 parameter.. (x,y,z,dst)'''
# def mathfunction(x,y):  # x adalah parameter
#     print(x**y)
# mathfunction(2,2);mathfunction(2,3);mathfunction(2,4);
'''integrasi input'''
# def pangkat (angka1,angka2):
#     print (angka1 ** angka2)
# pangkat (
#     float(input('Ketik angka 1: ')),
#     float(input('Ketik angka 1: '))
# )
'''function ganjil, genap'''
# def gangen (x):
#     if (x % 2) == 0:
#         print ('ini angka genap')
#     else:
#         print ('ini angka ganjil')

# gangen(
#     (input('Masukan angka: ')),
#     )
'''buat program'''
# 1. masukan angka 1
# 2. masukan operator aritmatika
# 3. masukan angka 2

# def matematika (x,y,op):
#     if op == '+':
#         print (x + y)
#     elif op == '-':
#         print (x-y)
#     elif op == '*':
#         print (x*y)
#     elif op == '/':
#         print (x/y)
#     else:
#         print('gagal menghitung')

# # matematika(2,3,'/')
# matematika (
#     float(input('masukan angka 1: ')),
#     float(input('masukan angka 2: ')),
#     input('masukan operator: '),
# )

# def calc():
#     x = float (input('masukan angka 1: '))
#     op = input('Masukan operator (+-*/)')
#     y =float (input('masukan angka 2: '))

'''variabel diluar function bisa kepanggil'''
# def tes(x):
#     print (x)
# tes(2)
# x=13

# student = ['Abi', 'Bayu', 'Celine']

# def tes (x):
#     print (x[0])
#     print ('Caca'in x)
# tes(student)

'''1 function ubah huruf vocal menjadi o'''
# def vocal (kalimat):
#     kalimat = kalimat.lower()
#     kalimat = kalimat.replace('a','o')
#     kalimat = kalimat.replace('e','o')
#     kalimat = kalimat.replace('i','o')
#     kalimat = kalimat.replace('o','o')
#     kalimat = kalimat.replace('u','o')
#     print (kalimat)
# vocal('Ikan Pari terbang')

'''# salah'''
    # for e in x:
    #     if e == 'o':
    #         print (e)
    #     elif e == 'a'or'e'or'i'or 'u':
    #         print ('o')
    #     elif e != 'a' or 'e' or 'i' or 'u' or 'o':
    #         print ('k')
'''Return function = menyimpan value /variabel'''
# def returnHello():
#     return 'Ambil String ini'

# print (returnHello())
''''''
# def gangen (x):
#     if (x % 2) == 0:
#         return 'ini angka genap'
#     else:
#         return 'ini angka ganjil'

# print (
# gangen(
#     float(input('Masukan angka: ')),
#     )
#     )
'''While condition'''
# i = 9
# while i <10 and i>5:
#     print (i)
#     i -= 1
''''''
# stud = ['andi','budi','caca',"deni"]
# index = 0
# while index <= len(stud)-1:
#     print (stud[index])
#     index = index +1
''''''
# x = [1,2,3,4,5,6,7,8,9,10]
# y = []
# z = 0
# while len(y) != len(x):
#     for i in x:
#         i = i ** 2
#         y.append(i)
# print (y)
''''''
# x = [1,2,3,4,5,6,7,8,9,10]
# y = []
# index = 0
# while index <= len(x)-1:
#     y.append(x[index]**2)
#     index +=1
# print (y)
''''''
'''BREAK dan CONTINUE'''
# break berhenti
# continue skip

# password1 = '12345'
# attempt = 0

# def password (input_password):
#     benar =0
#     if input_password == password1 :
#         print ('password benar')
#     else:
#         print ('password salah')


#PASSWORD
password = '12345'
inputuser = ''
attempt = 0
while inputuser != password and attempt <5:
    inputuser = input ('ketik password: ')
    if inputuser !=password:
        print ('password salah')
        attempt += 1
    else :
        print (' password benar')
        break

