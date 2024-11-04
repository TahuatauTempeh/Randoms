# Nama File   = aritmatika pembagian
# Nama        = Azka A. Maulana
# NIM         = 24060124140195
# Tanggal     = 30 September 2024 (tanggal mulai menulis di VsCode)
# Deskripsi   = fungsi rekuren aritmatika pembagian

# DEFINISI DAN SPESIFIKASI
# division : 2 integer > 0 -> integer > 0
#   {division(x,y) adalah fungsi untuk membagi x dengan y selama nya sampai y = 0, dimana fungsi akan menyebut variabel x}

# REALISASI
def division(x,y) :
    if y == 0 :
        return x 
    else :
        return round((division(x,y - 1) / y), 3)
    
# APLIKASI
print(division(8,2))
print(division(7,5))
print(division(8,6))

# division(x,y) :   x , y = 0
                    # (x,y-1) / y , y > 0

# basis , rekursi
