# Operasi Komparasi

# Setiap hasil dari operasi komparasi adalah boolean

# >, <, >=, <=, ==, !=, is, is not

a = 4
b = 2

# ! 1. Lebih Besar dari ">"
print("====Lebih besar dari (>)====")
hasil = a > 3 
print(a, ">", 3, "=", hasil) # True
hasil = b > 3 
print(b, ">", 3, "=", hasil) # False
hasil = b > 2 
print(b, ">", 2, "=", hasil) # False

# ! 2.  Kurang dari "<"
print("====Kurang dari (<)====")
hasil = a < 3 
print(a, "<", 3, "=", hasil) # False
hasil = b < 3 
print(b, "<", 3, "=", hasil) # True
hasil = b < 2 
print(b, "<", 2, "=", hasil) # False

# ! 3. Lebih dari sama dengan ">="
print("====Lebih dari sama dengan (>=)====")
hasil = a >= 3 
print(a, ">=", 3, "=", hasil) # True
hasil = b >= 3 
print(b, ">=", 3, "=", hasil) # False
hasil = b >= 2 
print(b, ">=", 2, "=", hasil) # True

# ! .4 Kurang dari sama dengan "<="
print("====Kurang dari sama dengan (<=)====")
hasil = a <= 3 
print(a, "<=", 3, "=", hasil) # False
hasil = b <= 3 
print(b, "<=", 3, "=", hasil) # True
hasil = b <= 2 
print(b, "<=", 2, "=", hasil) # True

# ! 5. Sama dengan (==)
print("====Sama Dengan (==)====")
hasil = a == 4
print(a, "==", 4, "=", hasil) # True
hasil = b == 4
print(b, "==", 4, "=", hasil) # False

# ! 5. Tidak sama dengan (!=)
print("====Sama Dengan (!=)====")
hasil = a != 4
print(a, "!=", 4, "=", hasil) # False
hasil = b != 4
print(b, "!=", 4, "=", hasil) # True

# ! 6. "is" sebagai komparasi object identity
print("====Object Identity (is)====")
x = 5 # Ini adalah assignment pembuat objec
y = 5
print("nilai x =", x, ", id = ", hex(id(x)))
print("nilai x =", y, ", id = ", hex(id(y)))
hasil = x is y
print("x is y =", hasil) # True

x = 5 # Ini adalah assignment pembuat objec
y = 6
print("nilai x =", x, ", id = ", hex(id(x)))
print("nilai x =", y, ", id = ", hex(id(y)))
hasil = x is y
print("x is y =", hasil) # False

# ! 6. "is" sebagai komparasi object identity
print("====Object Identity (is not)====")
x = 5 # Ini adalah assignment pembuat objec
y = 5
print("nilai x =", x, ", id = ", hex(id(x)))
print("nilai x =", y, ", id = ", hex(id(y)))
hasil = x is not y
print("x is not y =", hasil) # False

x = 5 # Ini adalah assignment pembuat objec
y = 6
print("nilai x =", x, ", id = ", hex(id(x)))
print("nilai x =", y, ", id = ", hex(id(y)))
hasil = x is not y
print("x is not y =", hasil) # True

