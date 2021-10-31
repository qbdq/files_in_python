## Coding : UTF-8 encoded
"""
# ! Ennoncée  : 

L'exercice consiste à créer une fonction NbrLigne qui a pour paramètre le nom d'un fichier (texte) 
et qui renvoie le nombre de lignes de ce fichier.

"""


def NbrLigne (texte):
    with open(texte,'r') as f:
        return len(f.readlines())
        

