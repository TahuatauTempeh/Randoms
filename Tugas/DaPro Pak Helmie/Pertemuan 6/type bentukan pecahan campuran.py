# Nama File   = Type bentukan pecahan campuran
# Nama        = Azka A. Maulana
# Tanggal     = 12 Octobre 2024
# Deskripsi   = membuat fungsi pecahan campuran dengan type bentukan pecahan

# DEFINISI TYPE
# type pecahan: <bil: integer, n: integer ≥ 0, d: integer > 0>
#   {pecahan terdiri dari tiga komponen, bil = bilangan bulat, n adalah pembilang dengan nilai lebih kecil dari penyebut d yang bernilai lebih dari 0}

# DEFINISI DAN SPESIFIKASI SELEKTOR
# bil: pecahan → integer
#   {bil(P) memberikan komponen bilangan bulat dari pecahan campuran P}

# pemb: pecahan → integer
#   {pemb(P) memberikan pembilang dari pecahan campuran P}

# peny: pecahan → integer
#   {peny(P) memberikan penyebut dari pecahan campuran P}  

# DEFINISI DAN SPESIFIKASI KONSTRUKTOR
# MakePecahan: 3 integer → pecahan
#   {MakePecahan(bil, n, d) membentuk pecahan campuran dengan komponen bil, pembilang n, dan penyebut d}

# DEFINISI DAN SPESIFIKASI OPERATOR
# KonversiPecahan: pecahan → pecahan
#   {KonversiPecahan(P) mengubah pecahan campuran P menjadi pecahan biasa}
# KonversiReal: pecahan → real
#   {KonversiReal(P) mengubah pecahan campuran P menjadi bilangan real}
# AddP: 2 pecahan → pecahan
#   {AddP(P1, P2) menjumlahkan dua buah pecahan campuran}



# REALISASI
def KonversiPecahan(P):
    bilangan = bil(P) * peny(P) + pemb(P)
    if bil(P) < 0:
        return makeP(bilangan * -1, peny(P))
    return makeP(bilangan, peny(P))

def KonversiReal(P):
    return RealP(KonversiPecahan(P))

def pecahan_to_campuran(P):
    pembilang = pemb(P)
    penyebut = peny(P)
    bil = pembilang // penyebut  # Bagian bilangan bulat
    n = pembilang % penyebut  # Sisa dari pembilang
    d = penyebut
    return MakePecahan(bil, n, d)

def AddP(P1, P2):
    pec1 = KonversiPecahan(P1)
    pec2 = KonversiPecahan(P2)
    hasil = AddPecahan(pec1, pec2)
    return pecahan_to_campuran(hasil)

