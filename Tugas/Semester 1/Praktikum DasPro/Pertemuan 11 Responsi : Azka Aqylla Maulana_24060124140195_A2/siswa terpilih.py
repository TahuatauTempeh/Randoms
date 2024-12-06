#   Nama File   = siswa terpilih
#   Nama        = Azka A. Maulana
#   NIM         = 24060124140195
#   Tanggal     = 4 Decembre 2024 (when it's written)
#   Deskripsi   = siswa terpilih :0


#   DEFINISI DAN SPESIFIKASI


#   REALISASI
def KonsLo(l, s):
    return [l] + s

def KonsLi(s, l):
    return s + [l]

def FirstList(s):
    return s[0]

def TailList(s):
    return s[1:]

def HeadList(s):
    return s[:-1]

def LastList(s):
    return s[-1]

def IsEmpty(s):
    return s == []

def isAtom(s):
    return type(s) != list

def isList(s):
    return type(s) == list

def IsEqual(s1, s2):
    if len(s1) == len(s2):
        if IsEmpty(s1) and IsEmpty(s2):
            return True
        else:
            return FirstList(s1) == FirstList(s2) and IsEqual(TailList(s1), TailList(s2))
    else:
        return False

def IsMemberLS(l, s):
    if IsEmpty(s):
        return False
    else:
        if isAtom(FirstList(s)):
            return IsMemberLS(l, TailList(s))
        else:
            if IsEqual(FirstList(s), l):
                return True
            else:
                return IsMemberLS(l, TailList(s))

def IsMemberS(x, S):
    if IsEmpty(S):
        return False
    else:
        if isAtom(FirstList(S)):
            return FirstList(S) == x or IsMemberS(x, TailList(S))
        else:
            return IsMemberS(x, FirstList(S)) or IsMemberS(x, TailList(S))

def nilai(siswa, LoL):
    if IsEmpty(LoL):
        return "Siswa itu tidak ada di kelas ini"
    else:
        if FirstList(FirstList(LoL)) == siswa:
            return LastList(FirstList(LoL))
        else:
            return nilai(siswa, TailList(LoL))

#   APLIKASI
import ast

LoL = ast.literal_eval(input("Masukkan daftar siswa: "))
siswa = input("Masukkan nama siswa: ")
print(nilai(siswa, LoL))

#   input [["Andi", 25], ["Budi", 70], ["Citra", 85]]