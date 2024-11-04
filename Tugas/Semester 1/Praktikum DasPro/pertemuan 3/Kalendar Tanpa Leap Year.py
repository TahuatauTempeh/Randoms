# Nama File   = Kalendar tanpa Leap Year
# Nama        = Azka A. Maulana
# Tanggal     = 09 September 2024
# Deskripsi   = Buat day counter tanpa Leap Year

# DEFINISI DAN SPESIFIKASI
# hari_kalender : int [1...31], int [1...12], int [0...9999] -> int [1...365]
#   {hari_kalendar(d,m,y) dari suatu tanggal (d,m,y) tanpa Leap Year}
# total_days_after_x_months : int [1...12] -> int [1..36]
#   {total_days_after_x_months(n) adalah jumlah hari pada tanggal 1 bulan (n)}

# REALISASI
def hari_kalendar (d,m,y) :
    if m == 1 :
        total_days_after_x_month = 1
    elif m == 2 :
        total_days_after_x_month = 32
    elif m == 3 :
        total_days_after_x_month = 60
    elif m == 4 :
        total_days_after_x_month = 91
    elif m == 5 :
        total_days_after_x_month = 121
    elif m == 6 :
        total_days_after_x_month = 152
    elif m == 7 :
        total_days_after_x_month = 182
    elif m == 8 :
        total_days_after_x_month = 213
    elif m == 9 :
        total_days_after_x_month = 244
    elif m == 10 :
        total_days_after_x_month = 274
    elif m == 11 :
        total_days_after_x_month = 305
    elif m == 12 :
        total_days_after_x_month = 335

    return total_days_after_x_month + d - 1

# APLIKASI

print(f"{hari_kalendar (2,6,2000)} days" )