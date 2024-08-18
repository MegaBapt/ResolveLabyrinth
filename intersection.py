class Intersection:
    bas = None
    haut = None
    gauche = None
    droite = None
    arrivee = False

    def __init__(self, bas, haut, gauche, droite):
        self.bas = bas
        self.haut = haut
        self.gauche = gauche
        self.droite = droite

    def initArrivee(self):
        self.arrivee = True
        return None

    def isArrivee(self):
        return self.arrivee



inter = Intersection(None, None, None, None)
inter.initArrivee()
print(inter.isArrivee())
