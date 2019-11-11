'''List & Tupple
Tupple : immutable
List : mutable


list = [1,2,3]          >> mutable
tupple = (1, 2, 3)      >> immutable
Set/Himpunan = {1, 2, 3} >> no index, no duplicate elements
tidak ada elemen ke 0

'''
'''
x = {1,2,3,1,2,3}
# a = []
# for i in x:
#     a.append(i)
#     print (i)
# print (a)
# print (list(set(x)))

# x.add('a')
# print(x)

x.update('andi')
x.update('andi', 'z')
x.update('andi', [6,7,8])
print (x)
print ('budi' in x)

x.discard ('ujang') >> eror kalo ga ada
x.remove ('ujang')> ga error kalo ga ada
x.pop() >> ngapus elemen sesuai index
z.clear() >>
del z >> ilang sampe elemennya
'''
'''IRISAN, UNION, DIFFERENCE
a=list('abcde')
b=list('efghi')
a=set(a)
b=set(b)
print(a.intersection(b)) >> irisan
print(a&b)               >> irisan

print(a|b)               >> union/ gabungan
print(b|a)               >> union/ gabungan

print (a.difference(b))  >> selisih // a selisih b beda dgn b selisih a
print(a-b) selisih       >> selisih

print (a.symmetric_difference (b)) >> yang sama ilang, yg ga sama digabung
print (a^b)              >> symmetric difference
'''

'''
P = {1,2,4,7,9,19}
Q = {5,6,19,7,9,12,16,17}
R = {6,19,3,8}

print (P & Q)
print (P & Q | R)
print (P & Q ^ R)
print (P^R)
print (P-R)
'''
'''SEDEMIKIAN HINGGA'''
# P = (set (range(-4,5)))
# Q = (set (range(-7,2)))
# R = (set(range(-1,8)))
# S = (set (range(-9,10)))
# jawaban = (P|Q, P|R, Q|R)
# print (jawaban)
'''
Tuple = tuple('8935610')
tuple_set = list(Tuple)
print (tuple_set.reverse)
tuple_set.sort(reverse =True)
print (tuple_set)

S= (set(range(0,10)))
print (S)
'''
'''FROZEN SET adalah set yang seperti tupple
x = frozenset ([1,2,3])
x.add (2)
print (x, y)'''

'''
S= []
for i in range(0, 11) :
    S.append(i)
print (S)
'''
