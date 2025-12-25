# Operator Assignment: operasi yang dapat dilakukan dengan penyingkatan.
# Maksudnya yaitu operasi ditambah dengan assignment


#TODO: A. UNTUK OPERASI ARITMATIKA 
a = 5 # ini adalah assignment
print("Nilai a: " , a)

# ! 1. Pertambahan 
a += 1 # Artinya adalah a = a + 1
print("Nilai a += 1, nilai a menjadi: " , a)

# ! 2. Pengurangan
a -= 2 # Artinya adalah a = a - 2
print("Nilai a -= 2, nilai a menjadi: " , a)

# ! 3. Perkalian
a *= 5 # Artinya adalah a = a * 2
print("Nilai a *= 5, nilai a menjadi: " , a)

# ! 4. Pembagian
a /= 2 # Artinya adalah a = a / 2
print("Nilai a /= 2, nilai a menjadi: ", a)

# ! 5. Modulus
b = 10
print("\nNilai b: ", b)
b %= 3
print("Nilai b %= 3, nilai b menjadi: ", b)

# ! 6. Floor Division
b = 10
print("\nNilai b: ", b)
b //= 3
print("Nilai b //= 3, nilai b menjadi: ", b)

# ! 5. Pangkat
a= 5
print("\nNilai a: " , a)
a **= 3
print("Nilai a **= 3, Nilai a menjadi: ", a)


#TODO: A. UNTUK OPERASI BITWISE

# ! 1. OR
c = True
print("\nNilai c: ", c)
c |= False
print("Nilai c |= False, Nilai c menjadi: ", c)
c = False
print("Nilai c: ", c)
c |= False
print("Nilai c |= False, Nilai c menjadi: ", c)

# ! 2. AND
c = True
print("\nNilai c: ", c)
c &= False
print("Nilai c &= False, Nilai c menjadi: ", c)
c = True
print("Nilai c: ", c)
c &= True
print("Nilai c &= True, Nilai c menjadi: ", c)

# ! 3. XOR
c = True
print("\nNilai c: ", c)
c ^= False
print("Nilai c ^= False, Nilai c menjadi: ", c)
c = True
print("Nilai c: ", c)
c ^= True
print("Nilai c ^= True, Nilai c menjadi: ", c)

# ! 4. Shifting
d = 0b0100
print("\nNilai d: ", format(d, "04b"))
d >>= 2
print("Nilai d >>= 2, nilai d menjadi: ", format(d, "04b"))
d <<= 1
print("Nilai d <<= 1, nilai d menjadi: ", format(d, "04b"))