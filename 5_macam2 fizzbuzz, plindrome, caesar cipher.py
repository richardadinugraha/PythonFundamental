# kota = ['jakarta', 'bandung', 'surabaya']
# i = 0 
# while i< len(kota):
#     print(kota[i])
#     i+=1

# for i in kota:
#     print (i)

# for i in range(len(kota)):
#     print(kota[i])

# x = 'purwadhika'
# for i in x:
#     print (i)

# for i in range (2, 10): #(2,10,2) dari 2 sampe 10 & longkap 2
#     if i == 6:
#         continue
#     print(i)
# else:
#     print ('OK')

# for i in range (1,10+1):
#     if i%2==0:
#         print ('wow')
#     else:
#         print (i)



# def fizzbuzz (n):
#     for i in range (1,n+1):
#         if i%3==0 and i%5==0:
#             print ('FizzBuzz')
#         elif i%3==0 :
#             print ('Fizz')
#         elif i%5==0:
#             print ('Buzz')
#         else:
#             print (i)

# fizzbuzz(15)

# def fizzbuzz_while(no):
#     angka = no
#     i = 0
#     while i < angka:
#         if i%3==0 and i%5==0:
#             print ('FizzBuzz')
#             i += 1
#         elif i%3==0 :
#             print ('Fizz')
#             i += 1
#         elif i%5==0:
#             print ('Buzz')
#             i += 1
#         else:
#             print (i)
#             i += 1
    
# fizzbuzz_while(15)

# x = list('1234567')
# x.reverse()
# print (x)
# print (x[::-1])
# print (list(reversed(x)))

# x.sort(reverse=True)
# print (x)
# print (x.sort(reverse=True))


# def vocal (kalimat):
#     kalimat = kalimat.lower()
#     kalimat = kalimat.replace('a','o')
#     kalimat = kalimat.replace('e','o')
#     kalimat = kalimat.replace('i','o')
#     kalimat = kalimat.replace('o','o')
#     kalimat = kalimat.replace('u','o')
#     print (kalimat)
# vocal('lintang')

# Salahhhhhhh
# a = 'lintang'
# b = {}
# for i in a:
#     huruf_vokal = (list('aiueo'))
#     if i in huruf_vokal = True:
#         i = 'o'
#         print (a)
#     else:
#         i= 'i'
#         print (a)

# x = list('1234657')
# y = ('andi', 'budi', 'caca')

# def reverse(mylist):
#     hasil = []
#     for i in range(len(mylist)):
#         hasil.insert(0,mylist[i])
#     return hasil

# print (reverse(x))

def ubahvokal(kata):
    output = ''
    for huruf in kata:
        if huruf in 'aiueo':
            output = output + 'o'
        else:
            output = output + huruf
    return output
print (ubahvokal('lintang'))
            
#Palindrome
# x = input('masukan kata: ')
# # x.reverse()
# # print (x)
# palindrome = (x[::-1]) == x
# print (palindrome)
# print (x[::-1]== x)
# if x[::-1] == x:
#     print ('sip')
# else:
#     print ('bukan')
# print (list(reversed(x)))

# x.sort(reverse=True)
# print (x)
# print (x.sort(reverse=True))
''''''
# x = input('masukan kata: ')
# kata = ''
# for i in range(len(x)-1,-1,-1):
#     kata += x[i]
#     if (kata==x):
#         print ('palindrome')
#     else:
#         print ('bukan')
''''''
# kalimat = 'hai aku lintang'
# kata = ''
# for i in range(len(kalimat)-1,-1,-1):
#     kata+= kalimat [i]
# # print (kata)

# kalimat_1= kalimat [::-1]
# print (kalimat_1)


# '''function membalikan tiap kata dari sebuah kalimat'''
# kalimat = 'hai aku lintang'
# a = kalimat.split()
# b = ''
# c = ''

# # cara pewe
# # for i in a:
# #     b += i [::-1]
# #     b += " "
# # ''''''

# for q in range(len(kalimat)-1,-1,-1):
#     c += kalimat[q]
# c = c.split() [::-1]
# d = ''
# for i in c:
#     d += i
#     d += ' '

# print (a)
# print (b)
# print (c)
# print (d)
# ''''''


# balik kalimat
# buat trasnlator morse!
morse_dict = { 'A':'.-', 'B':'-...',
    'C':'-.-.', 'D':'-..', 'E':'.', 
    'F':'..-.', 'G':'--.', 'H':'....', 
    'I':'..', 'J':'.---', 'K':'-.-', 
    'L':'.-..', 'M':'--', 'N':'-.', 
    'O':'---', 'P':'.--.', 'Q':'--.-', 
    'R':'.-.', 'S':'...', 'T':'-', 
    'U':'..-', 'V':'...-', 'W':'.--', 
    'X':'-..-', 'Y':'-.--', 'Z':'--..', 
    '1':'.----', '2':'..---', '3':'...--', 
    '4':'....-', '5':'.....', '6':'-....', 
    '7':'--...', '8':'---..', '9':'----.', 
    '0':'-----', ', ':'--..--', '.':'.-.-.-', 
    '?':'..--..', '/':'-..-.', '-':'-....-', 
    '(':'-.--.', ')':'-.--.-',' ':'/'}

# kalimat = input('Masukan kalimat : ').upper()
# output = ''
# for a in kalimat :
#     output += morse_dict[a]+' '
# print (output)

# caesar cipher
caesar_kalimat = input ('Masukan kalimat caesar : ')
alphabet = list ('abcdefghijklmnopqrstuvwxyz')
output = ''

for a in caesar_kalimat:
    index_huruf = alphabet.index(a)
    index_cipher = (index_huruf + (100 % 26))%26 
    output += alphabet[index_cipher]
print (output)

    


# print (nama.replace('tinggi', 'keren'))
# # menghitung huruf tanpa spasi
# print (len(nama.replace(' ', '').replace('&', '')))
''''''
# x = 'kuda balap'
# x = list (x[::-1])
# x = ''.join(x)

# print (x)