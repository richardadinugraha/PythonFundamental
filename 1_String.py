# PR hitung julah huruf 'c' dan kata 'startup'
nama = 'Purwadhika Startup & Coding School'
countc = nama.count('c')
countstartup = nama.count('Startup')
findc = nama.find('h')
countspace = nama.count(' ')

print (str(countstartup)*3)
print (countc)
print (findc)
print (countspace)

#######################
#Jumlah huruf
#1st method - For Loop
count = 0
for i in nama.lower():
    if(i == 'c'):
        count = count + 1
print('Jumlah c : ', count)

#2nd method - Count
count = 0
count = nama.lower().count('c')
print('Jumlah c 2nd method: ', count)

#3rd method - If Expression
count = 0
temp = nama.lower().index('c')
if(temp > 0):
    count = count + 1
temp = nama[temp:len(nama)].index('c')
if(temp > 0):
    count = count + 1
print('Jumlah c 3rd method: ', count)

#4th method
cari = 'c'
x = nama.lower().replace(cari, '')
print(x)
jumlahCari = len(nama) - len(x)
print(f'Jumlah huruf \'{cari}\' ada = {jumlahCari}')

#Jumlah kata startup
#1st method
wordCounter = nama.lower().count('startup')
print('Jumlah kata startup :', wordCounter)

#2nd method
yangDicari = 'startup'
x =  nama.lower().replace(yangDicari, '')
jumlahCari = len(nama) -  len(x)
print(f'Jumlah kata \'{yangDicari}\' ada = {int(jumlahCari/len(yangDicari))}')


''' def cariIndex(list, i):
        return [x for x, y in enumerate(list) if y == i]
        print(cariIndex(a, 3))
'''