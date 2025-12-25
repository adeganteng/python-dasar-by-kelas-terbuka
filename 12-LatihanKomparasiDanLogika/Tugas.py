# Pekerjaan Rumah Komparasi dan Logika

# ! 1. ----0++++5-----8+++++11----
inputUser = float(input("Masukan angka: "))

#TODO 1. ----0++++
lebih_dari_nol = inputUser > 0
print("Lebih dari 0: ", lebih_dari_nol)

#TODO 2. ++++5----
kurang_dari_lima = inputUser < 5
print("Kurang dari 5: ", kurang_dari_lima)

#TODO 3. ----8++++
lebih_dari_delapan = inputUser > 8
print("Lebih dari 8: ", lebih_dari_delapan)

#TODO 4. ++++11----
kurang_dari_sebelas = inputUser < 11
print("Kurang dari 11: ", kurang_dari_sebelas)

#TODO 5: ----0++++5-----8+++++11----
isCorrect = (lebih_dari_nol and kurang_dari_lima) or (lebih_dari_delapan and kurang_dari_sebelas)
print("angka yang anda masukan: ", isCorrect)

# ! 2. ++++0----5++++8----11++++
inputUser = float(input("Masukan angka: "))

#TODO 1. ++++0----
kurang_dari_nol = inputUser < 0
print("Kurang dari 0: ", kurang_dari_nol)

#TODO 2. ----5++++
lebih_dari_lima = inputUser > 5
print("lebih dari 5: ", lebih_dari_lima)

#TODO 3. ++++8----
kurang_dari_delapan = inputUser < 8
print("kurang dari 8: ", kurang_dari_delapan)

#TODO 4. ----11++++
lebih_dari_sebelas = inputUser > 11
print("lebih dari 11: ", lebih_dari_sebelas)

#TODO 5: ++++0----5++++8----11++++
isCorrect = (kurang_dari_nol or lebih_dari_lima) and (kurang_dari_delapan or lebih_dari_sebelas)
print("angka yang anda masukan: ", isCorrect)
