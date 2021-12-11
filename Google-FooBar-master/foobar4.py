#MAXIMUM PRODUCT SUBARRAY(NON_CONTIGOUS & NON_EMPTY)
def answer(ls):
    pc,nc,zc=0,0,0
    for i in ls:
        if i>0:
            pc+=1
        elif i<0:
            nc+=1
        else:
            zc+=1

    if (pc==0 and nc==0):
        return '0'
    if (pc==0 and nc==1):
        if zc==0:
            return str(sum(ls))
        else:
            return '0'

    res=1

    if nc==0:
        for i in ls:
            if i!=0:
                res*=i
        res=str((res))
        return res if res[-1]!='L' else res[:-1]

    if not (nc^1)&1:#nc is ODD
        for i in ls:
            if i!=0:
                res*=i
        ls2=[i for i in ls if i<0]
        div=max(ls2)
        res=res/div
        res=str((res))
        return res if res[-1]!='L' else res[:-1]

    else:
        for i in ls:
            if i!=0:
                res*=i
        res=str((res))
        return res if res[-1]!='L' else res[:-1]
