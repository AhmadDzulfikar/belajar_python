# Date & Time (Latihan)
import datetime as dt

print("Silahkan maskkan tanggal, \nbulan dan tahun lahir anda")
tanggal = int(input("Tanggal \t:"))
bulan = int(input ("Bulan \t\t:"))
Tahun = int(input ("Tahun \t\t:"))

tanggal_lahir = dt.date(Tahun, bulan, tanggal)
print(f"tanggal lahir anda adalah : {tanggal_lahir}")
print(f"Hari lahir anda adalah {tanggal_lahir:%A}")

print('\nTANGGAL HARI INI')
hari_ini = dt.date.today()
print(f'hari ini tanggal {hari_ini}')
umur_hari = hari_ini - tanggal_lahir
umur_tahun = umur_hari.days // 365
umur_bulan_sisa = (umur_hari.days % 365) // 30
print(f'hari anda hidup adalah {umur_hari}')
print(f'umur anda adalah {umur_tahun} tahun,  {umur_bulan_sisa} bulan')