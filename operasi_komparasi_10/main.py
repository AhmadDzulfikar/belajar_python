# Operasi Komparasi 

# Setiap hasil dari operasi komparasi adalah boolean

# >, <, >=, <=, ==, !=, is, is not

a = 4
b = 2

# Lebih dari (>)
print("\n ======= Lebih dari (>) =======")
hasil = a > 3 #1
print(a, "> 3", "=", hasil)
hasil = b > 3 #2
print(b, "> 3 =", hasil )
hasil = b > 2 #3
print(b, "> 2 =", hasil) 

# Kurang dari (<)
print("\n ======= Kurang dari (<) =======")
hasil = a < 3 #1
print(a, "< 3", "=", hasil)
hasil = b < 3 #2
print(b, "< 3 =", hasil )
hasil = b < 2 #3
print(b, "< 2 =", hasil)


# Lebih dari sama dengan (>=)
print("\n ======= Lebih dari sama dengan(>=) =======")
hasil = a >= 3 #1
print(a, ">= 3", "=", hasil)
hasil = b >= 3 #2
print(b, ">= 3 =", hasil )
hasil = b >= 2 #3
print(b, ">= 2 =", hasil) 

# Kurang dari sama dengan (<=)
print("\n ======= Kurang dari sama dengan(<=) =======")
hasil = a <= 3 #1
print(a, "<= 3", "=", hasil)
hasil = b <= 3 #2
print(b, "<= 3 =", hasil )
hasil = b <= 2 #3
print(b, "<= 2 =", hasil)

# sama dengan (==)
print("\n ======= sama dengan(==) =======")
hasil = a == 3 #1
print(a, "== 3", "=", hasil)
hasil = b == 3 #2
print(b, "== 3 =", hasil )
hasil = b == 2 #3
print(b, "== 2 =", hasil)

# sama dengan (!=)
print("\n ======= sama dengan(!=) =======")
hasil = a != 3 #1
print(a, "!= 3", "=", hasil)
hasil = b != 3 #2
print(b, "!= 3 =", hasil )
hasil = b != 2 #3
print(b, "!= 2 =", hasil)

# 'is' sebagai komparasi object identity
print('======= Object Identity (is) =======')
x = 5 # ini adalah assignment membuat object 
y = 5
print('nilai x =', x, 'id =', hex(id(x)))
print('nilai y =', y, 'id =', hex(id(y)))
hasil = x is y 
print('x is y =', hasil ) 

x = 5 # ini adalah assignment membuat object 
y = 6
print('nilai x =', x, 'id =', hex(id(x)))
print('nilai y =', y, 'id =', hex(id(y)))
hasil = x is y 
print('x is y =', hasil )

# 'is not' sebagai komparasi object identity
print('======= Object Identity (is not) =======')
x = 5 # ini adalah assignment membuat object 
y = 5
print('nilai x =', x, 'id =', hex(id(x)))
print('nilai y =', y, 'id =', hex(id(y)))
hasil = x is not y 
print('x is not y =', hasil ) 

x = 5 # ini adalah assignment membuat object 
y = 6
print('nilai x =', x, 'id =', hex(id(x)))
print('nilai y =', y, 'id =', hex(id(y)))
hasil = x is not y 
print('x is not y =', hasil )