# Perulangan loop

# for kondisi:
#   aksi

# ini dengan list
angka2_list = [0, 1, 2, 3, 4, 5]

print(angka2_list)
for i in angka2_list:
    print(f'i sekarang {i}')
print('Akhir dari program 1 \n')

# ini dengan range
angka2_range = range(5)

for i in angka2_range:
    print(f'i sekarang -> {i}')
print('Akhir dari progrm 2 \n')

#  ini dengan range
angka2_range = range(1,5)

for i in angka2_range:
    print(f'i sekarang -> {i}')
print('Akhir dari program 3 \n')

# contoh 
for spam in angka2_range:
    print('Jangan males belajar')
print('Akhir program 4 \n')

# menggunakan string
data_str = "dzulfikar hebat"

for nama in data_str:
    print(nama)
print('Akhir dari pemrograman 5 \n')
