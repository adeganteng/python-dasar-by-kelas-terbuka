# Tipe Data

# a = 10 , a adalah variabel dengan nilai 10

### TIPE DATA STANDAR ###

# Tipe data: A. Angka satuan yang ngga ada komanya (integer)
data_integer = 1 # data ini boleh 1 atau 1juta, atau 1 milyar, atau 344242, bebas yang penting tidak ada komanya (",")
print("data: ", data_integer, ", berupa: ", type(data_integer)) #data:  1 , berupa:  <class 'int'>


# Tipa data: B. Angka dengan koma (float)
data_float = 1.5
print("data: ", data_float, ", berupa: ", type(data_float)) #data:  1.5 , berupa:  <class 'float'>


# Tipe data: C. Kumpulan karakter (String)
data_string = "Ucup"
print("data: ", data_string, ", berupa: ", type(data_string)) # data:  Ucup , berupa:  <class 'str'>


# Tipe data: D. binner => True/False (boolean)
data_bool_true = True
print("data: ", data_bool_true, ", berupa: ", type(data_bool_true)) # data:  True , berupa:  <class 'bool'>
data_bool_false = False
print("data: ", data_bool_false, ", berupa: ", type(data_bool_false)) # data:  False , berupa:  <class 'bool'>


### TIPE DATA KHUSUS ###

# a. Bilangan Kompleks
data_complex = complex(5,6)
print("data: ", data_complex, ", berupa: ", type(data_complex)) # data:  (5+6j) , berupa:  <class 'complex'>

# Tipe data dari bahasa C (maksudnya bisa menggunakan tipe data dari bahasa C)
from ctypes import c_double
data_c_double = c_double(10.5)
print("data: ", data_c_double, ", berupa: ", type(data_c_double)) # data:  c_double(10.5) , berupa:  <class 'ctypes.c_double'>