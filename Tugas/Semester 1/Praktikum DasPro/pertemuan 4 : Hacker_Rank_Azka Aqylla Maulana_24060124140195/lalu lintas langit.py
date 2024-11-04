# Nama File   = lalu lintas langit
# Nama        = Azka A. Maulana
# NIM         = 24060124140195
# Tanggal     = 22 September 2024 (tanggal mulai menulis di VsCode)
# Deskripsi   = lalu lintas langit

# DEFINISI DAN SPESIFIKASI
# monitor_pesawat : 3 int -> string
# [monitor_pesawat (x,y,z) adalah funsgi untuk menganalisis data dan mengeluarkan status operasional pesawat berdasarkan kondisi berikut: "Kecepatan Berbahaya": Jika kecepatan melebihi 900 km/h atau di bawah 200 km/h. "Terlalu Tinggi": Jika ketinggian pesawat melebihi 12.000 meter. "Bahan Bakar Rendah": Jika status bahan bakar kurang dari 20%. "Aman untuk Mendarat": Jika ketinggian kurang dari 5.000 meter, kecepatan antara 200 hingga 900 km/h, dan bahan bakar lebih dari 50%. "Berjalan Normal": Jika tidak ada kondisi di atas yang terpenuhi]

# REALISASI
def monitor_pesawat(x,y,z) :
    if y > 900 or y < 200 :
        return ('Kecepatan Berbahaya')
    elif x > 12000 :
        return ('Terlalu Tinggi')
    elif z < 20 :
        return ('Bahan Bakar Rendah')
    elif x < 5000 and 200 < y < 900 and z > 50 :
        return ('Aman untuk Mendarat')
    else :
        return ('Berjalan Normal')
print(eval(input()))

# APLIKASI
monitor_pesawat(4000,850,55)
monitor_pesawat(5000,950,70)