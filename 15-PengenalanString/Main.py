# Pengenalan String

data = "Ini adalah string"
print(data) # Ini adalah string
print(type(data)) # <class 'str'>

#TODO 1. Cara membuat string
# ! 1. Menggunakan single quote ('...')
data = 'Menggunakan single quote'
print(data)

# ! 2. Menggunakan double quote ("...")
data = "Menggunakan double quote"
print(data)

print('"Halo, apa kabar?"')
print("'Halo, apa kabar?'")
print("Ini adalah hari jum'at")

#TODO 2. Menggunakan tanda \
# ! 1. Membuat tanda ' menjadi string
print('Mari sholat Jum\'at') # Mari sholat Jum'at
print('g\'day, isn\'t it?') # g'day, isn't it?

# ! 2. Backlash
print("C:\\user\\usup") #C:\user\usup

# ! 3. Tab
print("Ucup\totong, jauhan!")# Ucup    otong, jauhan!

# ! 4. Backspace
print("Ucup \bOtong, jadi deketan!") #UcupOtong, jadi deketan!

# ! 5. Newline
print("Baris pertama.\nBaris kedua.") # LF -> Line Feed -> unix, macos, linux
print("Baris pertama.\rBaris kedua.") # CR -> Carriage Return -> commodore , acorn, lisp
print("Baris pertama.\r\nBaris kedua.") # CRLF -> Line Feed Carriage Return -> dipakai oleh windows

#TODO 3. String Literal atau raw
# ! 1. Raw string
# ingat hati-hati
print('C:\new folder') # akan salah pathnya, \n -nya kebaca menjadi newline
# mengunakan raw string
print(r"C:\new folder") # C:\new folder

# ! 2. Multiline Literal String
print("""
Nama: Ucup
Kelas: 3 SD
""")

# ! 3. Multiline Literal String dan Raw
print(r"""
Nama: Ucup
Kelas: 3 SD\new normal
Website: www.ucup.com/newID
""")