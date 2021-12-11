def prod(seq, a, b):
    r = 1
    for i in range(a, b):
        r *= seq[i]
    return r

def maxprodnon0(seq, a, b):
    firstneg = -1
    negs = 0
    for i in range(a, b):
        if seq[i] >= 0: continue
        negs += 1
        if firstneg < 0:
            firstneg = i
        lastneg = i
    if negs % 2 == 0: return prod(seq, a, b)
    return max(prod(seq, firstneg + 1, b), prod(seq, a, lastneg))

def maxprod(seq):
    best = 0
    N = len(seq)
    i = 0
    while i < N:
        while i < N and seq[i] == 0:
            i += 1
        j = i
        while j < N and seq[j] != 0:
            j += 1
        best = max(best, maxprodnon0(seq, i, j))
        i = j
    return str(best)
