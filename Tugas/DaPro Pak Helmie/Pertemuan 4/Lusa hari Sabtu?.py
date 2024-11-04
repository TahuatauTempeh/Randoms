# Nama file : Lusa hari Sabtu?.py
# Pembuat : Azka Aqylla Maulana
# Tanggal : 26 Agustus 2024
# Deskripsi : Buat predikat yg akan memeriksa apakah lusa adalah hari Sabtu, ketika diberikan masukan tgl, bln dan tahun, apabila diketahui bahwa tanggal 1 Januari di tahun yg bersangkutan adalah hari Kamis. 

# DEFINISI DAN SPESIFIKASI

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

def nama_hari (d) :
   hari_dalam_minggu = ["Senin","Selasa","Rabu","Kamis","Jumat","Sabtu","Minggu"]
   start_day = 3 
   hari_ke = (start_day + (d - 1)) % 7

   return hari_dalam_minggu [hari_ke]

def hari_kalendar (d,m,y) :
   if m > 2 and leap_year (y) : 
        return months (m) + d - 1 + 1
   else :
      return months (m) + d - 1 
   
   return nama_hari (total)

# APLIKASI
print(hari_kalendar(2,4,2020))