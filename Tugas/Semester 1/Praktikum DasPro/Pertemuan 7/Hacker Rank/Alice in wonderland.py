#   Nama File   = Alice in wonderland
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
    
def Alice(W) :
    if IsEmpty(W) :
        return 0
    else:
        if FirstElmt(W) < 0 :
            return abs(1 + Alice(Tail(W)))
        else :
            return abs(Alice(Tail(W)))

print(Alice([1, 2 , 0, -1, -2]))