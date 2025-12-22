# Operasi Aritmatika

a = 10
b = 3

# Operasi tambah +
hasil = a + b
print(a, "+", b, "=", hasil)

# Operasi pengurangan -
hasil = a - b
print(a, "-", b, "=" , hasil)

# Operasi Perkalian *
hasil = a * b
print(a, "*", b, "=", hasil)

# Operasi Pembagian /
hasil = a / b
print(a, "/", b, "=" , hasil)

# Operasi eksponen (pangkat) **
hasil = a ** b 
print(a, "**", b, "=", hasil)

# Operasi modulus (Sisa bagi) %
hasil = a % b
print(a, "%", b, "=", hasil) 

# Operasi floor division (dibulatkan dalam satuan) //
hasil = a // b
print(a, "//", b, "=", hasil) #10 // 3 = 3

# PRIORITAS OPERASI, OPERATIONAL PRESENDENCE

x = 3
y = 2
z = 4

""" 
Urutan Pengoperasian
    1. Kurung ()
    2. eksponen **
    3. perkalian , pembagian,  modulus, floor division * / % //
    4. Pertambahan dan pengurangan + -
"""

hasil = x ** y * z + x / y - y % z // x
print(x,"**",y,"*",z,"+",x,"/",y,"-",y,"%",z,"//",x, "=", hasil)

hasil = x + y * z 
print(x, "+", y, "*", z, "=", hasil)

hasil = 3 * 2 ** 3
print(hasil)

hasil = 3 * 6 // 4
print(hasil)

# Kurung mengambil langkah paling awal
hasil = (x + y) * z 
print("(",x, "+", y,")", "*", z, "=", hasil)