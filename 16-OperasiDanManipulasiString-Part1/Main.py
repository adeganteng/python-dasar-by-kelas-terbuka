# Operasi dan Manipulasi String

# ! 1. Menyambung String (concatenate)
nama_pertama = "ucup"
nama_tengah = "D"
nama_akhir = "Fame"

nama_lengkap = nama_pertama +" " + nama_tengah + "'" +nama_akhir
print(nama_lengkap)

# ! 2. Menghitung panjang string
panjang = len(nama_lengkap)
print("Panjang dari " + nama_lengkap + " = " + str(panjang))

# ! 3. Operator untuk string
# Mengecek apakah ada komponen char atau string di string 
# Jika ingin mengecek jika ada maka menggunakan "in"
d = "d"
status = d in nama_lengkap
print(d + " ada di " + nama_lengkap + " = " + str(status))
D = "D"
status = D in nama_lengkap
print(D + " ada di " + nama_lengkap + " = " + str(status))

# Jika ingin mengecek jika tidak ad maka menggunakan "not in"
d = "d"
status = d not in nama_lengkap
print(d + " ada di " + nama_lengkap + " = " + str(status))

# Mengulang String
print("wk"*10)
print(10*"ck")

# Indexing
print("Index ke-0: " + nama_lengkap[0])
print("Index ke-6: " + nama_lengkap[6])
print("Index ke-(-1): " + nama_lengkap[-1])
print("Index ke-(-2): " + nama_lengkap[-2])
print("Index ke-[0:3]: " + nama_lengkap[0:4]) # dibaca => yaitu diambil dari index 0 sampai dengan 4 tetapi index ke 4 tidak diikutkan
print("Index ke-[3:7]: " + nama_lengkap[3:8])
print("Index ke-[0,2,4,6,8,10]: " + nama_lengkap[0:11:2]) # dibaca => yaitu mengambil string pada index ke 0, 2, 4, 6, 8, 10 [index pertama:indexterakhir:increment]

# Mencari item paling kecil
print("Paling kecil: " + min(nama_lengkap))

# Mencari item paling besar
print("Paling besar: " + max(nama_lengkap))

# Maksud dari mencari  item paling besar atau kecil
ascii_code = ord(" ")
print("ASCII code untuk spasi adalah: ", str(ascii_code))
data = 117
print("char untuk ASCII 117 adalah: " + chr(data))

# ! 4. Operator dalam bentuk method
data = "otong surotong pararotong"
# Menghitung jumlah karakater tertentu pada data
jumlah = data.count("o")
print("jumlah o pada " + data + " = " + str(jumlah))