import datetime as dt

x=dt.datetime.now()
# print (x.strftime('%d'))   # tanggal
# print (x.strftime('%A'))   # hari
# print (x.strftime('%m'))   # bulan
# print (x.strftime('%B'))   # nama bulan
# print (x.strftime('%Y'))   # tahun

# print (x.strftime('%H'))   # 24 jam 
# print (x.strftime('%I'))   # 12 jam
# print (x.strftime('%p'))   # am / pm
# print (x.strftime('%M'))   # min
# print (x.strftime('%S'))   # sec

# print (x.strftime('%c'))
# print (x.strftime('%x'))
# print (x.strftime('%X'))

# print (x.strftime('Sekarang jam %H:%M:%S WIB'))


# # Buat file python isinya class tanggal

dict_hari = {
    'monday': 'senin',
    'tuesday' : 'selasa',
    'wednesday': 'rabu',
    'thursday' : 'kamis',
    'friday' : 'jumat',
    'saturday' : 'sabtu',
    'sunday' : 'minggu'
}

class waktu:
    def __init__ (self):
        self.day = dict_hari.get(x.strftime('%A').lower())
        self.date = x.strftime('%d')
        self.month = x.strftime('%B')
        self.year = x.strftime('%Y')
        self.hour = x.strftime('%H')
        self.min = x.strftime('%M')
        self.sec = x.strftime('%S')

objWaktu = waktu()
# objwaktu = waktu()
print (vars(waktu()))
print(vars(objWaktu))

# dict_bulan = {

