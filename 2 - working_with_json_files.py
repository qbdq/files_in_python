"""
    Author : Gharsa  Abderrahen
    Coding : UTF-8 
    Date   : 10 / 31 / 2021
    
    
    [Exercice 2] :
    

2) Écrire le code python qui lit le fichier CSV et qui écrit :
 le nombre de candidats ayant plus que 10 000 voix,
 le nombre de candidats âgés de moins de 40 ans,
 la moyenne de voix obtenues,
 le gagnant dans cette campagne,
 le candidat ayant le moins de voix.
3) Écrire une fonction qui trie les résultats issus du fichier "elections.csv" suivant le nombre de voix par 
ordre décroissant et qui sauvegarde le résultat dans un nouveau fichier CSV "resultatsElections.csv".

    
"""

# ! Imports :
import csv
import Utilities




# TODO: Créer un fichier CSV "Elections.csv" contenant tous les candidats d’une campagne électorale, triés 
# TODO: par ordre croissant sur le nom.
# * Done

# ! Définir la fonction Operations
def operation(Operation):
      
    with open("files/Elections.csv" , "r") as csvfile :  
        data = list(csv.reader(csvfile , delimiter=','))
        # * le nombre de candidats ayant plus que 10 000 voix
        count = 0
        if Operation == 1:
            for i,row in enumerate(data):
                if i != 0:
                    if int(row[len(row)-1]) > 100000 : 
                        count += 1
            return "Nombre des condidats ayant plus que 10 000 voix = {}".format(count)
        # * le nombre de candidats âgés de moins de 40 ans
        elif Operation == 2:
            for i,row in enumerate(data):
                if i != 0:
                    if int(row[2]) < 40 : 
                        count += 1
            return "Nombre des condidats Agés de moins de 40 ans = {}".format(count)
        # * la moyenne de voix obtenues
        elif Operation == 3:
            for i,row in enumerate(data):
                if i != 0:
                    count += int(row[len(row)-1])
            return "La moyenne de voix obtenues = {}".format(count/i)        
        # * le gagnant dans cette campagne,
        elif Operation == 4:
            max = 0
            max_indice = 0
            for i,row in enumerate(data):
                if i != 0 :
                    if max < int(row[len(row)-1]) :
                        max_indice = i
            data[max_indice][0]
            return "Le Gangant dans cette campagne est {} , {} , avec {} voix  "
        
        # * le candidat ayant le moins de voix.
        elif Operation == 5:
            max = 0
            min_indice = 0
            for i,row in enumerate(data):
                if i != 0 :
                    if min > row[len(row)-1] :
                        min_indice = i
            return "le condidat ayant le moins de voix  est {} , {} , avec {} voix  ".format(data[0][min_indice], data[1][min_indice], data[3][min_indice])
        else:
            csvfile.close()
        
    
    

    

# ! Définir la fonction trie

def Trie():
    pass


if __name__ =="__main__":
    print(operation(1))
    print(operation(2))
    print(operation(3))
    print(operation(4))
    print(operation(5))