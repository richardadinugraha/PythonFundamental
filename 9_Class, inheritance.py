'''CLASS & OBJECT'''
# andi = {
#     'nama'= 'Andi',
#     'usia'= '21'
#         }

# budi = {
#     'nama'= Budi',
#     'usia'= '22'
# }

# Class>> membuat Cetakan untuk mencetak object

class Mobil:
    warna = "merah"
    tahun = 2010

#create object mobil1
# mobil1 = Mobil() 
# print (mobil1)
# print (mobil1.warna)
# print (mobil1.tahun)

# mobil2=Mobil()
# print (mobil1)
# print (mobil1.warna)
# print (mobil1.tahun)

# syntatic sugar .. misal  0.1 + 0.2 ga jadi 0.3

class MobilCustom():
    def __init__(self,warna,tahun, model):
        self.warna = warna
        self.tahun = tahun
        self.model = model
    # method
    def jadul (self):
        if self.tahun < 2010:
            return True
        else:
            return False
    # funtion lain
    def tes(self):
        print(self.warna,self.tahun,self.model,self.jadul())

mobilA = (MobilCustom('merah', 1998, 'GOKU'))
mobilB = (MobilCustom('merah', 2018, 'Gohan'))
print (mobilA.jadul())
''''''
print(mobilA.tes())
''''''
mobil1 = MobilCustom ('pink',2018, ['X'])
mobil2 = MobilCustom ('blue',2010, ['A','B'])

a = float (0.1)
b = float (0.2)
print (a+b)

print (mobil1.warna, mobil1.tahun, mobil1.model)

##################### Inheritance dalam class#### ambil dari class sebelumnya

class Car (MobilCustom):
    def __init__(self, soundSys):
        self.soundSys = soundSys   
        # pass

mobilx1 = MobilCustom('pink', 4, 'sport')
car1 = Car('black', 8, 'family', 'dolby')

print (mobilx1.warna, mobilx1.tahun)
print (car1.warna, car1.tahun)


