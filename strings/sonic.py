def sonic_how_many_rings_did_you_get(input_string):
    s=0
    for c in input_string:
        if c in 'abdegopqDOPQR069':
            s+=1
        elif c in 'B8':
            s+=2
    return s