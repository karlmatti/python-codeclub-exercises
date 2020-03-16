def elements_count(*lists):
    c=dict()
    for l in lists:
        for n in l:
            c[n] = c.get(n,0)+1
    d=c.copy()
    for k,v in c.items():
        if v==1:
            d.pop(k)
        else:
            d.pop(k)
            d[k]=v-1
    return d