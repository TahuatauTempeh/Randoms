# DEFINISI DAN SPESIFIKASI
# Daysfrom1900 : int[1...31], int[1...12], int > 1900 -> int >=0
#   {Daysfrom1900(d,m,y) adalah fungsi untuk membentuk sebuah tanggal seperti soal nomor 1,
#   kemudian mengembalikan hari absolut yang dihitung mulai tanggal 1 Januari 1900 dengan memperhitungkan tahun kabisat.}


# REALISASI
def dpm (b) :
    if b == 1 :
       return 1
    elif b == 2 :
       return 32
    elif b == 3 :
       return 60
    elif b == 4 :
       return 91
    elif b == 5 :
       return 121
    elif b == 6 :
       return 152
    elif b == 7 :
       return 182
    elif b == 8 :
       return 213
    elif b == 9 :
       return 244
    elif b == 10 :
       return 274
    elif b == 11 :
       return 305
    elif b == 12 :
       return 335
    
def iskabisat(year) :
   if (year % 4 == 0 and year % 100 == 0) or (year % 400 == 0)
      return 1
   else :
      return 0

def addyear (current_year,) :
   return ((current_year - 1900) + ())

def haridari1900(d,m,y) :
   return 

# APLIKASI

