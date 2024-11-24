from lol import *

#   makepn : elmt, pohon -> pohon
#       {makepn(pn) buat bikin pohon}
def makepn(a,pn) :
    return [a,pn]

# 
def akar(pn) :
    return pn[0]

def anak(pn) :
    return pn[1]

def istreeempty(pn) :
    return pn == []

def isoneelmt(pn) :
    return (istreeempty(pn) == False) and (istreeempty(anak(pn)) == True)

def nbnelmt(pn) :
    if istreeempty(pn) :
        return 0
    elif isoneelmt(pn) :
        return 1
    else :
        return 1 + nbnelmt(anak(pn)[0]) + nbelmtchild(anak(pn)[1:])
    
def nbelmtchild(pn) :
    if istreeempty(pn) :
        return 0
    else :
        return nbnelmt(pn[0]) + nbelmtchild(pn[1:])
    
def nbdaun(pn) :
    if istreeempty(pn) :
        return 0
    if isoneelmt(pn) and istreeempty(anak(pn)) :
        return 1
    else :
        return nbdaunchild(anak(pn))

def nbdaunchild(pn) :
    if istreeempty(pn) :
        return 0
    else :
        return nbdaun(pn[0]) + nbdaunchild(pn[1:])

Wee = makepn(2,[])
Woo = makepn('A', [makepn( 'B', [makepn( 'D', []),makepn('E', []), makepn( 'F', [])]) , makepn( 'C', [makepn( 'G', []) ,makepn('H', [makepn('I', [1])])]) ])


print(Wee) # [2,[]]
print('-' * 120)
print(istreeempty(Wee)) # False
print('-' * 120)
print(isoneelmt(Wee)) # True
print('-' * 120)
print(Woo) 
print('-' * 120)
print(nbnelmt(Woo))
print('-' * 120)
print(nbdaun(Woo))
