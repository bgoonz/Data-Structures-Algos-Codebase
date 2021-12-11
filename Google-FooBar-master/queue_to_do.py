#XOR OF UPPER DIAGONAL ELEMENTS
def answer(strt, ln):
    wrkr_lst = [(strt + (ln - l) * ln,
                    strt + (ln - l) * ln + l)
                   for l in range(ln, 0, -1)]

    rdcd_xor = [xorng(strt, lst) for strt, lst in wrkr_lst]

    return reduce(lambda x, y: x ^ y, rdcd_xor)

def xorng(strt, lst):
    # inclusive strt and exclusive lst
    if (lst - strt) == 0:
        return 0
    if (lst - strt) == 1:
        return strt
    if (lst - strt) <= 4:
        return reduce(lambda x, y: x ^ y, range(strt, lst))
    else:
        bgn_rng = (strt, strt / 4 * 4 + 4)
        lst_rng = (lst / 4 * 4, lst)
        return xorng(*bgn_rng) ^ xorng(*lst_rng)
