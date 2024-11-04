# Nama File   = Type bentukan pecahan
# Nama        = Azka A. Maulana
# Tanggal     = 8 Octobre 2024
# Deskripsi   = membuat fungsi pecahan dengan type bentukan pecahan

# DEFINISI TYPE
# type pecahan : <n : integer >= 0, d : integer > 0>
#   {n adalah numerator dan d adalah denumerator pada pecahan}

# DEFINISI SELEKTOR
# pem : pecahan -> integer >= 0
#   {pem(P) memebrikan numerator}
# peny : pecahan -> integer > 0
#   {peny(P) memberikan denumerator}

# DEFINISI KONSTRUKTOR  
# makeP : integer >= 0, integer > 0
#   {makeP(a,b) untuk membentuk pecahan. a = numerator; b = denumerator}

# DEFINISI OPERATOR
# AddP : pecahan, pecahan -> pecahan
#   {AddP(P1,P2) untuk menjumlahkan 2 pecahan}
# SubP : pecahan, pecahan -> pecahan
#   {SubP(P1,P2) untuk mengurangakn pecahan dengan pecahan lain}
# MulP : pecahan, pecahan -> pecahan
#   {MulP(P1,P2) untuk mengalikan pecahan dengan pecahan lainnya}
# DivP : pecahan, pecahan -> pecahan
#   {DivP(P1,P2) untuk membagi dua pecahan}
# KonversikeRealP : pecahan ->

# REALISASI
def pemb(P):
    return P[0]

def peny(P):
    return P[1]

def makeP(a,b) :
    return [a,b]

def AddP(P1,P2):
    return makeP((pemb(P1) * peny(P2)) + (pemb(P2) * peny(P1)), (peny(P1) * peny(P2)))

def SubP(P1,P2):
    return makeP((pemb(P1) * peny(P2)) - (pemb(P2) * peny(P1)), (peny(P1) * peny(P2)))
    
def MulP(P1,P2):
    return makeP((pemb(P1) * pemb(P2)), (peny(P1) * peny(P2)))

def DivP(P1,P2):
    return makeP((pemb(P1) * peny(P2)), (peny(P1) * pemb(P2)))

def KonversikeRealP(P):
    return pemb(P) / peny(P)

def isEqP(P1,P2):
    return pemb(P1)/peny(P1) == pemb(P2)/peny(P2)

def isLtP(P1,P2):
    return pemb(P1)/peny(P1) < pemb(P2)/peny(P2)

def IsGtp(P1,P2):
    return pemb(P1)/peny(P1) > pemb(P2)/peny(P2)

# APLIKASI