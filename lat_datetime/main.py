# Date and Time (Latihan)

import datetime as dt

hari_ini = dt.date.today()
print(hari_ini)

print(hari_ini)
print(f"Today is {hari_ini:%A}")

tanggal = dt.date(2005,9,19)
print(tanggal)
print(f"my born day in {tanggal:%A}")
