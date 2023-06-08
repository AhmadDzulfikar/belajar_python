# 1.) - - - - - 0 + + + + + 5 - - - - - 8 + + + + + 11 - - - - - -

# 2.) + + + + + 0 - - - - - 5 + + + + + 8 - - - - - 11 + + + + + +

'''KERJAKAN!!
        1.)'''

inputUser = float(input("Masukkan angka yang bernilai \n lebih dari 0 dan kurang dari 5 \n atau \n lebih dari 8 dan kurang dari 11 \n :"))

# lebih dari 0 dan kurang dari 5
lebihDari_0 = inputUser > 0
kurangDari_5 = inputUser < 5 
antara0dan5 = lebihDari_0 and kurangDari_5
print("\n lebih dari 0 dan kurang dari 5 =", antara0dan5)
# lebih dari 8 dan kurang dari 11 
lebihDari_8 = inputUser > 8 
kurangDari_11 = inputUser < 11
antara8dan11 = lebihDari_8 and kurangDari_11
print("\n lebih dari 8 dan kurang dari 11 =", antara8dan11)

hasil = antara0dan5 or antara8dan11
print("angka yang anda masukkan =", hasil)

print("\n", 10*"=", "\n")
''' KERJAKAN 
        2.)'''

inputUser = float(input("Masukkan angka yang bernilai \n antara 5 dan 8 \n atau \n lebih dari 11 \n :"))

# Antara 5 dan 8
kurangDari_0 = inputUser < 0 
print("\n kurang dari 0 =", kurangDari_0)
lebihDari_5 = inputUser > 5
kurangDari_8 = inputUser < 8
antara5dan8 = lebihDari_5 and kurangDari_8
print("\n lebih dari 5 kurang dari 8 =", antara5dan8)
# Lebih dari 11
lebihDari_11 = inputUser > 11
print("\n lebih dari 11 =", lebihDari_11)

hasil = kurangDari_0 or antara5dan8 or lebihDari_11
print("angka yang anda masukkan =", hasil)