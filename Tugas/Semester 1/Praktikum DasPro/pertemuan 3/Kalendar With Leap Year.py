# Nama File   = Kalendar with Leap Year
# Nama        = Azka A. Maulana
# Tanggal     = 09 September 2024
# Deskripsi   = Buat day counter with Leap Year

# DEFINISI DAN SPESIFIKASI
# hari_kalendar : int [1...31], int[1...12], int[0...9999] -> int [1...366]
#   {hari_kalendar(d,m,y) dari suatu tanggal (d,m,y)}}
# months : int [1...12] -> int [1...36]
#   {months(m) adalah jumlah hari pada tanggal 1 bulan (n)}
# leap_year : int -> int
#   {leap_year(y) buat IDK. I just put it there not knowing what it's for mate. It somehow works so it's fine I guess}

# REALISASI
def leap_year (a): 
    return (a  % 4 == 0) and ((a % 100 != 0) or (a // 400 == 0))

def months (m) :
    if m == 1 :
       return 1
    elif m == 2 :
       return 32
    elif m == 3 :
       return 60
    elif m == 4 :
       return 91
    elif m == 5 :
       return 121
    elif m == 6 :
       return 152
    elif m == 7 :
       return 182
    elif m == 8 :
       return 213
    elif m == 9 :
       return 244
    elif m == 10 :
       return 274
    elif m == 11 :
       return 305
    elif m == 12 :
       return 335

def hari_kalendar (d,m,y) :
   if m > 2 and leap_year (y) : 
        return months (m) + d - 1 + 1
   else :
      return months (m) + d - 1 
   
# APLIKASI
print(hari_kalendar(2,4,2020))