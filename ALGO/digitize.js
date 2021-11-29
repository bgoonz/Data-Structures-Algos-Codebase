function digitize(n) {
    r = n.toString().split('');
    r.forEach((el, i, a) => { a[i] = parseInt(el); })
    return r
}
digitize(123)
