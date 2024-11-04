# Nama File   = aritmatika perpangkatan
# Nama        = Azka A. Maulana
# NIM         = 24060124140195
# Tanggal     = 30 September 2024 (tanggal mulai menulis di VsCode)
# Deskripsi   = fungsi rekuren aritmatika perpangkatan

# DEFINISI DAN SPESIFIKASI
# power_to : 2 integer > 0 -> integer > 0
#   {power_to(x, y) adalah fungsi untuk menghitung perpangkatan rekursif dengan mengalikan x sebanyak y kali}

# REALISASI
def power_to(x,y) :
    if y == 1 :
        return x
    else :
        return (power_to(x,y - 1) * x)
    
# APLIKASI
print(power_to(2,3))
print(power_to(4,2))
print(power_to(6,2))