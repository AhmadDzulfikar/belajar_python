# Date & Time (Latihan)

# Waktu Lahir : 08 08 1966
# Waktu Meninggal : 14 januari 2021

import datetime as dt

# Waktu Lahir
print("Silahkan maskkan tanggal, \nbulan dan tahun lahir anda")
tanggal = int(input("Tanggal \t:"))
bulan = int(input ("Bulan \t\t:"))
Tahun = int(input ("Tahun \t\t:"))

tanggal_lahir = dt.date(Tahun, bulan, tanggal)
print(f"tanggal lahir anda adalah : {tanggal_lahir}")
print(f"Hari lahir anda adalah {tanggal_lahir:%A}")

# Waktu Meninggal
print("\nSilahkan masukkan waktu meninggal")
tanggal_m = int(input("Tanggal Meninggal \t:"))
bulan_m = int(input('Bulan Meninggal \t:'))
tahun_m = int(input('Tahun Meninggal \t:'))

tanggal_meninggal = dt.date(tahun_m,bulan_m,tanggal_m)
print(f'tanggal meninggal adalah {tanggal_meninggal}')
print(f'Hari meninggal adalah {tanggal_meninggal:%A}')


print('\nTANGGAL HARI INI')
hari_ini = dt.date.today()
print(f'hari ini tanggal {hari_ini}')
umur_hari = hari_ini - tanggal_lahir
umur_haris = tanggal_meninggal - tanggal_lahir
umur_tahun = umur_haris.days // 365
umur_bulan_sisa = (umur_haris.days % 365) // 30
print(f'hari anda hidup adalah {umur_haris}')
print(f'umur anda adalah {umur_tahun} tahun,  {umur_bulan_sisa} bulan')