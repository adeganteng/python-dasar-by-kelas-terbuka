# Belajar Casting 
# Casting tipe data adalah merubah satu tipe data ke tipe lain
#  Tipe data = int, float, str, bool

## INTEGER
print("==== INTEGER ====")
data_int = 9
print("data= ", data_int, ", type= ", type(data_int)) #data=  9 , type=  <class 'int'>

data_float = float(data_int)
data_str = str(data_int)
data_bool = bool(data_int) # Akan bernilai false jika nilai int = 0
print("data: ", data_float, ", tipe: ", type(data_float)) # data:  9.0 , tipe:  <class 'float'>
print("data: ", data_str, ", tipe: ", type(data_str)) # data:  9 , tipe:  <class 'str'>
print("data: ", data_bool, ", tipe: ", type(data_bool)) # data:  True , tipe:  <class 'bool'>


## FLOAT
print("==== FLOAT ====")
data_float = 9.9 
print("Data: ", data_float, ", Tipe: ", type(data_float)) # Data:  9.9 , Tipe:  <class 'float'>

data_int = int(data_float) # Akan dibulatkan kebawah
data_str = str(data_float)
data_bool = bool(data_float) # akan false jika nilai float = 0
print("Data: ", data_int, ", Tipe: ", type(data_int)) # Data:  9 , Tipe:  <class 'int'>
print("Data: ", data_str, ", Tipe: ", type(data_str)) # Data:  9.9 , Tipe:  <class 'str'>
print("Data: ", data_bool, ", Tipe: ",type(data_bool)) # Data:  True , Tipe:  <class 'bool'>


## BOOLEAN
print("==== BOOLEAN ====")
data_bool = True
print("Data: ", data_bool, ", Tipe: ", type(data_bool)) # Data:  True , Tipe:  <class 'bool'>

data_int = int(data_bool) # bool = True => 1, bool = False => 0
data_str = str(data_bool)
data_float = float(data_bool) 
print("Data: ", data_int, ", Tipe: ", type(data_int)) # Data:  1 , Tipe:  <class 'int'>
print("Data: ", data_str, ", Tipe: ", type(data_str)) # Data:  True , Tipe:  <class 'str'>
print("Data: ", data_float, ", Tipe: ",type(data_float)) # Data:  1.0 , Tipe:  <class 'float'>


## STRING 
print("==== STRING ====")
data_str = "10"
print("Data: ", data_str,", Tipe: ", type(data_str)) # Data:  10 , Tipe:  <class 'str'>

data_int = int(data_str) # String harus berupa angka, kalau tidak angka maka akan error
data_float = float(data_str) # String harus berupa angka, kalau tidak angka maka akan error
data_bool = bool(data_str) # jika nilai string nya kosong maka akan False
print("Data: ", data_int, ", Tipe: ", type(data_int)) # Data:  10 , Tipe:  <class 'int'>
print("Data: ", data_float, ", Tipe: ", type(data_float)) # Data:  10.0 , Tipe:  <class 'float'>
print("Data: ", data_bool, ", Tipe: ", type(data_bool)) # Data:  True , Tipe:  <class 'bool'>