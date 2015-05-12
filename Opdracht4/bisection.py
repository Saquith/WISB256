def findRoot(f,a,b,epsilon) :
    m = (a + b) / 2
    
    # Stopping criterion
    if abs(b - a) <= epsilon :
        return m

    # Check if this is already a root
    if f(a) == 0 :
        return a
    if f(b) == 0 :
        return b

    # Go into recursion
    if (f(a) < 0 and f(m) > 0) or (f(a) > 0 and f(m) < 0) :
        return findRoot(f,a,m,epsilon)
    if (f(m) < 0 and f(b) > 0) or (f(m) > 0 and f(b) < 0) :
        return findRoot(f,m,b,epsilon)

def findAllRoots(f,a,b,epsilon) :
    #if f(a) * f(b) >= 0 :
        #raise(AssertionError('f(a) * f(b) >= 0'))
    m = (a + b) / 2

    # Stopping criterion
    if abs(b - a) <= epsilon :
        return [m]

    l = []
    # Check if this is already a root
    if f(a) == 0 :
        l.append(a)
    if f(b) == 0 :
        l.append(b)
    if f(m) == 0 :
        l.append(m)
        
    # Build the lists recursively
    if (f(a) < 0 and f(m) > 0) or (f(a) > 0 and f(m) < 0) :
        l.extend(findAllRoots(f,a,m,epsilon))
    if (f(m) < 0 and f(b) > 0) or (f(m) > 0 and f(b) < 0) :
        l.extend(findAllRoots(f,m,b,epsilon))
    return l
