# Nama File   = Fungsi besaran Derajat
# Nama        = Azka A. Maulana
# Tanggal     = 09 September 2024
# Deskripsi   = Tuliskanlah sebuah fungsi yang menerima suatu besaran dalam dalam derajat Celcius dan kode konversi ke derajat Reamur, Fahrenheit atau Kelvin, dan mengirimkan nilai derajat sesuai kode konversi


# DEFINISI DAN SPESIFIKASI 
# temperature_in_Celcius_to_Others : real,char - > real
#   {temperature_in_Celcius_to_Others(x,y) untuk menghitung hasil suhu dari Celcius ke Fahrenheit (F), Reamur (R), dan Kelvin (K)}

# REALISASI
def temperature_in_Celcius_to_Others (x,y) :
    if y == 'F' :
        return (x * 9/5) + 32
    elif y == 'R' :
        return 4/5 * x
    elif y == 'K' :
        return x + 273
    
#APLIKASI
print(temperature_in_Celcius_to_Others(35,'F'))
print(temperature_in_Celcius_to_Others(35,'R'))
print(temperature_in_Celcius_to_Others(35,'K'))