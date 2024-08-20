from os.path import exists
import sys
import labirinthe
import intersection

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
			return "|" 
		if (y < 0):
			return "|" 
		if (x > len(self.labi)):
			return "|" 
		if (y >= len(self.labi[x])):
			return "|" 
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

		nombre = intersection.Intersection(self, memoire1, memoire2, memoire3, memoire4, ligne, colonne)
		return nombre.direction()