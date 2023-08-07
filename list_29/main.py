# --- LIST ---


# kumpulan data numbers
data_angka = [1,2,4,3,4]
print(data_angka)

# kumpulan data string 
data_string = ["dzulfikar", "difa", "dina"]
print(data_string)

# kumpulan data boolean 
data_boolean = [True, False, True, False]
print(data_boolean)

# kumpulan data campuran
data_campuran = [1, 'aku sayang ibu', True, 2, 'juga sayang ayah', True]
print(data_campuran)

## cara alternatif membuat list
data_range = range(0,10,2) # range(start, stop, step)
print(data_range)
data_list = list(data_range)
print(data_list)

# membuat list dengan for loop, list comprehension 
data_list_for = [i**3 for i in range (0,10)]
print(data_list_for)

# membuat list pake for pake if
list_pake_for_if = [i for i in range(0,10) if i != 3]
print(list_pake_for_if)

# membuat list pake for pake if genap
list_pake_for_if_genap = [i for i in range(0,10) if i%2 == 0]
print(list_pake_for_if_genap)

# membuat list pake for pake if ganjil
list_pake_for_if_ganjil = [i for i in range(0,10) if i%2 != 0]
print(list_pake_for_if_ganjil)

# membuat list pake for pake if ganjil kuadrat
list_pake_for_if_genap = [i**2 for i in range(0,10) if i%2 != 0]
print(list_pake_for_if_genap)



#tess
#tes