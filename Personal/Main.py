a = 5
b = 2
c = 6

def fungsi1(x):
    x = 2+c*3
    print(x)

# fungsi1(3)

# def fungsi2(y):
#     y = (2*a^2)+8*b-2
#     print(y)

# fungsi2(9)

def ayam(x,y):
    if x == True:
        z = y + 6
    else:
        z = y + 3
    return z

print(ayam(True,4))
print(ayam(False,4))