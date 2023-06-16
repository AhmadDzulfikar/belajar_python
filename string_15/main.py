data = "ini adalah string"
print(data)
print("tipe data ini adalah:", type(data))

# 1. Cara membuat string
'''
    1. dengan menggunakan single quote '...'
    2. dengan menggunakan double quote "..."
'''
sQuote = 'ini adalah contoh single quote'
print(sQuote)

dQuote = "ini adalah contoh double quote"
print(dQuote)

data = 'Andi berkata: "Halo, selamat pagi"'
datas = "ini adalah hari jum'at"
print(data, '\n',datas)

# 2. Menggunakan tanda \
print('besok adalah hari jum\'at') #membuat tanda ' menjadi string
print('g\'day, isn\'t it?')

# Backlash
print('C:\\Users\\Ahmad Dzulfikar') #pake double \ biar salah satunya keitung

# tab
print('satu \t satu \t aku sayang ibu') # \t memberi kesan tab

# backspace 
print('saya \bdan \banda') # \b memberi kesan backspace

# new line
print('pertama \nkedua')  # LF -> Line Feed -> untuk unix, linux, macbook
print('pertama \rkedua ') # CR -> Carriage Return -> bahasa lama/ sistem operasi lama
print('pertama\r\nkedua') #CRLF -> Carriage Return Line Feed -> untuk windows

# 3. Menggunakan raw string
print('C:\new folder')

#menggunakan raw string (r)
print(r'C:\new folder')
print(r'C\new folder \b \\ \t ')

# Multiline literal string
print("""
Nama : Ahmad Dzulfikar As Shavy
Kelas : 12 Rpl
""")

# Multiline literal string & RAW
print(r"""
Nama : Ahmad Dzulfikar As Shavy
Kelas : 12 Rpl\n Data Scientist
""")