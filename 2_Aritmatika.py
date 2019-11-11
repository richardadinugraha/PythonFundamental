hari = ['senin', 'selasa', 'rabu', 'kamis', 'jumat', 'sabtu', 'minggu']

now = 'Rabu'
week = 7
totalDays = 100

currentIndex = hari.index(now.lower())
hariKe = (totalDays%week) + currentIndex
if(hariKe > 6):
    hariKe -= 7

print(f'{totalDays} hari dari hari {now} adalah hari {hari[hariKe]}')

### Hitung hari
JumlahHari = int(input('Masukkan jumlah hari :'))

year = 360
month = 30
week = 7
sisaHari = 0

jumlahYear =  jumlahHari//year
sisaHari = jumlahHari%year

jumlahMonth = sisaHari//month
sisaHari = sisaHari%month

jumlahWeek = sisaHari//week
sisaHari = sisaHari%week

print(f'{jumlahYear} Tahun, {jumlahMonth} Bulan, {jumlahWeek} Minggu, {sisaHari} hari')


### Kambing & Ayam
# 4 kambing + 2 ayam = 32
totalAnimal = 13
totalFeet = 32
animal1Feet = 2
animal2Feet = 4

divisor = abs(animal2Feet-animal1Feet)
if divisor == 0:
    divisor = 1

goat = abs((totalFeet - (totalAnimal*animal1Feet)))/divisor
print("Goat:", goat)

chicken = (totalFeet - (goat*animal2Feet))/animal1Feet
print("Cow:", chicken)


'''
    Sembilan belas tahun yang lalu, umur Anak setengah tahun lebih 
    muda dari seperempat umur Ibunya.
    Umur Anak sekarang 19 tahun lebih tua dari sepertujuh umur Ibunya.
    Berapa umur Ibu saat melahirkan Anaknya?
'''
'''
    Persamaan 1 : A - 19 = 1/4(B - 19) - 1/2
                  A      = 1/4B - 19/4 - 2/4 + 76/4
                  A      = 1/4B + 55/4
                  tahunKebelakang = 19
                  kurangUmur = 1/2
                  rasioIbu = 4
    Persamaan 2 : A > 1/7B + 19
    Substitusi  : 1/4B + 55/4 > 1/7B + 19
                  3/28B > 76/4-55/4
                  3/28B > 21/4
                  B > 21/4 * 28/3
                  B > 49
                  A > 1/7(49) + 19
                  A > 26
'''
    
'''
    Umur andi dan ayahnya sekarang jumlahnya 50 tahun, 4 tahun yang lalu,
    umur ayah 6 kali umur andi, umur andi dan umur ayahnya saat ini
    berturut-turut adalah:
'''

rasioIbu = 1/7
rasioAnak = 1/4
perbedaanTahun = 1/2
perbedaanUmur = 19

firstEq = (perbedaanUmur * rasioAnak) + perbedaanTahun
secondEq = rasioAnak - rasioIbu

umurIbu = int(firstEq/secondEq)

thirdEq = (((rasioAnak/rasioIbu)*perbedaanUmur) + ((perbedaanUmur * rasioAnak) + rasioAnak) - perbedaanUmur)
fourthEq = rasioAnak/rasioIbu - 1

umurAnak = int(thirdEq/fourthEq)

umurMelahirkan = umurIbu - umurAnak

print(f'Umur ibu = {umurIbu}, Umur anak = {umurAnak}, Umur ibu pada saat melahirkan = {umurMelahirkan}')

############

totalUmur = 50
rasioUmurAndi = 1
rasioUmurAyah = 6
jumlahTahun = 4

#umur4TahunLalu = (totalUmur-8)/(rasioUmurAndi+rasioUmurAyah)
#umurAndi = umur4TahunLalu+4
#umurAyah = 6*umur4TahunLalu+4

umurAyah = (rasioUmurAyah*(totalUmur-jumlahTahun)+jumlahTahun)/(rasioUmurAndi+rasioUmurAyah)
umurAndi = totalUmur - umurAyah

print(f'Umur Andi adalah {umurAndi}')
print(f'Umur Ayah adalah {umurAyah}')

