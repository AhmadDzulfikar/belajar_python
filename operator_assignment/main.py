# Operasi yang dapat dilakukan dengan penyingkatan

# Operasi ditambah denga assignment

a = 5 # adalah assignment
print("nilai a:", a)

a += 1 # artinya adalah nilai a + 1
print('nilai a += 1, nilai a menjadi:', a)

a -= 2 # artinya adalah nilai a - 2
print('nilai a -= 2, nilai a menjadi:', a)

a *= 2 # artinya adalah nilai a * 2
print('nilai a *= 2, nilai a menjadi:', a)

a /= 2 # artinya adalah nilai a / 2
print('nilai a /= 2, nilai a menjadi:', a)

print('\n======== Modulus ========')
b = 10
print('nilai b:', b)
b %= 3 # artinya adalah nilai b % 3 (Modulus)
print('nilai b %= 3, nilai b adalah:', b)

print('\n======== Floor Devision ========')
b = 10
print('nilai b:', b)
b //= 2 # artinya adalah nilai b // 2 (floor devision)
print('nilai b //= 2, nilai b adalah:', b)

print('\n======== Pangkat ========')
a = 2
print('nilai a:', a)
a **= 5
print('nilai a **= 5, nilai a menjadi:', a)



# OPERATOR BITWISE
# OR
print('\n======== OR ========')
c = True
print('nilai c:', c)
c |= True
print('nilai c |= False, nilai c menjadi:', c)
c = False
print('nilai c:', c)
c |= False
print('nilai c |= False, nilai c menjadi:', c)
c = False
print('nilai c:', c)
c |= True
print('nilai c |= True, nilai c menjadi:', c)
c = True
print('nilai c:', c)
c |= True
print('nilai c |= True, nilai c menjadi:', c)

# AND
print('\n======== AND ========')
c = True
print('nilai c:', c)
c &= False
print('nilai c &= False, nilai c menjadi:', c)
c = False
print('nilai c:', c)
c &= False
print('nilai c &= False, nilai c menjadi:', c)
c = False
print('nilai c:', c)
c &= True
print('nilai c &= True, nilai c menjadi:', c)
c = True
print('nilai c:', c)
c &= True
print('nilai c &= True, nilai c menjadi:', c)

# XOR
print('\n======== XOR ========')
c = True
print('nilai c:', c)
c ^= False
print('nilai c ^= False, nilai c menjadi: ', c)
c = False
print('nilai c:', c)
c ^= False
print('nilai c ^= False, nilai c menjadi: ', c)
c = False
print('nilai c:', c)
c ^= True
print('nilai c ^= True, nilai c menjadi: ', c)
c = True
print('nilai c:', c)
c ^= True
print('nilai c ^= True, nilai c menjadi: ', c)

