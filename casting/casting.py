# Casting adalah merubah satu tipe data ke tipe lain

#tipe data ada str, int, float, bool

## STRING
print("=======STRING=======")
data_str = "3"
print("data:", data_str, "tipenya adalah", 
    type(data_str))

data_int = int(data_str)
data_float = float(data_str)
data_bool = bool(data_str)
print("data:", data_int, "tipenya adalah", 
    type(data_int))
print("data:", data_float, "tipenya adalah", 
    type(data_float))
print("data:", data_bool, "tipenya adalah", 
    type(data_bool)) #kalo misal data aslinya string hasilnya jadi true

## INT
print("=======INT=======")
data_int = 10
print("data:", data_int, "tipenya adalah", 
    type(data_int))

data_str = str(data_int)
data_bool = bool(data_int)
data_float = float(data_int)
print("data:", data_str, "tipenya adalah", 
    type(data_str))
print("data", data_bool, "tipenya adalah", 
    type(data_bool))
print("data:", data_float, "tipenya adalah",
    type(data_float))