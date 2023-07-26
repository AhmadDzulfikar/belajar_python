# latihan 

# kalkulator sederhana
print(30*"=")
print("Simple Calculator")
print(30*"=")

angka_1 = float(input("masukkan angka ke 1 = "))
operator = input("operator (+,-,*,/): ")
angka_2 = float(input("masukkan angka ke 2 = "))

# percabangannya 

if operator == "+":
    hasil = angka_1 + angka_2
    print(f"hasilnya adalah {hasil}")
elif operator == "-":
    hasil = angka_1 - angka_2
    print(f"hasilnya adalah {hasil}")
elif operator == "*":
    hasil = angka_1 * angka_2
    print(f"hasilnya adalah {hasil}")
elif operator == "/":
    hasil = angka_1 / angka_2
    print(f"hasilnya adalah {hasil}")

else: 
    print("Masukkan data yang bener")

print("Akhir dari program, terimakasih")