#   Nama File   = mencuri uang
#   Nama        = Azka A. Maulana
#   NIM         = 24060124140195
#   Tanggal     = 28 Octobre 2024 (when it's written)
#   Deskripsi   = Hacker rank

user_input = input("")

def Konso(e, l):
    return [e] + l

def IsEmpty(s):
    return s == ""

def FirstChar(s):
    return s[0]

def TailString(s):
    return s[1:]

def StringToList(s):
    if IsEmpty(s):
        return []
    else:
        return Konso(FirstChar(s), StringToList(TailString(s)))
    
def inputing(s):
    return StringToList(user_input)

def digit(S) :
    return '0' <= S <= '9'

def hasil(S) :
    if IsEmpty(S) :
        return 0 
    else :
        if FirstChar(StringToList(S)) == digit(S) :
            return 1 + hasil((TailString(S)))
        else :
            return hasil(TailString(S))


print(hasil(f"{user_input}"))


# print(StringToList("sd213"))