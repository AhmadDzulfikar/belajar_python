# Latihan perulangan membuat segitiga

sisi = 10

# 1. Menggunakan For

# dummy variable
print(10*'=', 'for', '='*10)

count = 1 
for i in range(sisi):
    print('*'*count)
    count += 1

# 2. Menggunakan While
print(10*'=', 'while', '='*10)
count = 1 
while True:
    print('*'*count)
    count += 1
    
    if count > sisi:
        break

# 3. hanya ganjil saja
print(10*'=', 'hanya ganjil', '='*10)
count = 1
while True:
    if (count%2):
        print('*'*count) # print jika ganjil
        count += 1

    else:
        # akan kembali ke atas jika ganjil
        count += 1
        continue

    
    # akan break jika cound > sisi
    if count > sisi:
        break
print('akhir dari while')

# 4. segitiga sama kaki
print(10*'=', 'segitiga sama kaki', '='*10)
count = 1
spasi = int(sisi/2)
ketupat = 1

while True:
    if (count%2):
        print(' '*spasi, '*'*count) # print jika ganjil
        count += 1
        spasi -= 1

    else:
        # akan kembali ke atas jika ganjil
        count += 1
        continue

    
    # akan break jika cound > sisi
    if count > sisi:
        break
print('akhir dari while')



