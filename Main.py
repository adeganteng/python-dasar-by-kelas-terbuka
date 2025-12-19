import time
start_time = time.time()
print("Hello World")
print("Hello")
print("World")
print("Hello Guyss!")

# Ini adalah comment jadi tidak akan di eksekusi oleh programnya
a = 10 # Ini adalah variable + assignments kode hanya disimpan dalam memory dan akan dijalankan ketika sudah ada printahnya
"""
Ini adalah multiline comment
Multi line comment juga tidak akan dijalankan oleh program
"""
print(a)

for i in range(1, 1000):
    a = 10

print(time.time() - start_time, "detik")
# Kita bisa mengcompile python ke yang namanya bytecode
