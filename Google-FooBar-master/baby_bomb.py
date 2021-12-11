# solution for baby_bomb
def gcd(a, b):
    if a<b:
        a,b = b,a
    while b:
        a, b = b, a%b
    return a

def answer(M, F):

    b = int(F)
    a = int(M)

    k = gcd(a, b)

    if a*b==0 or ( (abs(a - b) % k == 0) and k != 1 ):
        return "impossible"

    return str(func(a, b))

def func(a, b):
    
    if b == 1:
        return a - 1

    elif a == 1:
        return b - 1

    else:
        if a < b:
            return func(b, a)
        else:
            return (a / b) + func(a - a / b * b, b)
