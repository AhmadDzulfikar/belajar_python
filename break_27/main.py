# break

# break + input
angka = 0 

data_int = int(input("hitung sampai = "))

while True:
    angka += 1
    print(f"angka sekarang -> {angka}")

    if angka == data_int:
        print(f'angka sudah {data_int}')
        break

    print('lanjuttt')

print('selesai')


# break + yang biasa
# angka = 0 

# while angka < 6:
#     angka += 1
#     print(f"angka sekarang -> {angka}")

#     if angka == 4:
#         print(f'angka sudah {angka}')
#         break

#     print('lanjuttt')

# print('selesai')