# continue, pass & break 

# pass -> dia berfungsi sebagai dummy 

# angka = 0 

# while angka < 5:
#     angka += 1
#     if angka == 3:
#         # print('OOMMAAGAA')
#         pass # ini tidak akan dieksekusi

#     print(angka)  

# continue 
angka = 0

print(f"angka sekarang -> {angka}")

while angka < 5:
    angka += 1
    print(f"angka sekarang -> {angka}") # aksi 1

    if angka == 3:
        print('sudah 3 nichh') 
        continue # continue akan membuat loop meloncat kembali ke awal

    print("mantapppp") # aksi 2

print("berhenti")