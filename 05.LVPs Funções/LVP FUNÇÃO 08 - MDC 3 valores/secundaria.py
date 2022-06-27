def f_mult(a,b,c):
    mult=0
    d=2
    while d<a:
        if (a%d==0 and b%d==0 and c%d==0):
            mult=d
        d=d+1
    return mult