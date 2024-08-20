from os.path import exists
import sys
import labirinthe
import intersection


class Couloir:
    ligne = 0
    colonne = 0
    distance = 0
    direction = 0
    memoire1 = None
    memoire2 = None
    memoire3 = None
    memoire4 = None
    labyrinthe = None

    def __init__(self, labyrinthe, distance, direction, ligne, colonne):
        self.distance = distance
        self.direction = direction
        self.labyrinthe = labyrinthe
        self.ligne = ligne
        self.colonne = colonne

    def __str__(self):
        return f"Couloir ==> distance : {self.distance}, direction : {self.direction}. Position {self.ligne}-{self.colonne}"


    def avance(self):
        self.labyrinthe.changeLastDirection(self.direction) 
        if self.direction == 1:#droite
            self.colonne += self.distance
        if self.direction == 2:#haut
            self.ligne -= self.distance
        if self.direction == 3:#gauche
            self.colonne -= self.distance
        if self.direction == 4:#bas
            self.ligne += self.distance
#       print(f"Couloir.avance : ligne {ligne} - colonne {colonne}")

        memoire1 = None if self.labyrinthe.isNotWall(self.ligne+1, self.colonne) else True
        memoire2 = None if self.labyrinthe.isNotWall(self.ligne-1,self.colonne) else True
        memoire3 = None if self.labyrinthe.isNotWall(self.ligne, self.colonne-1) else True
        memoire4 = None if self.labyrinthe.isNotWall(self.ligne, self.colonne+1) else True

        nombre = intersection.Intersection(self.labyrinthe, memoire1, memoire2, memoire3, memoire4, self.ligne, self.colonne) #bas, haut, gauche, droite
        resultDirection = nombre.direction()
        return f"avancé de {self.distance}\n"+resultDirection