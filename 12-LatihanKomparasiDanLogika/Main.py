# Episode latihan logika dan komparasi

# ! 1. Membuat gabungan area rentang dari angka

# ++++3------10+++++++

inputUser = float(input("Masukan angka yang bernilai\nKurang dari 3\natau\nlebih besar dari 10\n: "))

#TODO 1. ++++3-----
# Memeriksa angka kurang dari 3
isKurangDari  = inputUser < 3
print( "Kurang dari 3: ",isKurangDari)

#TODO 2. ----10++++
# Memeriksa angka lebih dari 10
isLebihDari = inputUser > 10
print("Lebih dari 10: " ,isLebihDari)

#TODO 3. ++++3------10+++++++
isCorrect = isKurangDari or isLebihDari
print("Angka yang anda masukan: ", isCorrect)


print("\n", 10*"=", "\n")

# ! 2. Membuat irisan area rentang dari angka
# ----3++++10-----
inputUser = float(input("Masukan angka yang bernilai\nLebih dari 3\ndan\nkurang dari 10\n: "))

#TODO 1. ----3++++
# Lebih dari 3
isLebihDari = inputUser > 3
print("Lebih dari 3: ", isLebihDari)

#TODO 2. ++++10----
# Kurang dari 10
isKurangDari = inputUser < 10
print("Kurang dari 10: ", isKurangDari)

#TODO 3. ----3++++10-----
isCorrect = isKurangDari and isLebihDari
print("Angka yang anda masukan: ", isCorrect)