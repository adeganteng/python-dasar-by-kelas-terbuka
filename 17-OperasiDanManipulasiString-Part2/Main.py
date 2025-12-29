# Operator dalam bentuk methods

#TODO: Merubah case dari string
# ! 1. Merubah semua character ke UPPERCASE
salam = "bro!"
print("normal: " + salam)
salam = salam.upper()
print("upper: " + salam)

# ! 2. Merubah semua character ke lowercase
alay = "aKu KeCe aBiezzZzZzzzZZ"
print("normal: " + alay)
alay = alay.lower()
print("normal: " + alay)

#TODO: Pengecekan dengan isX method
# ! 1. contoh pengecekan lower case "islower()"
salam = "sist"
apakah_lower = salam.islower() # hasilnya bool
print(salam + " is lower = " + str(apakah_lower))

# ! 2. Contoh pengecekan uppercase "isupper()"
apakah_upper = salam.isupper() # hasilnya bool
print(salam + " is upper = " + str(apakah_upper))

# ! 3. isalpha() -> mengecek apakah semua karakter huruf (A–Z, a–z)
teks1 = "BelajarPython"
teks2 = "Belajar123"

print(teks1 + " is alpha = " + str(teks1.isalpha()))  # True
print(teks2 + " is alpha = " + str(teks2.isalpha()))  # False

# ! 4. isalnum() -> mengecek apakah hanya huruf dan angka (tanpa spasi/simbol)
teks1 = "Belajar123"
teks2 = "Belajar 123"

print(teks1 + " is alnum = " + str(teks1.isalnum()))  # True
print(teks2 + " is alnum = " + str(teks2.isalnum()))  # False (ada spasi)

# ! 5. isdecimal() -> mengecek apakah hanya angka desimal (0–9)
angka1 = "12345"
angka2 = "123.45"

print(angka1 + " is decimal = " + str(angka1.isdecimal()))  # True
print(angka2 + " is decimal = " + str(angka2.isdecimal()))  # False (ada titik)

# ! 6. isspace() -> mengecek apakah hanya berisi spasi, tab, atau newline
spasi1 = "   "
spasi2 = "  a  "

print("'" + spasi1 + "' is space = " + str(spasi1.isspace()))  # True
print("'" + spasi2 + "' is space = " + str(spasi2.isspace()))  # False

# ! 7. "istitle()" -> untuk mengecek apakah semua kata dimulai dengan huruf besar
judul = "It Is Okay Not To Be Orkay"
cek_judul = judul.istitle()
print(judul + " is title = " + str(cek_judul)) # True

judul = "It is Okay Not To Be Orkay"
cek_judul = judul.istitle()
print(judul + " is title = " + str(cek_judul)) # False

#TODO: Penecekan Komponen "startswith()" & "endswith()"
# ! 1. startswith()
cek_start = "Rangga Sudirman".startswith("Rangga")
print("start = " + str(cek_start)) # True

# ! 2. endswith()
cek_end = "Rangga Sudirman".endswith("sudirman")
print("End = " + str(cek_end)) # False

#TODO: Penggabungan dan pemisahan komponen join() & split()
# ! 1. join()
pisah = ['aku', 'sayang', 'kamu']
gabungan = ",".join(pisah)
print(pisah)
print(gabungan)

gabungan = ' '.join(pisah)
print(gabungan)

# ! 2. split()
gabungan = "Aku sayang kamu"
print(gabungan.split(" "))

#TODO: Alokasi karakter menggunakan ljust(), rjust(), & center()
# ! 1. ljust()
kiri = "kiri".ljust(10)
print("'"+kiri+"'")

# ! 2. rjust()
kanan = "kanan".rjust(10)
print("'"+kanan+"'")

# ! 3. center()
tengah = "tengah".center(20, "=")
print("'"+tengah+"'")

#TODO: Menghilangkan tanda yang di inginkan menggunakan "strip()"
kata = "::::::::::Ade::".strip(":")
print(kata)

#TODO: Lain-lain
# ! 1. replace() — Mengganti substring
kalimat = "Aku sayang kamu"
hasil = kalimat.replace("kamu", "Python")

print(hasil)  # Aku sayang Python

# ! 2. find() — Mencari posisi substring
kalimat = "Belajar Python itu menyenangkan"
posisi = kalimat.find("Python")

print("Posisi 'Python' =", posisi)  # 8

# ! 3. count() — Menghitung kemunculan substring
kalimat = "ha ha ha haha"
jumlah = kalimat.count("ha")

print("Jumlah 'ha' =", jumlah)  # 5

# ! 4. capitalize() — Huruf pertama jadi besar
teks = "python itu keren"
print(teks.capitalize())  # Python itu keren

# ! 5. title() — Setiap kata diawali huruf besar
judul = "belajar python dasar"
print(judul.title())  # Belajar Python Dasar

# ! 6. swapcase() — Menukar huruf besar ↔ kecil
teks = "Aku KeCe"
print(teks.swapcase())  # aKU kEcE 