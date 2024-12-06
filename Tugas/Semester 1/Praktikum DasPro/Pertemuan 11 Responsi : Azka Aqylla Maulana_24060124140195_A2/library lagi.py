#   Nama File   = we going to perpus with dis
#   Nama        = Azka A. Maulana
#   NIM         = 24060124140195
#   Tanggal     = 4 Decembre 2024 (when it's written)
#   Deskripsi   = perpus perpus :0

def MakeList(a):
    return [a]

def Konso(e, L):
    return [e] + L

def Konsi(L, e):
    return L + [e]

def concatList(L1, L2):
    return L1 + L2

def FirstElmt(L):
    return L[0]

def LastElmt(L):
    return L[-1]

def Head(L):
    return L[:-1]

def Tail(L):
    return L[1:]

def IsEmpty(L):
    return L == []

def FirstList(LoL):
    return LoL[0]

def LastList(LoL):
    return LoL[-1]

def HeadList(LoL):
    return LoL[:-1]

def TailList(LoL):
    return LoL[1:]

def IsEmpty(LoL):
    if LoL == []:
        return True
    else:
        return False

def IsAtom(LoL):
    if type(LoL) == list:
             return False
    else:
        return True

def IsList(LoL):
    if IsAtom(LoL) == False:
        return True
    else:
        return False

def getTag(shelf):
    return FirstElmt(FirstList(shelf))

def getBooks(shelf):
    return LastElmt(FirstList(shelf))

def makeShelf(tag, book):
    return [[tag] + [book]]

def AddToShelf(tag, book):
    return [tag] + [book]
        
def AddBooks(shelves, tag, book):
    if IsEmpty(shelves):  
        return [makeShelf(tag, book)[0]]
    else:
        first_shelf = FirstList(shelves)  
        if getTag(first_shelf) == tag: 
            updated_books = concatList(getBooks(first_shelf), book)
            updated_shelf = makeShelf(tag, updated_books)[0]
            return Konso(updated_shelf, TailList(shelves)) 
        else:
            return Konso(first_shelf, AddBooks(TailList(shelves), tag, book))