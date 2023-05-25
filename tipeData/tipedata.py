# a = 10, a adalah variable dengan nilai 10 

# tipe data: angka satuan adalah (integer)
contoh_integer = 12
print("data:", contoh_integer, "adalah tipe data", 
    type(contoh_integer))

# tipe data: angka menggunakan koma adalah (float)
contoh_float = 1.3
print("data:", contoh_float, "adalah tipe data",
    type(contoh_float))

# tipe data: menggunakan ""/kumpulan karakter adalah (string)
contoh_string = "Pucay"
print("data:", contoh_string, "adalah tipe data", 
    type(contoh_string))

# tipe data: True/False (0/1) adalah (boolean)
contoh_boolean = True
print("data:", contoh_boolean, "adalah tipe data",
    type(contoh_boolean))

## Tipe data khusus

# bilangan kompleks
contoh_complex = complex(5,6) #j is imaginary numbers 
print("data:", contoh_complex, "adalah tipe data",
    type(contoh_complex))

# tipe data dari bahasa C
from ctypes import c_double, c_char

contoh_c_double = c_double(100.5)
print("data:", contoh_c_double, "adalah tipe data",
    type(contoh_c_double))