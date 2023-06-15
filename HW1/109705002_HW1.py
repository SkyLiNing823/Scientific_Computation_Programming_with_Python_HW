def rightpad(s, n, c='0'):
    if(n % len(c) == 0):
        s += ((n-len(s))//len(c))*c
    else:
        s += ((n-len(s))//len(c))*c + c[:(n-len(s)) % len(c)]
    return s


def leftpad(s, n, c='0'):
    if(n % len(c) == 0):
        s = ((n-len(s))//len(c))*c + s
    else:
        s = (c[n % len(c)-1:]+c*((n-len(s))//len(c))) + s
    return s
