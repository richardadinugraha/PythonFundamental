'''
class X:
    def __init__ (self, nama):
        self.nama = nama
    
class Y(X):
    def __init__ (self,nama,gelar):
        X.__init__(self,nama)

class Y(X):
    def __init__ (self,nama,gelar, univ):
        X.__init__(self,nama)
        self.gelar = gelar
        self.kampus = univ
# class Y(X):
#     def __init__ (self, nama, gelar):
#         super().__init__(nama, gelar)

objX = X('Andi')
objY = Y('Budi', 'Dr', 'AtmaJaya')
objZ = Y('Ujang','S1', 'UI')
objZ.pacar = 'jomblo'
setattr(objZ, 'alamat', 'BSD')

print (objY.kampus)
print (getattr(objY, 'nama'))
print (hasattr(objY, 'pacar'))

from pprint import pprint
pprint (vars(objY))
print (vars(objY))
print (vars(objZ))

# delete
delattr(objZ, 'alamat')
print (vars(objZ))

del Y.nama #hapus attribute pada class, bukan object ya!
print (objY.kampus)
'''
# _________________
class student:
    def __init__(self, nama, usia, status):
        self.nama = nama
        self.usia = usia
        self.status = status


data = [
    {'nama':'Andi', 'usia': 21, 'status': 'jomblo'},
    {'nama':'Budi', 'usia': 21, 'status': 'jomblo'},
    {'nama':'Caca', 'usia': 21, 'status': 'jomblo'},
    {'nama':'Deni', 'usia': 21, 'status': 'jomblo'}
    ]

# dataA = []
# for a in data:
#     A= a.values()
#     nama = a.get('nama')
#     usia = a.get('usia')
#     status = a.get('status')
#     print (status)

# def createObj(x):
#     nama = x['nama']
#     vars()[nama]=student(x['nama'],x['usia'], x['status'])
#     return vars()[nama]

# def createObj(x):
#     return student(x['nama'], x['usia'], x['status']) #simplifikasi

# dataNew = map (func, iterable)
# dataNew = list(map (createObj, data))

dataNew = list(map(
    lambda x : student(x['nama'], x['usia'], x['status']), data)) #pake lambda function

# print (dataNew[0].nama) #pangggil namanya siapa
print (dataNew[0].nama)


# namaz = 'ultraman' # ultraman adalah isi variabel
# vars()[namaz] = 12345 #isi variabel diambil dijadikan variabel
# print (ultraman)