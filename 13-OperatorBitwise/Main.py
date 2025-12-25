# Operator Bitwise, operasi biner/binary

a = 9
b = 5

# ! 1. Bitwise OR (|)
c = a | b
print("\n=======OR=======")
print("nilai: ", a, ", binary: ", format(a, "08b"))
print("nilai: ", b, ", binary: ", format(b, "08b"))
print('--------------------------(|)')
print("nilai: ", c, ", binary: ", format(c, "08b"))

# ! 2. Bitwise AND (&)
c = a & b
print("\n=======AND=======")
print("nilai: ", a, ", binary: ", format(a, "08b"))
print("nilai: ", b, ", binary: ", format(b, "08b"))
print('--------------------------(&)')
print("nilai: ", c, ", binary: ", format(c, "08b"))

# ! 3. Bitwise XOR (^)
c = a ^ b
print("\n=======XOR=======")
print("nilai: ", a, ", binary: ", format(a, "08b"))
print("nilai: ", b, ", binary: ", format(b, "08b"))
print('--------------------------(^)')
print("nilai: ", c, ", binary: ", format(c, "08b"))

# ! 4. Bitwise Not (~)
c = ~a
print("\n=======NOT=======")
print("nilai: ", a, ", binary: ", format(a, "08b"))
print('--------------------------(~)')
print("nilai: ", c, ", binary: ", format(c, "08b"))
print('--------------------------(^)')
d = 0b0000001001
e = 0b1111111111
print("nilai: ", e ^ d, ", binary: ", format(e^d, "08b"))

# ! 5. Shifting
# Shift Right
c = a >> 2
print("\n=======Shift Right=======")
print("nilai: ", a, ", binary: ", format(a, "08b"))
print('--------------------------(>>)')
print("nilai: ", c, ", binary: ", format(c, "08b"))
# Shift Left
c = a << 2
print("\n=======Shift Left=======")
print("nilai: ", a, ", binary: ", format(a, "08b"))
print('--------------------------(<<)')
print("nilai: ", c, ", binary: ", format(c, "08b"))
