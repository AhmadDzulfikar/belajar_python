#Mengambil data user 

#data yang diinput pasti string
data = input("Masukkan Nama:")

print("Nama:", data, "type =", type(data))

#cara input data int
numbers = int(input("Masukkan angka:"))

print("Nomor =", numbers, "type:", type(numbers))

#cara input data 
numbers = float(input("Masukkan angka:"))

print("Nomor =", numbers, "type:", type(numbers))

#cara input nilai boolean
biner = bool(int(input("Masukkan nilai biner:"))) #dikasih tipedata int biar angka 0 bisa menjadi false

print("Nilai =", biner, "bertipe =", type(biner))

# etst