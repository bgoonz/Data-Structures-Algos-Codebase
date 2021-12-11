#TARGET LEXICOGRAPHICAL ORDER, ARRAY FINDING
def answer(ls,t):
    ls2=ls[:]
    for i in range(1,len(ls)):
        ls2[i]+=ls2[i-1]
    for i in range(len(ls)):
        for j in range(len(ls2)):
            if ls2[j]==t:
                return [i,j]
        for j in range(len(ls2)):
            ls2[j]-=ls[i]
    else:
        return [-1,-1]
