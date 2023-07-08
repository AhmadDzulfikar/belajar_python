# format string

# contoh generic 
name = 'Ahmad Dzulfikar As Shavy'
format_str = f"hello {name}"
print(format_str)

# angka
angka = 2005
# format_str = "angka + " + str(angka)
format_str = f"angka = {angka}"
print(format_str)

# boolean
boolean = True
format_str = f'boolean = {boolean}'
print(format_str)

# bilangan bulat 
angka = 2005
format_str = f'angka = {angka:d}' # d = bilangan bulat 
print(format_str)

# bilangan dengan ordo ribuan 
angka =  2000000000
format_str = f'angka dengan koma = {angka:,}'
print(format_str)

# bilangan desimal
angka = 2005.0219289
format_str = f'desimal = {angka:.3f}'
print(format_str)

# menampilkan leading zero 
angka = 2005.46321
format_str = f'leading zero = {angka:9.3f}'
print(format_str)

# menampilkan tanda + atau -
angka_minus = -2500
angka_plus = 4000
format_minus = f"minus = {angka_minus:+d}"
format_plus = f'plus = {angka_plus:+.2f}'
print(format_minus)
print(format_plus)

# memformat persen
persentase = 0.100
format_persen = f'persentase dari 10 = {persentase:.3%}'
print(format_persen)

# didalem {} kita dapat melakukan operasi aritmatika dalam placeholder
harga = 20000
jumlah = 2
format_string = f'harga total adalah = Rp. {harga * jumlah:,}'
print(format_string)

# format angka lain (binary, octal, hexadecimal)
angka = 255
format_binary = f'binary = {bin(angka)}'
format_octal = f'octal = {oct(angka)}'
format_hex = f'hex = {hex(angka)} '

print(format_binary)
print(format_octal)
print(format_hex)