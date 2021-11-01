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
                    if int(row[-1]) > 10000 : 
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
                    count += int(row[-1])
            return "La moyenne de voix obtenues = {:.2f}".format(count/i)        
        # * le gagnant dans cette campagne,
        elif Operation == 4:
            max = 0
            max_indice = 0
            for i,row in enumerate(data):
                if i != 0 :
                    if max < int(row[-1]) :
                        max_indice = i
                        max = int(row[-1])
            return "Le Gangant dans cette campagne est : {}  {} , avec {} voix ".format(data[max_indice][1],data[max_indice][0],data[max_indice][-1])
        # * le candidat ayant le moins de voix.
        elif Operation == 5:
            liste_vide =[]
            for row in data:
                try:
                  liste_vide.append(int(row[-1]))
                except:
                  pass
            min = liste_vide[0]
            indice_min = 0
            for i,Nombre in enumerate(liste_vide):
                if min > Nombre:
                    indice_min = i
                    min = Nombre
            return "Le candidat ayant le moins de voix est : {} {} avec {} voix ".format(data[indice_min+1][0], data[indice_min+1][1],data[indice_min+1][-1])
                              
            print(liste_vide)
                
        else:
            print("wrong choice")
            csv.close()
        
    
    

    

# ! Définir la fonction trie

def Trie():
    with open("files/Elections.csv" , "r+") as csvfile :  
        data = list(csv.reader(csvfile , delimiter=','))
        columns = data[0]
        list_to_sort = data[1:]
        list_to_sort.sort(key = lambda x:int(x[-1]) ,reverse=True)

        csvfile.seek(0)
        csvfile.write(",".join(columns)+"\n")
        for row in list_to_sort:
            csvfile.write(",".join(row)+"\n")
        csvfile.truncate()

if __name__ =="__main__":
    Trie()    
