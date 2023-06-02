# Program konversi celsius ke satuan yang lain

print("\n PROGRAM KONVERSI TEMPERATURE \n")

celcius = float(input("masukkan suhu dalam celcius : "))
print("suhu adalah", celcius, "C")

#reamur
reamur = (4/5) * celcius
print("suhu celcius dalam reamur adalah : ", reamur, "R")

#Fahrenheit
fahrenheit = ((9/5) * celcius) + 32
print("suhu celcius dalam fahrenheit adalah : ", fahrenheit, "F")

#kelvin
kelvin = celcius + 273 
print("suhu celcius dalam kelvin adalah : ", kelvin, "K")