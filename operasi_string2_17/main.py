# operator  dalam bentuk methods

## merubah case dari string 

## merubah semua ke upper case 

print('upper')
salam = 'bro!!!'
print('normal = ' + salam)
salam = salam.upper()
print('upper =', salam)

print('\nlower')
kenalan = 'hAlLo gAys nAmA AkU dElf'
print('normal =',kenalan)
kenalan = kenalan.lower()
print('lower =', kenalan)

## pengecekan menggunakan isX method

# contoh untuk pengecekkan lower case 
salam = 'sist'
cek = salam.islower() # hasilnya bool
print(salam + ' is lower = ' + str(cek))

cek_upper = salam.isupper() # hasilnya bool 
print('"'+salam + '"' + ' is upper ? ' + str(cek_upper))

# islower & upper
# isalpha() <---- untuk mengecek semuanya huruf
# isalnum() <---- untuk mengecek huruf dan angka (mengecek password)
# isdesimal() <--- untuk mengecek semuanya angka
# isspace() <---- spasi, tab, newline (\n)
# istitle() <--- semua kata dimulai dengan huruf besar

print("\ncoba istitle")
judul = 'Hari Ini Badminton'
cek_title = judul.istitle() # hasilnya boolean
print("'" + judul + "'" + " is title? " + str(cek_title))
judul = 'Hari ini badminton'
cek_title = judul.istitle() # hasilnya boolean
print("'" + judul + "'" + " is title? " + str(cek_title))
judul = "Hari jum'at badminton"
cek_title = judul.istitle() # hasilnya boolean
print('"' + judul + '"' + " is title? " + str(cek_title))

# ngecek komponen startswith() endswith()
cek_start = 'Ahmad Dzulfikar As Shavy'.startswith('Ahmad')
print("Ahmad Dzulfikar As Shavy " + "start with Ahmad? " + str(cek_start))

cek_end = 'Ahmad Dzulfikar As Shavy'.endswith('Shavy')
print("Ahmad Dzulfikar As Shavy " + "end with Shavy? " + str(cek_end))

## penggabungan komponen join() split()
pisah = ['aku', 'adalah', 'orang', 'terkuat'] # [] = list, list adalah kumpulan data
print(pisah)

pisah = ['aku', 'adalah', 'orang', 'terkuat']
gabung = ' '.join(pisah)
print(gabung)

print('\nngubah kalimat menjadi list')
gabungan = 'gwnjirtadinjirketidurannjir'
print(gabungan.split('njir'))

## alokasi karakter
print(5*'=' + 'data' + '='*5)

## alokasi karakter rjust(),ljust(),center

kanan = "kanan".rjust(10)
print('"' + kanan + '"')

kiri = "'" + "kiri".ljust(10) + "'"
print(kiri)
tengah = "'" + "tengah".center(10) + "'"
print(tengah)

# tengah1 = "'" + 'tengah'.center(30, "-") + "'"
# print(tengah1)

tengah1 = ' tengahGaris '.center(30, "-")
print(tengah1)

# kebalikannya --> strip()
tengah1 = tengah1.strip("-") # menghilangkan tanda -
print("'" + tengah1 + "'")

kanan = kanan.strip()
print('"' + kanan + '"')

