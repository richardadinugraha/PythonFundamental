
#menghitung mean

baris = [1,1,5,2,2,2,2,2,2,2,2,2,2,2,4,4,4,3,7,9,15,10,10,10,10,10,10,11]
baris2 = list(range(1,1000))
def mean(listangka):
    suma=0
    for a in listangka:
        suma+= a
    mean = suma/len(listangka)
    return mean

def median(listangka):
    listangka.sort()
    freq = len(listangka)
    if freq %2 != 0:
        median = listangka[freq//2+1]
        return median
    else:
        median = (listangka[freq//2+1] + listangka[freq//2])/2
        return int(median)

def percentile(listangka,persentil):
    listangka.sort()
    freq = len(listangka)
    indexpersentil = int(freq * persentil/100)
    if freq %2 != 0:
        persentil = listangka[indexpersentil]
        return persentil
    else:
        persentil = ((listangka[indexpersentil] + listangka[indexpersentil+1])/2)
        return int(persentil)

def modus(listangka):
    freq = 0
    angka = 0

    for a in listangka:
        if listangka.count(a)>freq :
            freq = listangka.count(a)
            angka = a
    return angka

#     for a in (listangka):
        

print (mean(baris2))

print (median(baris))

print (modus(baris))

print (percentile(baris,10))

