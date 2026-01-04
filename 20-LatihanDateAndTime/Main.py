# Date and Time

# Pengenalan sedikit tentang modul datetime di Python
import datetime as dt

# hari_ini = dt.date.today()
# print(hari_ini)
# print(f"Hari ini adalah hari = {hari_ini:%A}")

# tanggal = dt.date(2007,8,9)
# print(tanggal)
# print(f"Hari ini adalah hari = {tanggal:%A}")

#TODO: Latihan menghitung umur (tahun, bulan, hari) dari tanggal lahir
print("Silahkan masukan tanggal, bulan, dan tahun lahir Anda!")
tanggal = int(input("Tanggal \t= "))
bulan = int(input("Bulan \t\t= "))
tahun = int(input("Tahun \t\t= "))

tanggal_lahir = dt.date(tahun, bulan, tanggal)
print(f"Tanggal lahir anda adalah = {tanggal_lahir:%A, %d %B %Y}")

hari_ini = dt.date.today()
print(f"Hari ini tanggal = {hari_ini:%A, %d %B %Y}")

# Menghitung umur
umur_hari = (hari_ini - tanggal_lahir).days
umur_tahun = umur_hari // 365
umur_bulan = (umur_hari % 365) // 30
sisa_hari = (umur_hari % 365) % 30
print(f"Umur anda adalah {umur_tahun} tahun, {umur_bulan} bulan, dan {sisa_hari} hari.")

# Menghitung umur dalam jam
lahir = dt.datetime(tahun, bulan, tanggal)
jam_sekarang = dt.datetime.now()
umur_jam = (jam_sekarang - lahir).total_seconds() // 3600
print(f"Umur anda dalam jam adalah {int(umur_jam):,} jam.")



