# Latihan Konversi Suhu Temperatur

# Program konversi suhu celcius ke satuan lainnya

celcius = float(input("Masukan suhu dalam celcius: "))
print("Suhu adalah", celcius, "Celcius")

# Reamur
reamur = (4/5) * celcius
print("Suhu celcius dalam reamur adalah ", reamur, "Reamur")

# Fahrenheit
fahrenheit = ((9/5) * celcius) + 32
print("Suhu celcius dalam fahrenheit adalah ", fahrenheit, "Fahrenheit")

#  Kelvin 
kelvin = celcius + 273
print("Suhu celcius dalam kelvin adalah ", kelvin, "Kelvin")


# QUIZ CHALLENGE

#TODO: 1. Konversi Fahrenheit ke Kelvin
fahrenheit = float(input("Masukan suhu dalam fahrenheit: "))
# Cara 1
fahrenheitToCelcius = 5/9 * (fahrenheit - 32 )
celciusToKelvin = fahrenheitToCelcius + 273.15
print("Suhu fahrenheit ke Kelvin adalah: ", celciusToKelvin, "Kelvin")
# Cara 2
fahrenheitToKelvin = (fahrenheit - 32) * 5/9 + 273.15
print("Suhu fahrenheit ke Kelvin adalah: ", fahrenheitToKelvin, "Kelvin")

#TODO: 2. Konversi Kelvin ke Fahrenheit
kelvin = float(input("Masukan suhu dalam kelvin: "))
# Cara 1
kelvinToCelcius = kelvin - 273.15
celciusToFahrenheit = ((9/5) * kelvinToCelcius) + 32
print("Suhu Kelvin Ke Fahrenheit adalah: ", celciusToFahrenheit, "Fahrenheit") 
# Cara 2
kelvinToFahrenheit= (kelvin - 273.15) * 9/5 + 32
print("Suhu Kelvin Ke Fahrenheit adalah: ", kelvinToFahrenheit, "Fahrenheit") 


