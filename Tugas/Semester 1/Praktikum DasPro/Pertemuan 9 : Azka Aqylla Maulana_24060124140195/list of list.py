def isAtom(s) :
    return type(s) != list

def isList(s) :
    return type(s) == list

def KonsLo(l,s) :
    return [l] + s

def KonsLi(s,l) :
    return s + [l]

def FirstList(s) :
    return s[0]

def LastList(s) :
    return s[-1]

def TailList(s) :
    return s[1:] 

def HeadList(s) :
    return s[:-1]

def IsEmpty(s) :
    return s == []
    
def IsMember (X,l) :
    if IsEmpty(l) :
        return False
    else :
        if FirstElmt(l) == X :
            return True
        else :
            return IsMember(X,Tail(l))

def IsEqual(s1,s2) :
    if NbElmt(s1) == NbElmt(s2) :
        if IsEmpty(s1) and IsEmpty(s2) :
            return True
        else :
            return FirstElmt(s1) == FirstElmt(s2) and IsEqual(Tail(s1),Tail(s2))
    else :
        False

def IsMemberList(l,s) :
    if IsEmpty(s) :
        return False
    else :
        if isAtom(FirstList(s)) :
            return IsMemberList(l,TailList(s))
        else :
            if IsEqual(FirstList(s)) :
                return True
            else :
                return IsMemberList(l,Tail(s))

# def IsEqS(s1,s2)

# dasdasdasdas

print(isList([1,2,3,4,5,5,5,6]))
print(isAtom([3,2,3]))
print(IsMemberList(2,[2,3,4]))
