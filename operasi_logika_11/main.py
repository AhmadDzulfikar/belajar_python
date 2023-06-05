# Operasi Logika
# not, or, and, xor

# - - - - TABEL KEBENARAN - - - -

# NOT
print('====== NOT ======')
a = True
b = not a 
print('a =', a)
print('-----> Not')
print('b =', b)


# OR 
print('\n ====== Or ======') # Kalau ada true, hasilnya true
a = False
b = False
c = a or b
print(a, 'Or', b, '=', c)
a = False
b = True
c = a or b 
print(a, 'Or', b, ' =', c)
a = True 
b = False
c = a or b 
print(a, 'Or', b, ' =', c)
a = True 
b = True
c = a or b
print(a, 'Or', b, '  =', c)

# AND
print('\n ====== And ======') # yang hasilnya true cuman true ketemu true
a = False
b = False
c = a and b 
print(a, 'And', b, '=', c)
a = False 
b = True
c = a and b 
print(a, 'And', b, ' =', c)
a = True 
b = False 
c = a and b 
print(a, 'And', b, ' =', c)
a = True
b = True 
c = a and b 
print(a, 'And', b, '  =', c)

# XOR
print('\n ====== XOR ======') # semisal A & B nya beda hasilnya true
a = False 
b = False
c = a ^ b
print(a, 'XOR', b, '=', c)
a = False 
b = True
c = a ^ b 
print(a, 'XOR', b, ' =', c)
a = True
b = False 
c = a ^ b 
print(a, 'XOR', b, ' =', c)
a = True 
b = True 
c = a ^ b 
print(a, 'XOR', b, '  =', c)

# Ada lagi operasi logika yaitu NAND, NOR, XNOR