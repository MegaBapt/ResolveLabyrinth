from os.path import exists
import sys


def droite(droite, labyrinthe, test_colonne, test_ligne, taille):
	if droite != None:
		while labyrinthe.getCase(test_ligne, test_colonne) == " ":
			test_colonne = test_colonne+1
			taille = taille+1
		nombre = Couloir(labyrinthe, taille, 1)
		return "aller à droite "+nombre.avance()

def gauche(gauche, labyrinthe, test_colonne, test_ligne, taille):
	if gauche != None:
		while labyrinthe.getCase(test_ligne, test_colonne) == " ":
			test_colonne = test_colonne-1
			taille = taille+1
		nombre = couloir(labyrinthe, taille, 3)
		return "aller à gauche "+nombre.avance()

def haut(haut, labyrinthe, test_colonne, test_ligne, taille):
	if haut != None:
		while labyrinthe.getCase(test_ligne, test_colonne) == " ":
			test_ligne = test_ligne-1
			taille = taille+1
		nombre = couloir(labyrinthe, taille, 2)
		return "aller en haut "+nombre.avance()

def bas(bas, labyrinthe, test_colonne, test_ligne, taille):
	if bas != None:
		while labyrinthe.getCase(test_ligne, test_colonne) == " ":
			test_ligne = test_ligne+1
			taille = taille+1
		taille = taille-1
		nombre = couloir(self.labyrinthe, self.taille, 4)
		return "aller en bas "+nombre.avance()


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
		print(f"> Creation {self}")

	def __str__(self):
		return f"Intersection ==> H : {self.haut}, B : {self.bas}, G : {self.gauche}, D : {self.droite}. Position {self.ligne}-{self.colonne}"

	def direction(self):

		# La méthode de test de l'arrivée n'est pas suffisante pour stopper tout le traitement.
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
		nombre = Couloir(self.labyrinthe, self.taille - 1, self.DROITE, self.ligne, self.colonne)
		return "aller à droite: "+nombre.avance()

	def analyseGauche(self):
		self.test_colonne -= 2
		self.taille += 2
		while self.labyrinthe.isWall(self.test_ligne, self.test_colonne) and self.labyrinthe.isNotWall(self.test_ligne+1, self.test_colonne+1) and self.labyrinthe.isNotWall(self.test_ligne-1, self.test_colonne+1):
			self.test_colonne -= 1
			self.taille += 1
		nombre = Couloir(self.labyrinthe, self.taille - 1, self.GAUCHE, self.ligne, self.colonne)
		return "aller à gauche: "+nombre.avance()

	def analyseHaut(self):
		self.test_ligne -= 2
		self.taille += 2
		while self.labyrinthe.isWall(self.test_ligne, self.test_colonne) and self.labyrinthe.isNotWall(self.test_ligne+1, self.test_colonne+1) and self.labyrinthe.isNotWall(self.test_ligne+1, self.test_colonne-1):
			self.test_ligne -= 1
			self.taille += 1
		nombre = Couloir(self.labyrinthe, self.taille - 1, self.HAUT, self.ligne, self.colonne)
		return "aller en haut: "+nombre.avance()

	def analyseBas(self):
		self.test_ligne += 2
		self.taille += 2
		while self.labyrinthe.isWall(self.test_ligne, self.test_colonne) and self.labyrinthe.isNotWall(self.test_ligne-1, self.test_colonne+1) and self.labyrinthe.isNotWall(self.test_ligne-1, self.test_colonne-1):
			self.test_ligne += 1
			self.taille += 1
		nombre = Couloir(self.labyrinthe, self.taille-1, self.BAS, self.ligne,  self.colonne)
		return "aller en bas: "+nombre.avance()

	def initArrivee(self):
		self.arrivee = True
		return None

	def isArrivee(self):
		return self.arrivee



##inter = Intersection(None, None, None, None)
#inter.direction()
#inter.initArrivee()
#	print(inter.isArrivee())



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
		print(f"> Création {self}")

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
#		print(f"Couloir.avance : ligne {ligne} - colonne {colonne}")

		memoire1 = None if self.labyrinthe.isNotWall(self.ligne+1, self.colonne) else True
		memoire2 = None if self.labyrinthe.isNotWall(self.ligne-1,self.colonne) else True
		memoire3 = None if self.labyrinthe.isNotWall(self.ligne, self.colonne-1) else True
		memoire4 = None if self.labyrinthe.isNotWall(self.ligne, self.colonne+1) else True

		nombre = Intersection(self.labyrinthe, memoire1, memoire2, memoire3, memoire4, self.ligne, self.colonne) #bas, haut, gauche, droite
		resultDirection = nombre.direction()
		return f"avancé de {self.distance}\n"+resultDirection


class Labyrinthe:
	labi = {}
	ligne = 2
	colonne = 1
	memoire1 = 1
	memoire2 = 1
	memoire3 = 1
	memoire4 = 1
	derniere = 4

	def __init__(self, fileName):
		self.fileName = fileName
		file = None
		try:
			nombre = 1
			if (exists(fileName)):
				file = open(fileName, "r")
				lignes = file.readlines()
				for ligne1 in lignes:
					self.labi[nombre]  = ligne1.rstrip()
					nombre = nombre+1
				print(f"Init du Labyrinthe avec le fichier {fileName}")
				print(f"Je dois arriver à cette postion {len(self.labi)-1} - {len(self.labi[1])-1}")
			else:
				print(f"Le fichier {fileName} n'existe pas")
		except Exception:
			print("Erreur lors de l'init du labyrinthe")
		finally:
			if (file != None):
				file.close()

	def getLabyrinthe(self):
		return self.labi

	def getCase(self, x, y):
		if (x < 0):
#			print(f"getCase : Error OutOfboundIndex x = {x}")
			return "|" # On renvoir un mur sur on est OutOfBoundIndex
		if (y < 0):
#			print(f"getCase : Error OutOfboundIndex y = {y}")
			return "|" # On renvoir un mur sur on est OutOfBoundIndex
		if (x > len(self.labi)):
#			print(f"getCase : Error OutOfboundIndex x = {x} ({len(self.labi)})")
			return "|" # On renvoir un mur sur on est OutOfBoundIndex
		if (y >= len(self.labi[x])):
#			print(f"getCase : Error OutOfboundIndex y = {y} ({len(self.labi[x])})")
			return "|" # On renvoir un mur sur on est OutOfBoundIndex
		return self.labi[x][y]

	def isWall(self, x, y):
		return self.getCase(x, y) == " "

	def isNotWall(self, x, y):
		return self.getCase(x, y) != " "

	def lastDirection(self):
		return self.derniere

	def changeLastDirection(self, ca):
		self.derniere = ca
		return self.derniere

	def départ(self, ligne = 2, colonne = 1):
		memoire1 = None if self.labi[ligne+1][colonne] != " " else True

		memoire2 = None if self.labi[ligne-1][colonne] != " " else True

		memoire3 = None if self.labi[ligne][colonne-1] != " " else True

		memoire4 = None if self.labi[ligne][colonne+1] != " " else True
#		if labi[ligne][colonne+1] != " ":
#			memoire4 = None

#		print(f"ligne {ligne} - colonne {colonne}")
		nombre = Intersection(self, memoire1, memoire2, memoire3, memoire4, ligne, colonne)
#		print(nombre)
		return nombre.direction()

if __name__ == "__main__":
	if (len(sys.argv) <= 1):
		print("Vous devez indiquer le nom du fichier labyrinthe à analyser.")
		print("Exemple : py resolution.py labi2")
		quit()
	else:
		nombre = Labyrinthe(sys.argv[1])
		print("haut = 2")
		print("bas = 4")
		print("gauche = 3")
		print("droite = 1")
		print(nombre.départ())