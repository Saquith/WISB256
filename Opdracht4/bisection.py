def findRoot(f,a,b,epsilon) :
    m = (a + b) / 2
    
    if abs(b - a) <= epsilon :
        return m
    if (f(a) < 0 and f(m) > 0) or (f(a) > 0 and f(m) < 0) :
        return findRoot(f,a,m,epsilon)
    if (f(m) < 0 and f(b) > 0) or (f(m) > 0 and f(b) < 0) :
        return findRoot(f,m,b,epsilon)

def findAllRoots(f,a,b,epsilon) :
    m = (a + b) / 2

    # Stopping criterion
    if abs(b - a) <= epsilon :
        return [m]

    # Build the lists recursively
    l = []
    if (f(a) < 0 and f(m) > 0) or (f(a) > 0 and f(m) < 0) :
        l.extend(findAllRoots(f,a,m,epsilon))
    if (f(m) < 0 and f(b) > 0) or (f(m) > 0 and f(b) < 0) :
        l.extend(findAllRoots(f,m,b,epsilon))
    return l
