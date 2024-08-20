from os.path import exists
import sys
import labirinthe

if __name__ == "__main__":
	if (len(sys.argv) <= 1):
		print("Vous devez indiquer le nom du fichier labyrinthe à analyser.")
		print("Exemple : py resolution.py labi2")
		quit()
	else:
		nombre = labirinthe.Labyrinthe(sys.argv[1])
		print(nombre.départ())