# Operator bitwise, operasi biner, binary

# OR (|), AND (&), XOR (^), NOT(~).

a = 5
b = 7

# Bitwise OR (|)
c = a | b 
print("\n ======OR======")
print('nilai :', a, 'binary :', format(a, '08b'))
print('nilai :', b, 'binary :', format(b, '08b'))
print('-------------------------------(|)')
print('nilai :', c, 'binary :', format(c, '08b'))

# Bitwise AND (&)
c = a & b 
print('\n ======AND======')
print("nilai :", a, 'binary :', format(a, '08b'))
print("nilai :", b, 'binary :', format(b, '08b'))
print("nilai :", c, 'binary :', format(c, '08b'))

# Bitwise XOR (^)
c = a ^ b 
print('\n ======XOR======')
print("nilai :", a, 'binary :', format(a, '08b'))
print("nilai :", b, 'binary :', format(b, '08b'))
print("nilai :", c, 'binary :', format(c, '08b'))

# Bitwise NOT (~)
c = ~a 
print('\n ======NOT======')
print("nilai :", a, 'binary :', format(a, '08b'))
print('----------------------------(~)')
print("nilai :", c, 'binary :', format(c, '08b'))
print('----------------------------(^)')
d = 0b00000110
e = 0b11111111
print('nilai :', e^d, 'binary :', format(e^d, '08b'))

# Shifting 

# Shift Right (>>)
c = a >> 2
print('\n ======>>======')
print("nilai :", a, 'binary :', format(a, '08b'))
print('----------------------------(>>)')
print("nilai :", c, 'binary :', format(c, '08b'))

# Shift Left (<<)
c = a << 2
print('\n ======<<======')
print("nilai :", a, 'binary :', format(a, '08b'))
print('----------------------------(<<)')
print("nilai :", c, 'binary :', format(c, '08b'))


#test