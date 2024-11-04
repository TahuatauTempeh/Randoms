# defense itu type armor dikali persentase HP

# DEFINISI TYPE
# type stats : <HP : integer, DEF : integer, ATK : integer>
#   {HP itu nilai nyawa/darah character. DEF itu nilai defense character. ATK itu nilai damage serangan character}

# DEFINISI SELEKTOR
# HP : stats -> integer
#   {HP(s) memberikan nilai health character}
# DEF : stats -> integer
#   {DEF(s) memberikan nilai defense character}
# ATK : stats -> integer
#   {ATK(s) memberikan nilai attack character}

# DEFINISI KONSTRUKTOR
# makestats : integer, integer, integer -> stats
#   {makestats(x1,x2,x3) untuk mengubah nilai ke stats}

# DEFINISI OPERATOR



# REALISASI
def HP(s) :
    return s

def DEF(s) :
    return s

def ATK(s) :
    return s


def defense(s1,s2) : # s1 = defense default. s2 = health default. s3 = tipe armor
    return DEF(s2) + (HP(s1) * 20/100)

def critchance(s) :
    return ATK(s) * 10/100

def critattack(s1) : # s1 = atk
    return critchance(s1) + ATK(s1)

def findatkdmg(s1) :
    return critattack(s1)

def stats(x1,x2,x3) :
    return f"HP = {HP(x1)}, DEF = {defense(x1,x2)}, ATK = {findatkdmg(x3)}"

def statsdebuff(x1,x2,x3,x4) :
    if x4 == 1 : # 1 = poison so health will decrease
        return f"HP = {HP(x1) - abs(HP(x1) - ((HP(x1) * 10/100) + (HP(x1) * 5/100) + (HP(x1) * 2/100)))}, DEF = {defense(x1,x2)}, ATK = {findatkdmg(x3)}"
    elif x4 == 2 : # 2 = slow so attack will go down
            return f"HP = {HP(x1)}, DEF = {defense(x1,x2)}, ATK = {findatkdmg(x3) - abs(findatkdmg(x3) - ((ATK(x3) * 25/100) -12))}"
    elif x4 == 3 : # 3 = armor break so defense decrease by 50% of default defense (without the hp)
        return f"HP = {HP(x1)}, DEF = {defense(x1,x2) - abs(DEF(x2) - (DEF(x2) * 1/2))}, ATK = {findatkdmg(x3)}"
    elif x4 == 4 : # 4 = petrified so attack -20% and defense = 0
           return f"HP = {HP(x1)}, DEF = 0, ATK = {  abs(findatkdmg(x3) - (ATK(x3) * 20/100))}" 
    else :
        return "No Debuff Applied"

# APLIKASI
print(f"Your new stats are : {stats(200,30,80)}")
print(f"Your new stats are : {statsdebuff(200,30,80,0)}")
print(f"Your new stats are : {statsdebuff(200,30,80,1)}")
print(f"Your new stats are : {statsdebuff(200,30,80,2)}")
print(f"Your new stats are : {statsdebuff(200,30,80,3)}")
print(f"Your new stats are : {statsdebuff(200,30,80,4)}")
