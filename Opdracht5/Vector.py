import math

class Vector :
    array = []
    size = 0
            
    def __init__(self, n, default=None) :
        self.array = []
        self.size = n
        if default is None :
            default = 0.000000
        if not isinstance(default, list) :
            for i in range(0, n) :
                self.array.append(default)
        else :
            self.array = default

    def __str__(self) :
        printString = "{0:.6f}".format(self.array[0])
        for i in range(1, self.size) :
            s = "{0:.6f}".format(self.array[i])
            printString += "\n%s" % s
        return printString

    def __repr__(self) :
        return  ('Vector | size: %s, array: %s' % (self.size, str(self.array)))

    def __add__(self, other) :
        l = []
        for i in range(0, self.size) :
            l.append(self.array[i] + other.array[i])
        return Vector(self.size, l)
    
    def __sub__(self, other) :
        l = []
        for i in range(0, self.size) :
            l.append(self.array[i] - other.array[i])
        return Vector(self.size, l)

    def scalar(self, alpha) :
        l = []
        for i in range(0, self.size) :
            l.append(self.array[i] * alpha)
        return Vector(self.size, l)
    
    def lincomb(self, other, alpha, beta) :
        return self.scalar(alpha) + other.scalar(beta)

    def inner(self, other) :
        x = 0
        for i in range(0, self.size) :
            x += self.array[i] * other.array[i]
        return x

    def norm(self) :
        x = 0
        for i in range(0, self.size) :
            x += self.array[i]**2
        return math.sqrt(x)

    def proj(self, v) :
        return self.scalar((v.inner(self) / self.inner(self)))

    def length(self) :
        x = 0
        for i in range(0, self.size) :
            x += self.array[i]**2
        return math.sqrt(x)

    def div(self, alpha) :
        l = []
        for i in range(0, self.size) :
            l.append(self.array[i] / alpha)
        return Vector(self.size, l)

def GrammSchmidt(V) :
    count = len(V)
    U = [V[0]]
    W = [V[0].div(V[0].length())]
    for i in range(1, count) :
        U.append(V[i])
        for j in range(len(U) - 1) :
            U[i] -= U[j].proj(V[i])
        W.append(U[i].div(U[i].length()))
    return W
