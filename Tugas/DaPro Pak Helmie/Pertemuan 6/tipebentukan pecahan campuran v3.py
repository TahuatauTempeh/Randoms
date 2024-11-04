# Nama File   = Type bentukan pecahan campuran
# Nama        = Azka A. Maulana
# Tanggal     = 18 Octobre 2024 (when it's written)
# Deskripsi   = membuat fungsi pecahan campuran dengan type bentukan pecahan

# DEFINISI TYPE
#  type pecahanc: <bil: integer, n: integer >= 0, d: integer > 0>
#   {membuat pecahan campuran dari bilangan bulat (bil), pembilang (n), dan penyebut (d)}

# DEFINISI DAN SPESIFIKASI SELEKTOR
# GetBil: pecahanc → integer
#   {GetBil(P) mengembalikan bagian bil dari pecahan campuran.}
# GetN: pecahanc → integer
#   {GetN(P) mengembalikan bagian pembilang (n) dari pecahan campuran.}
# GetD: pecahanc → integer
#   {GetD(P) mengembalikan bagian penyebut (d) dari pecahan campuran.}

# DEFINISI DAN SPESIFIKASI KONSTRUKTOR
# MakePecahanC: 3 integer → pecahanc
#   {MakePecahanC(bil, n, d) membentuk pecahan campuran dari bilangan bulat, pembilang, dan penyebut.}

# DEFINISI DAN SPESIFIKASI OPERATOR
# Abs: integer → integer
#   {Abs(x) mengembalikan nilai absolut dari bilangan integer.}
# KonversiPecahan: pecahanc → integer
#   {KonversiPecahan(P) mengubah pecahan campuran menjadi pecahan biasa.}
# KonversiReal: pecahanc → real
#   {KonversiReal(P) mengubah pecahan campuran menjadi bilangan real.}
# ToMixedFraction: 2 integer → pecahanc
#   {ToMixedFraction(pembilang, penyebut) mengubah pecahan biasa menjadi pecahan campuran.}
# AddP: pecahanc, pecahanc → pecahanc
#   {AddP(P1,P2) menjumlahkan dua pecahan campuran dan mengembalikan hasilnya dalam bentuk pecahan campuran.}
# SubP: pecahanc, pecahanc → pecahanc
#   {SubP(P1,P2) mengurangkan pecahan campuran P1 dengan P2 dan mengembalikan hasilnya dalam bentuk pecahan campuran.}
# MulP: pecahanc, pecahanc → pecahanc
#   {MulP(P1,P2) mengalikan dua pecahan campuran dan mengembalikan hasilnya dalam bentuk pecahan campuran.}
# DivP: pecahanc, pecahanc → pecahanc
#   {DivP(P1,P2) membagi pecahan campuran P1 dengan P2 dan mengembalikan hasilnya dalam bentuk pecahan campuran.}
# IsEqP: pecahanc, pecahanc → boolean
#   {IsEqP(P1,P2) membandingkan apakah dua pecahan campuran P1 dan P2 bernilai sama.}
# IsLtP: pecahanc, pecahanc → boolean
#   {IsLtP(P1,P2) membandingkan apakah pecahan campuran P1 lebih kecil dari pecahan campuran P2.}
# IsGtP: pecahanc, pecahanc → boolean
#   {IsGtP(P1,P2) membandingkan apakah pecahan campuran P1 lebih besar dari pecahan campuran P2.}


# REALISASI
def MakePecahanC(bil, n, d):
    return [bil, n, d]  

def GetBil(P):
    return P[0]  

def GetN(P):
    return P[1]  

def GetD(P):
    return P[2]  

def Abs(x):
    if x < 0:
        return -x
    else:
        return x

def KonversiPecahan(P):
    if GetBil(P) < 0:
        return GetBil(P) * GetD(P) - GetN(P)  
    else:
        return GetBil(P) * GetD(P) + GetN(P)  

def KonversiReal(P):
    return KonversiPecahan(P) / GetD(P)

def ToMixedFraction(pembilang, penyebut):
    bil = pembilang // penyebut # // maksudnya pembagian bulat. misal 20 // 3 = 18 so div
    n = Abs(pembilang) % penyebut # % = mod
    return MakePecahanC(bil, n, penyebut)

def AddP(P1, P2):
    pembilang = KonversiPecahan(P1) * GetD(P2) + KonversiPecahan(P2) * GetD(P1)
    penyebut = GetD(P1) * GetD(P2)
    return ToMixedFraction(pembilang, penyebut)

def SubP(P1, P2):
    pembilang = KonversiPecahan(P1) * GetD(P2) - KonversiPecahan(P2) * GetD(P1)
    penyebut = GetD(P1) * GetD(P2)
    return ToMixedFraction(pembilang, penyebut)

def MulP(P1, P2):
    pembilang = KonversiPecahan(P1) * KonversiPecahan(P2)
    penyebut = GetD(P1) * GetD(P2)
    return ToMixedFraction(pembilang, penyebut)

def DivP(P1, P2):
    pembilang = KonversiPecahan(P1) * GetD(P2)
    penyebut = KonversiPecahan(P2) * GetD(P1)
    return ToMixedFraction(pembilang, penyebut)

def IsEqP(P1, P2):
    return KonversiPecahan(P1) * GetD(P2) == KonversiPecahan(P2) * GetD(P1)

def IsLtP(P1, P2):
    return KonversiPecahan(P1) * GetD(P2) < KonversiPecahan(P2) * GetD(P1)

def IsGtP(P1, P2):
    return KonversiPecahan(P1) * GetD(P2) > KonversiPecahan(P2) * GetD(P1)

# APLIKASI
print(KonversiPecahan(MakePecahanC(3, 1, 2)))   # 7
print(KonversiReal(MakePecahanC(3, 1, 2)))  # 3.5
print(AddP(MakePecahanC(3, 1, 2), MakePecahanC(2, 1, 2)))   # [6, 0, 4]
print(SubP(MakePecahanC(3, 1, 2), MakePecahanC(1, 1, 2)))   # [2, 0, 4]
print(MulP(MakePecahanC(3, 1, 2), MakePecahanC(2, 1, 2)))   # [8, 3, 4]
print(DivP(MakePecahanC(3, 1, 2), MakePecahanC(1, 1, 2)))   # [2, 2, 6]
print(IsEqP(MakePecahanC(3, 1, 2), MakePecahanC(7, 0, 2)))  # False
print(IsLtP(MakePecahanC(3, 1, 2), MakePecahanC(4, 0, 2)))  # True
print(IsGtP(MakePecahanC(4, 0, 2), MakePecahanC(3, 1, 2)))  # True
