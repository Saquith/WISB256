class Dobbel :
    links  = 0
    rechts = 0
    boven  = 0
    onder  = 0
    voor   = 0
    achter = 0

    def __init__(self):
        self.links  = 2
        self.rechts = 5
        self.boven  = 6
        self.onder  = 1
        self.voor   = 4
        self.achter = 3

    def moveUp(self) :
        voor1   = self.voor
        boven1  = self.boven
        achter1 = self.achter
        onder1  = self.onder

        self.achter = boven1
        self.boven  = voor1
        self.voor   = onder1
        self.onder  = achter1

    def moveDown(self) :
        voor1   = self.voor
        boven1  = self.boven
        achter1 = self.achter
        onder1  = self.onder

        self.onder  = voor1
        self.voor   = boven1
        self.boven  = achter1
        self.achter = onder1

    def moveLeft(self) :
        boven1  = self.boven
        links1  = self.links
        onder1  = self.onder
        rechts1 = self.rechts

        self.onder  = links1
        self.links  = boven1
        self.boven  = rechts1
        self.rechts = onder1

    def moveRight(self) :
        boven1  = self.boven
        links1  = self.links
        onder1  = self.onder
        rechts1 = self.rechts

        self.rechts = boven1
        self.boven  = links1
        self.links  = onder1
        self.onder  = rechts1

    def __repr__(self) :
        return ('Dobbel: l: %s, r: %s, b: %s, o: %s, v: %s, a: %s' %
                (self.links, self.rechts, self.boven, self.onder, self.voor, self.achter))
    
    def __str__(self) :
        return ('Dobbel: l: %s, r: %s, b: %s, o: %s, v: %s, a: %s' %
                (self.links, self.rechts, self.boven, self.onder, self.voor, self.achter))


aantal = int(input())

L = ["omhoog", "rechts", "omlaag", "links"]
moves = []
for i in range(0, aantal) :
    moves.append(input())

dobbel = Dobbel()
for i in range (0, len(moves)) :
    if (moves[i] == L[0]) :
        dobbel.moveUp()
    elif (moves[i] == L[1]) :
        dobbel.moveRight()
    elif (moves[i] == L[2]) :
        dobbel.moveDown()
    else :
        dobbel.moveLeft()

print(dobbel.boven)
