#### Imports et définition des variables globales
"""on importe les differents modules dont on a besoin
"""
import csv

FILENAME = "listes.csv"

#### Fonctions secondaires

def read_data(filename:str)->list[str]:
    """retourne le contenu du fichier <filename>
    """
    with open(filename, mode="r", encoding="utf-8") as file:
        reader=csv.reader(file,delimiter=";")
        return [list(map(int,ligne))for ligne in reader ]
    #map transfome  ligne en int et encapsule dans une liste

def get_list_k(data: list[list[int]], k: int) -> list[int]:
    """fonction qui retourne la k-ième liste."""
    if k < 0 or k >= len(data):
        return None
    return data[k]

def get_first(l:list):
    """fonction qui retourne le premier élément de la liste
    """
    if l==[]:
        return None
    return l[0]

def get_last(l:list):
    """fonction qui retourne le dernier élément de la liste
    """
    if l==[]:
        return None
    return l[-1]

def get_max(l:list):
    """fonction qui retourne le maximum de la liste
    """
    if l==[]:
        return None
    return max(l)

def get_min(l:list):
    """fonction qui retourne le minimum de la liste
    """
    if l==[]:
        return None
    return min(l)

def get_sum(l:list):
    """fonction qui retourne la somme de la liste
    """
    if l==[]:
        return None
    return sum(l)


#### Fonction principale


def main():
    """On utilise les differentes fonctions definies au dessus
    """
    data = read_data(FILENAME)
    #on lit les données du fichier

    print("liste de données :")
    for i, liste in enumerate(data):
        print("Liste", i, ":",liste)
    #affiche chaque ligne avec son indice
    k = 1
    print("Liste",k,":", get_list_k(data, k))


if __name__ == "__main__":
    main()
