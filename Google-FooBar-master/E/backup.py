import math
from lkup2 import lkup


def row(arry):
    'Any array upto length 9 can be given, states of which are calculated using lookup table'

    st = bin(len(arry))[2:][::-1]
    ln = len(st)
    ar  = [2**i for i in range(ln) if st[i]=='1'][::-1]

    if ar[0]==8:
        ar=[4,4]+ar[1:]

    su = 0
    nw = []

    for i in range(len(ar)):
        nw.append( ( ar[i],int(''.join( arry[ su:su+ar[i] ] ),2) ) )
        su+=ar[i]

    arry = nw

    res = lkup[arry[0]]
    for k in range(1,len(arry)):

        res2 = set()
        ln = arry[k][0]

        shft_val = 4 + 2*(ln-1) - 2
        msk = 2**shft_val-1
        for i in res:
            for j in lkup[arry[k]]:
                chk = j >> shft_val
                if (i & 3) == chk:
                    res2.add( (i<<shft_val) | (j&msk) )

        res = res2

    return res


def answer(grid):
    '''
    if len(grid[0])>len(grid):
        grid =  list(map(list, zip(*grid)))
    '''

    W,L = len(grid[0]),len(grid)

    uppr_msk = int('10'*W,2)
    lwr_msk  = int('01'*W,2)

    r1 = row(grid[0])

    res = 1

    if L == 1:
        return len(r1)
    
    for i in range(1,L):

        dict_1 = { ( k & lwr_msk ):0 for k in r1 }

        r2 = row(grid[i])
        dict_2 = { ( k&uppr_msk )>>1:0 for k in r1 }

        dict_3 = { k:0 for k in dict_1 if k in dict_2 }

        res += sum(1 for k in r1 if (k&lwr_msk) in dict_3)

        r1 = r2
        
    res += sum(1 for k in r1 if ( k&uppr_msk )>>1 in dict_3)
    return res

    
