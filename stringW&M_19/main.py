# Width & Multiline

# Data

data_nama = 'Ahmad Dzulfikar'
data_umur = 17
data_tinggi = 172.0
data_nomor_sepatu = 42

# string standar
dataString = ' stringStandar '.center(30, '-')
print(dataString)
data_string = f'nama = {data_nama}, umur = {data_umur}, tinggi = {data_tinggi}, nomor sepatu = {data_nomor_sepatu}'
print(data_string)

# String Multiline (dengan menggunakan enter, newline, \n)
dataString = '\n'+' stringMultiline '.center(30, '-')
print(dataString)
data_string = f'nama = {data_nama}, \numur = {data_umur}, \ntinggi = {data_tinggi}, \nnomor sepatu = {data_nomor_sepatu}'
print(data_string)

# String Multiline (kutip triplets)
dataString = '\n'+' String kutip triplets '.center(40, '-')
print(dataString)

data_string = f"""nama = {data_nama}
umur = {data_umur}
tinggi = {data_tinggi}
ukuran sepatu = {data_nomor_sepatu}
"""
print(data_string)

# mengatur lebar 
dataString = '\n'+' String kutip triplets '.center(40, '-')
print(dataString)
data_tinggi = 180
data_string = f"""nama              = {data_nama}
umur          = {data_umur}
tinggi        = {data_tinggi}
ukuran sepatu = {data_nomor_sepatu}
"""
print(data_string)