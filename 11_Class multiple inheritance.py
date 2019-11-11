# class Manusia:
#     def __init__ (self, nama):
#         self.nama = nama

# class Pria (Manusia):
#     # pass
#     def __init__ (self, nama):
#         Manusia.__init__(self, nama)
#         self.gender= 'Laki-laki'

# class Wanita (Manusia):
#     # pass
#     def __init__ (self, nama):
#         Manusia.__init__(self, nama)
#         self.gender= 'perempuan'

# objA = Manusia('Andi')
# objB = Pria('Andi')
# objC = Wanita('Andi')

# print (vars(objA))
# print (vars(objB))
# print (vars(objC))

# # Multiple inheritance 

# class X:
#     def __init__ (self, x):
#         self.x = x
# class Y(X):
#     def __init__ (self, x,y):
#         X.__init__(self, x)
#         self.y= y
# class Z(Y):
#     def __init__ (self, x,y,z):
#         Y.__init__(self, x,y)
#         self.z= z

# objA = Z('a','b','c')
# print (vars(objA))

# Multiple inheritance tidak berhubungan
class X:
    def __init__ (self, x):
        self.x = x
class Y(X):
    def __init__ (self, y):
        self.y= y
class Z(Y):
    def __init__ (self, x,y, mcD):
        X.__init__(self, x)         #Property tergantung dari urutan
        Y.__init__(self, y)
        self.mcD= True

objA = Z('a','b','c')
print (vars(objA)) 
print (z.__mro___)