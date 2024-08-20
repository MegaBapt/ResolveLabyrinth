from os.path import exists
import sys
import labirinthe
import couloir

class Intersection:
    ligne = 0
    colonne = 0
    bas = None
    haut = None
    gauche = None
    droite = None
    arrivee = False
    taille = 0
    test_ligne = 0
    test_colonne = 0
    labyrinthe = None

    HAUT = 2
    BAS = 4
    GAUCHE = 3
    DROITE = 1

    def __init__(self,labyrinthe, bas, haut, gauche, droite, ligne, colonne):
        self.bas = bas
        self.haut = haut
        self.gauche = gauche
        self.droite = droite
        self.labyrinthe = labyrinthe
        self.ligne = ligne
        self.colonne = colonne
        self.test_ligne = ligne
        self.test_colonne = colonne

    def __str__(self):
        return f"Intersection ==> H : {self.haut}, B : {self.bas}, G : {self.gauche}, D : {self.droite}. Position {self.ligne}-{self.colonne}"

    def direction(self):
        if (self.ligne >= len(self.labyrinthe.getLabyrinthe())-1) and (self.colonne >= len(self.labyrinthe.getLabyrinthe()[1])-2):
            return "Vous êtes arrivé!"
        try:
            if self.labyrinthe.lastDirection() == self.BAS:
                if self.gauche != None:
                    return self.analyseGauche()
                if self.bas != None:
                    return self.analyseBas()
                if self.droite != None:
                    return self.analyseDroite()
                if self.haut != None:
                    return "Vous arrivez dans un cul de sac.\nPour repartir il faut "+self.analyseHaut()

            if self.labyrinthe.lastDirection() == self.GAUCHE:
                if self.haut != None:
                    return self.analyseHaut()
                if self.gauche != None:
                    return self.analyseGauche()
                if self.bas != None:
                    return self.analyseBas()
                if self.droite != None:
                    return "Vous arrivez dans un cul de sac.\nPour repartir il faut "+self.analyseDroite()

            if self.labyrinthe.lastDirection() == self.HAUT:
                if self.droite != None:
                    return self.analyseDroite()
                if self.haut != None:
                    return self.analyseHaut()
                if self.gauche != None:
                    return self.analyseGauche()
                if self.bas != None:
                    return "Vous arrivez dans un cul de sac.\nPour repartir il faut "+self.analyseBas()

            if self.labyrinthe.lastDirection() == self.DROITE:
                if self.bas != None:
                    return self.analyseBas()
                if self.droite != None:
                    return self.analyseDroite()
                if self.haut != None:
                    return self.analyseHaut()
                if self.gauche != None:
                    return "Vous arrivez dans un cul de sac.\nPour repartir il faut "+self.analyseGauche()

        except RecursionError:

            return "Naze du gros!!! T'as planté!"

        return "Je ne passerais jamais ici !!!"


    def analyseDroite(self):
        self.test_colonne += 2
        self.taille += 2
        while self.labyrinthe.isWall(self.test_ligne, self.test_colonne) and self.labyrinthe.isNotWall(self.test_ligne+1, self.test_colonne-1) and self.labyrinthe.isNotWall(self.test_ligne-1, self.test_colonne-1):
            self.test_colonne += 1
            self.taille += 1
        nombre = couloir.Couloir(self.labyrinthe, self.taille - 1, self.DROITE, self.ligne, self.colonne)
        return "aller à droite: "+nombre.avance()

    def analyseGauche(self):
        self.test_colonne -= 2
        self.taille += 2
        while self.labyrinthe.isWall(self.test_ligne, self.test_colonne) and self.labyrinthe.isNotWall(self.test_ligne+1, self.test_colonne+1) and self.labyrinthe.isNotWall(self.test_ligne-1, self.test_colonne+1):
            self.test_colonne -= 1
            self.taille += 1
        nombre = couloir.Couloir(self.labyrinthe, self.taille - 1, self.GAUCHE, self.ligne, self.colonne)
        return "aller à gauche: "+nombre.avance()

    def analyseHaut(self):
        self.test_ligne -= 2
        self.taille += 2
        while self.labyrinthe.isWall(self.test_ligne, self.test_colonne) and self.labyrinthe.isNotWall(self.test_ligne+1, self.test_colonne+1) and self.labyrinthe.isNotWall(self.test_ligne+1, self.test_colonne-1):
            self.test_ligne -= 1
            self.taille += 1
        nombre = couloir.Couloir(self.labyrinthe, self.taille - 1, self.HAUT, self.ligne, self.colonne)
        return "aller en haut: "+nombre.avance()

    def analyseBas(self):
        self.test_ligne += 2
        self.taille += 2
        while self.labyrinthe.isWall(self.test_ligne, self.test_colonne) and self.labyrinthe.isNotWall(self.test_ligne-1, self.test_colonne+1) and self.labyrinthe.isNotWall(self.test_ligne-1, self.test_colonne-1):
            self.test_ligne += 1
            self.taille += 1
        nombre = couloir.Couloir(self.labyrinthe, self.taille-1, self.BAS, self.ligne,  self.colonne)
        return "aller en bas: "+nombre.avance()

    def initArrivee(self):
        self.arrivee = True
        return None

    def isArrivee(self):
        return self.arrivee