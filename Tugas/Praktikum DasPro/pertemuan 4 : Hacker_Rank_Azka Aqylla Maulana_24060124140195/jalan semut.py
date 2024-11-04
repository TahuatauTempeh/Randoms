# Nama File   = jalan semut
# Nama        = Azka A. Maulana
# NIM         = 24060124140195
# Tanggal     = 22 September 2024 (tanggal mulai menulis di VsCode)
# Deskripsi   = jalan semut :0

# DEFINISI DAN SPESIFIKASI
# bidang : 3 int -> real
#   [bidang (x,y,z) adalah fungsi untuk mencari jarak terpendek yg dapat ditempuh oleh semut pada bidang (x,y,z)]
# jalanSemut : 3 int -> real
#   [jalanSemut (x,y,z) adalah fungsi untuk mencari jalan terpendek dan mebulatkannya to the last 3 decimal points (Aku nggak tahu cara translate kata kata terakhir ke bahasa Indonesia)]

# REALISASI
def bidang(x,y,z):
   if x>y and x>z:
     return ((y+z)**2+x**2)**0.5
   elif y>x and y>z:
     return ((x+z)**2+y**2)**0.5
   elif z>x and z>y:
     return ((x+y)**2+z**2)**0.5

def jalanSemut(x,y,z):
   return round(bidang(x,y,z), 3)

print(eval(input()))

# APLIKASI
jalanSemut(3,4,5)
jalanSemut(1,2,7)