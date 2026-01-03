# FORMAT STRING

#TODO: 1. Contoh Generic
# ! 1. string
nama = "Ucup"
# without_format = "Hello = " + nama
format_str = f"Hello {nama}"
print(format_str)


# ! 2. Boolean
boolean = True
format_str = f"Boolean = {boolean}"
print(format_str)

# ! 3. Angka/number
angka = 2005.5
# without_format = "angka = " + str(angka)
format_str = f"Angka = {angka}"
print(format_str)

# ! 4. Bilangan Bulat
angka = 15
format_str = f"Bilangan bulat = {angka:d}" # :d => jika angka berupa pecahan maka akan error, jadi yang ditampilin variabel angka harus berupa bilangan bulat
print(format_str)

# ! 5. Bilangan dengan ordo ribuan sampai juataan
ribuan = 2000
jutaan = 50000000
format_str= f"Ucup punya uang: {jutaan:,}, sedangkan dia punya: {ribuan:,}"
print(format_str)

# ! 6. Bilangan Desimal
angka = 2025.54321
format_str = f"Desimal: {angka:.2f}" # Desimal: 2025.54
print(format_str)
format_str = f"Desimal: {angka:.3f}" # Desimal: 2025.543
print(format_str)

# ! 7. Menampilkan leading zero
angka = 2025.54321
format_str = f"Desimal: {angka:010.3f}" # Desimal: 002025.543
print(format_str)

# ! 8. Menampilkan tanda + atau -
angka_minus = -10
angka_plus = 10
format_minus = f"Minus: {angka_minus:+d}"
format_plus = f"Plus: {angka_plus:+d}"
print(format_minus)
print(format_plus)

# ! 9. Memformat persen
persentase = 0.045
format_persen = f"persentase: {persentase:.2%}" # persentase=> Variabel, .2=> mau ambil berapa angka dibelakang titik, %+> memformat menjadi string
print(format_persen)

# ! 10. Melakukan operasi aritmatika didalam placeholder/"{....}
price = 50000
qty = 5
format_str = f"Harga total: Rp.{price*qty:,.2f}"
print(format_str)

# ! 11. Format angka lain (binary, octal, hex)
angka = 255
format_binary = f"Binary:: {bin(angka)}"
format_octal = f"Octal: {oct(angka)}"
format_hex = f"Hex: {hex(angka)}"

print(format_binary)
print(format_octal)
print(format_hex)
