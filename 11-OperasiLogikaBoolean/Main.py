# Operasi Logika atau Boolean

# ada: not, or, and, xor

# ! 1. NOT
print("====NOT====")
a = True
b = False
c = not a
d = not b
print("data a: ", a) # True
print("data b: ", b) # False
print("--------------NOT")
print("data c: ", c) # False
print("data d: ", d) # True


# ! 2. OR (Jika salah satu true, maka hasilnya adalah True)
print("====OR====")
a = False
b = False
c = a or b
print(a, "or", b , "=", c) # False

a = False 
b = True
c = a or b
print(a, "or", b, "=", c) # True

a = True
b = False
c = a or b
print(a, "or", b, "=", c) # True

a = True
b = True
c = a or b
print(a, "or", b, "=", c) # True


# ! 3. AND (Jika dua buah nilai True, maka hasilnya True, dan jika salah satu nilai bernilai False maka hasilnya akan False)
print("====AND====")
a = False
b = False
c = a and b
print(a, "and", b , "=", c) # False

a = False 
b = True
c = a and b
print(a, "and", b, "=", c) # False

a = True
b = False
c = a and b
print(a, "and", b, "=", c) # False

a = True
b = True
c = a and b
print(a, "and", b, "=", c) # True


# ! 3. XOR "^" (akan true jika salah satu True, sisanya False)
a = False
b = False
c = a ^ b
print(a, "XOR", b , "=", c) # False

a = False 
b = True
c = a ^ b
print(a, "XOR", b, "=", c) # True

a = True
b = False
c = a ^ b
print(a, "XOR", b, "=", c) # True

a = True
b = True
c = a ^ b
print(a, "XOR", b, "=", c) # False