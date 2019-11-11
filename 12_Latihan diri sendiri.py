# num = int(input('enter number: '))
# for i in range (0,num+1):
#     for j in range (1,i+1):
#         print('*', end=' ')
#     print ()

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

# Piramida angka
# num = 5
# # for i in range (1,num+1):
# #     for j in range  (1,num-i+1):
# #         print (end=' ')
# #     for j in range (i,0,-1):
# #         print (j, end = '')
# #     for j in range (2, i+1):
# #         print (j,end= '')
# #     print ()

for i in range (5, 0, -1):
    for j in range (0,5-i):
        print (end= ' ')
    for j in range (0,i):
        print ('*', end=' ')
    print ()

# piramida * terbalik
# for i in range (num, 0, -1):
#     for j in range(0,num-i):
#         print (end=' ')
#     for j in range(0,i):
#         print ('*', end=' ')
#     print ()




