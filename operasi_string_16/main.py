# Operasi dan manipulasi string 

# 1. menyambung string (concatenate)
nama_pertama = 'Ahmad'
nama_tengah = ' Dzulfikar'
nama_akhir = ' As Shavy'
nama_lengkap = nama_pertama + nama_tengah + nama_akhir
print(nama_lengkap)

# 2. menghitung panjang dari string
print('jumlah abjad dari', nama_lengkap , len(nama_lengkap))

# 3. operator untuk string

#mengecek apakah ada komponen char atau string di string 

A = 'a' 
status = 'a' in nama_lengkap
print (A + ' ada di ' + nama_lengkap + ' ' + 'adalah ' + str(status))

x = 'x'
status = 'x' in nama_lengkap
print(x + ' ada di ' + nama_lengkap + ' adalah ', str(status))

x = 'x'
status = 'x' not in nama_lengkap
print(x + ' tidak ada di', nama_lengkap, ' adalah ', str(status))

# mengulang string
print(10*' delf mapres ui ')

#indexing
print('index ke-0 : ' + nama_lengkap[0])
print('index ke-3 : ' + nama_lengkap[3])
print('index ke-4 : ' + nama_lengkap[4])
print('index ke-(-1) : ' + nama_lengkap[-1])
print('index ke 0:10 : ' + nama_lengkap[0:11])  
print('index ke 0,2,4,6,8,10 : ' + nama_lengkap[0:11:2])

# item paling kecil
print("paling kecil :", min(nama_lengkap))

# item paling besar
print("paling besar :", max(nama_lengkap))

ascii_code = ord(" ")
print("AASCII code untuk spasi adalah " + str(ascii_code))

data = 122
print('char untuk ASCII 122 adalah ' + chr(data))

# 4. Operator dalam bentuk method   
data = "udil surbakti"
jumlah = data.count('u')
print("jumlah u pada", data, 'adalah', jumlah)
