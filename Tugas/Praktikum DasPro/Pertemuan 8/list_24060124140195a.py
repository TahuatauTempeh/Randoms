#   Nama File   = List
#   Nama        = Azka A. Maulana
#   NIM         = 24060124140195
#   Tanggal     = 28 Octobre 2024 (when it's written)
#   Deskripsi   = list

#   DEFINISI TYPE
#   type list : [ ] or [e , list]
#       {elemen di bagian awal dan list di bagian akhir}
#   type list : [ ] or [list , e]
#       {elemen di akhir dan list di awal}

#   DEFINISI DAN SPESIFIKASI SELEKTOR
#   FirstElmt : list tidak kosong --> elemen
#       {FirstElmt(l) menghasilkan elemen pertama l}
#   LastElmt : list tidak kosong --> elemen
#       {LastElmt(l) mengembalikan nilai terakhir l}
#   Tail : list tidak kosong --> list
#       {Tail(l) mengasilkan list tanpa elemen pertama} 
#   Head : list tidak kosong --> list
#       {Head(l) menghasilan list tanpa elemen terakhir}

#   DEFINISI DAN SPESIFIKASI KONSTRUKTOR
#   Konso : elemen , list --> list
#       {Konso(e,l) membuat list dari elemen pertama (e) dan list. Elemen ditempatkan di depan list}
#   Konsi : list , elemen --> list
#       {konsi(l,e) membuat list dari elemen terakhir (e) dan list. Elemen ditempatkan di akhir list}

#   DEFINISI DAN SPESIFIKASI OPERATOR
#   IsEmpty : list --> boolean
#       {IsEmpty(l) mengembalikan True jika list l kosong, False jika tidak}
#   IsOneElmt : list --> boolean
#       {IsOneElmt(l) mengembalikan True jika list l hanya memiliki satu elemen, False jika tidak}
#   NbElmt : list --> integer
#       {NbElmt(l) menghitung jumlah elemen dalam list l}
#   ElmtKeN : integer, list --> elemen
#       {ElmtKeN(N, l) menghasilkan elemen ke-N dari list l}
#   IsMember : elemen, list --> boolean
#       {IsMember(X, l) mengembalikan True jika X adalah elemen dari list l, False jika tidak}
#   Copy : list --> list
#       {Copy(l) menghasilkan salinan dari list l}
#   Inverse : list --> list
#       {Inverse(l) menghasilkan list yang merupakan kebalikan dari list l}
#   Konkat : list, list --> list
#       {Konkat(l1, l2) menghasilkan list yang merupakan gabungan dari l1 dan l2}
#   SumElmt : list --> integer
#       {SumElmt(l) menghasilkan jumlah dari seluruh elemen dalam list l}
#   AvgElmt : list --> real
#       {AvgElmt(l) menghitung rata-rata dari elemen-elemen dalam list l}
#   MaxElmt : list --> elemen
#       {MaxElmt(l) menghasilkan elemen terbesar dalam list l}
#   MaxNB : list --> (elemen, integer)
#       {MaxNB(l) menghasilkan sebuah tuple (elemen, integer) yang berisi elemen terbesar dalam list l dan jumlah kemunculannya}
#   CountX : list, elemen --> integer
#       {CountX(l, x) menghitung berapa kali elemen x muncul dalam list l}
#   AddList : list, list --> list
#       {AddList(l1, l2) menghasilkan list baru dengan setiap elemen hasil penjumlahan elemen-elemen di posisi yang sama dalam l1 dan l2}
#   IsPalindrom : list --> boolean
#       {IsPalindrom(l) mengembalikan True jika list l adalah palindrom (membaca sama dari depan maupun belakang), False jika tidak}

#   REALISASI
def Konso(e,l) :
    return [e] + l

def Konsi(l,e) :
    return l + [e]

def FirstElmt(l) :
    return l[0]

def LastElmt(l) :
    return l[-1]

def Tail(l) :
    return l[1:]

def Head(l) :
    return l[:-1]

def IsEmpty(l) :
    return l == []

def IsOneElmt(l) :
    if IsEmpty(l) :
        return False
    else :
        return Tail(l) == [] and Head(l) == []
    
def NbElmt(l) :
    if IsEmpty(l) :
        return 0
    else :
        return 1 + NbElmt(Tail(l))
    
def ElmtKeN(N,l) :
    if N == 1 :
        return FirstElmt(l)
    else :
        return ElmtKeN(N - 1, Tail(l))
    
def IsMember (X,l) :
    if IsEmpty(l) :
        return False
    else :
        if FirstElmt(l) == X :
            return True
        else :
            return IsMember(X,Tail(l))
        
def Copy(l) :
    if IsEmpty(l) :
        return []
    else :
        return Konsi(Copy(Head(l)),LastElmt(l))
    
def Inverse(l) :
    if IsEmpty(l) :
        return []
    else :
        return Konsi(Inverse(Tail(l)),FirstElmt(l))
    
def Konkat(l1,l2) :
    if IsEmpty(l1) :
        return l2
    else :
        return Konso(FirstElmt(l1),Konkat(Tail(l1),l2))
    
def SumElmt(l) :
    if IsEmpty(l) :
        return 0
    else :
        return FirstElmt(l) + SumElmt(Tail(l))
    
def AvgElmt(l) :
    if IsEmpty(l) :
        return 0 
    else :
        return (SumElmt(l)) / NbElmt(l)
    
def max2(a,b) :
    if 'a' > 'b' :
        return a
    else : 
        return b
    
def MaxElmt(l) :
    if IsOneElmt(l) :
        return l
    else :
        return max2(LastElmt(l),MaxElmt(Head(l)))
    
def MaxNB(l) :
    if IsEmpty(l) :
        return (None, 0)  
    else : 
        return (MaxElmt(l), CountX(l, MaxElmt(l)) )

def CountX(l, x) :
    if IsEmpty(l) :
        return 0
    elif FirstElmt(l) == x:
        return 1 + CountX(Tail(l), x)
    else:
        return CountX(Tail(l), x)

def AddList(l1,l2) :
    if IsEmpty(l1) and IsEmpty(l2) :
        return []
    elif IsEmpty(l1) and not IsEmpty(l2) :
        return l2
    elif not IsEmpty(l1) and IsEmpty(l2) :
        return l1
    else :
        return Konso(FirstElmt(l1) + FirstElmt(l2), AddList(Tail(l1),Tail(l2)))
    
def IsPalindrom(L):
    if IsEmpty(L) or IsOneElmt(L): 
        return True
    else:
        return FirstElmt(L) == LastElmt(L) and IsPalindrom(Tail(Head(L)))
    
#   APLIKASI    
# print(f"Is one Element : {IsOneElmt([2])}")
# print(f"Banyank elemen : {NbElmt([4,5,1,2])}")
# print(f"Elemen ke : {ElmtKeN(4,[3,4,5,6,7,8])}")
# print(f"Anggota dari list : {IsMember(10,[3,5,6,1,2,8])}")
# print(f"Anggota dari list : {IsMember(2,[1,2,3,4,5,])}")
# print(f"Inverse nya adalah : {Inverse([2,3,4,5])}")
# print(f"Hasil copy : {Copy([4,5,1,2])}")
# print(f"Konkat nya : {Konkat([2,4,6,7],[1,2,3,4])}")
# print(f"Hasil tambah dari anggota list : {SumElmt([2,3,1])}")
# print(f"Rata rata : {AvgElmt([2,3,4])}")
# print(f"Nilai tertinggi : {MaxElmt([3,2,1])}")
# print(f"Hasil : {MaxNB([3, 5, 5, 2, 5, 1])}")  
# print(f"Hasil tambah dua list : {AddList([2,3,6],[1,2])}")
# print(f"Apakah berikut termasuk palindrom : {IsPalindrom(['R', 'U', 'S', 'A', 'K'])}")
# print(f"Apakah berikut termasuk palindrom : {IsPalindrom(['K', 'A', 'S', 'U', 'R', ' ', 'R', 'U', 'S', 'A', 'K'])}")
# print(f"Apakah berikut termasuk palindrom : {IsPalindrom(['N', 'A', 'B', 'A', 'B', 'A', 'N'])}")    