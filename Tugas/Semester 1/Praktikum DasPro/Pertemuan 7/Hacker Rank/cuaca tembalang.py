#   Nama File   = cuaca tembalang
#   Nama        = Azka A. Maulana
#   NIM         = 24060124140195
#   Tanggal     = 28 Octobre 2024 (when it's written)
#   Deskripsi   = Hacker rank

def FirstElmt(l) :
    return l[0]

def Tail(l) :
    return l[1:]

def IsEmpty(l) :
    return l == []

def HitungHariPanas(S) :
    if IsEmpty(S) :
        return 0 
    else :
        if FirstElmt(S) > 30 :
            return abs(1 + HitungHariPanas(Tail(S)))
        else :
            return abs(HitungHariPanas(Tail(S)))
        
print(HitungHariPanas([20, 30, 34, 35, 28]))