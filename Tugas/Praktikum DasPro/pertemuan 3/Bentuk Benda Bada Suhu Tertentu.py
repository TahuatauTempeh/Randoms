# Nama File   = Bentuk Air Pada Suhu Berbeda
# Nama        = Azka A. Maulana
# Tanggal     = 11 September 2024
# Deskripsi   = Membuat app yang dapat menentukan apakah sebuah air itu padat, cair, atau gas

# DEFINISI DAN SPESIFIKASI
# suhu_air_n_Celsius : integer -> string
#   [suhu_air_n_Celsius (x) adalah fungsi untuk menentukan apakah air pada 'x' derajat Celsius itu padat(es), cair, uap]

# REALISASI
def suhu_air_n_Celsius (x) :
    if x == x <= 0 :
        return print ("padat/es")
    elif x == x>=100 :
        return print ("uap")
    else :
        return print ("cair")

# APLIKASI

suhu_air_n_Celsius (0)
suhu_air_n_Celsius (100)