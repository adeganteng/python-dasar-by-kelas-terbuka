# WIdth and Multiline

# Data
data_nama = "Ucup Sirukun"
data_umur = 28
data_tinggi = 150.5
data_nomor_sepatu = 44

# ! 1. String standard
print(5*"=", "Data String", 5*"=")
data_string = f"nama: {data_nama}, umur: {data_umur}, data tinggi: {data_tinggi}, data sepatu: {data_nomor_sepatu}"
print(data_string)

# ! 2. String multiline (dengan menggunakan enter, newline, \n)
print("\n"+5*"="+ "Data String"+ 5*"=")
data_string = f"nama: {data_nama},\numur: {data_umur},\ntinggi: {data_tinggi},\nsepatu: {data_nomor_sepatu}"
print(data_string)

# ! 3. String multiline (kutip triplets """...""")
print("\n"+5*"="+ "Data String"+ 5*"=")
data_string = f"""nama = {data_nama}
umur = {data_umur}
tinggi = {data_tinggi}
sepatu = {data_nomor_sepatu}
"""
print(data_string)

# ! 4. Mengatur lebar
print("\n"+5*"="+ "Data String"+ 5*"=")

# semisal kita mau alignment teks di kanan
data_nama = "Ucup"
data_string = f"""
nama   = {data_nama:>5}
umur   = {data_umur:>5}
tinggi = {data_tinggi:>5}
sepatu = {data_nomor_sepatu:>5}
"""
print(data_string)
