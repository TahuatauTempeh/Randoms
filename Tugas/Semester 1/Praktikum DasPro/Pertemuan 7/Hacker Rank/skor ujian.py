#   Nama File   = skor ujian
#   Nama        = Azka A. Maulana
#   NIM         = 24060124140195
#   Tanggal     = 28 Octobre 2024 (when it's written)
#   Deskripsi   = Hacker rank

#   DEFINISI TYPE
#   type list : [ ] or [e , list]
#       {elemen di bagian awal dan list di bagian akhir}
#   type list : [ ] or [list , e]
#       {elemen di akhir dan list di awal}

#   DEFINISI DAN SPESIFIKASI SELEkTOR

#   REALISASI
def Konso(e, l):
    return [e] + l

def Konsi(l, e):
    return l + [e]

def FirstElmt(l):
    return l[0]

def Tail(l):
    return l[1:]

def IsEmpty(l):
    return l == []

def NbElmt(l):
    if IsEmpty(l):
        return 0
    else:
        return 1 + NbElmt(Tail(l))

def ElmtKeN(N, l):
    if N == 1:
        return FirstElmt(l)
    else:
        return ElmtKeN(N - 1, Tail(l))

def Range(start, end):
    if start == end:
        return []
    else:
        return Konso(start, Range(start + 1, end))

def IsIncreasingTriple(a, b, c):
    return a < b and b < c

def JumlahPolaNaik(T):
    if NbElmt(T) < 3:
        return 0
    else:
        count = 0
        for i in Range(1, NbElmt(T) - 1):
            if IsIncreasingTriple(ElmtKeN(i, T), ElmtKeN(i + 1, T), ElmtKeN(i + 2, T)):
                count += 1
        return count

#   APLIKASI
print(f"Jumlah pola berturut-turut yang membentuk urutan naik: {JumlahPolaNaik([40, 41, 42, 43, 39, 45, 46, 47, 44])}")

