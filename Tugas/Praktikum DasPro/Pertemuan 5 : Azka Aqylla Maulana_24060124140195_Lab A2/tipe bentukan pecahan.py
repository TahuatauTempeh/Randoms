# Nama File   = tipe bentukan pecahan
# Nama        = Azka A. Maulana
# NIM         = 24060124140195
# Tanggal     = 28 September 2024 (tanggal mulai menulis di VsCode)
# Deskripsi   = menjawab soal tipe bentukan pecahan

# Definisi type
# type pecahan: <n:integer, d:integer>
#   {<n,d> adalah sebuah point dengan n adalah pembilang dan d adalah penyebut, penyebut bpecahan tidak boleh nol}

# Definisi Dan Spesifikasi Konstruktor
# MakeP: 2real --> pecahan
#   {makeP (n,d) membentuk point dari n dan d dengan n sebagai pembilang dan d sebagai penyebut}
# Realisasi
def makeP (n,d):
    return[n,d]

# Definisi Dan Spesifikasi Selector
# pemb: pecahan --> integer
#   {pemb(n) memberikan pembilang n dari pecahan tersebut}
# 
# peny: pecahan --> integer
#   {peny(d) memberikan penyebut d dari pecahan tersebut}

# Realisasi
def pemb(P):
    return P[0]

def peny(P):
    return P[1]

# Definisi dan Spesifikasi operator terhadap pecahan
# AddP: 2 pecahan --> pecahan
#   {AddP(P1,P2) menmbahkan 2 buah pecahan yaitu P1 dan P2}
# 
# SubP: 2 pecahan --> pecahan
#   {SubP(P1,P2) mengurangkan 2 buah pecahan yaitu P1 dan P2}
# 
# MulP: 2 pecahan --> pecahan
#   {MulP(P1,P2) mengalikan 2 buah pecahan yaitu P1 dan P2}
# 
# DivP: 2 pecahan --> pecahan
#   {DivP(P1,P2) membagikan 2 buah pecahan yaitu P1 dan P2}
# 
# RealP: pecahan --> real
#   {RealP(P1) menuliskan bilangan pecahan dalam notasi desimal}

# Realisasi 
def AddP(P1,P2):
    return makeP((pemb(P1) * peny(P2)) + (pemb(P2) * peny(P1)), (peny(P1) * peny(P2)))

def SubP(P1,P2):
    return makeP((pemb(P1) * peny(P2)) - (pemb(P2) * peny(P1)), (peny(P1) * peny(P2)))
    
def MulP(P1,P2):
    return makeP((pemb(P1) * pemb(P2)), (peny(P1) * peny(P2)))

def DivP(P1,P2):
    return makeP((pemb(P1) * peny(P2)), (peny(P1) * pemb(P2)))

def RealP(P):
    return pemb(P) / peny(P)

# Definisi dan Spesifikasi predikat
# isEqP: 2 pecahan --> boolean
#   {isEqP(P1,P2) membandingkan apakah ke-2 buah pecahan itu sama}
# 
# isLtP: 2 pecahan --> boolean
#   {isLtP(P1,P2) membandingkan 2 buah pecahan apakah P1 lebih kecil dari P2}
# 
# IsGtp: 2 pecahan --> boolean
#   {IsGtp(P1,P2) membandingkan 2 buah pecahan apakah P1 lebih besar dari P2}

# Realisasi
def isEqP(P1,P2):
    return pemb(P1)/peny(P1) == pemb(P2)/peny(P2)

def isLtP(P1,P2):
    return pemb(P1)/peny(P1) < pemb(P2)/peny(P2)

def IsGtp(P1,P2):
    return pemb(P1)/peny(P1) > pemb(P2)/peny(P2)


# Aplikasi
print(AddP(makeP(4,5), makeP(1,2)))
print(SubP(makeP(4,5), makeP(1,2)))
print(MulP(makeP(4,5), makeP(1,2)))
print(DivP(makeP(4,5), makeP(1,2)))
print(RealP(makeP(4,5)))

print(isLtP(makeP(1,3), makeP(1,2)))
print(isEqP(makeP(2,4), makeP(1,2)))
print(IsGtp(makeP(2,4), makeP(1,2)))