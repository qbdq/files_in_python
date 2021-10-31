
""""
#!Ennoncée:

ans une société multinationale, on reçoit plusieurs candidatures. Pour bien mener la 
campagne de recrutement, on souhaite gérer un fichier typé intitulé concours.txt qui comporte 
les enregistrements relatifs aux candidats d’un concours. Chaque enregistrement est composé 
de : NCIN, NOM, PRENOM, AGE, DECISION : (type contenant les identificateurs suivants : 
Ad (admis), R (refusé), Aj (ajourné), et séparés par point-virgule (;)
"""


# ! N.B : On suppose que les fichiers seront mis à la racine du lecteur D.

# * Imports 
from Utilities import *





# TODO: saissir les methodes qui vont nous aider a remplir un employe 
def saisir_CIN():
    print("Note : un CIN Dois contentir 8 digits et commence par 1 ou 0")
    while True:
        cin = input("Saisir le CIN de l'employée : ")
        if len (cin) == 8 :
            return cin
        else:
            print("Carte d'identitée national invalide")
        
def saisir_age():
    while True:
        age = input("Saisir l'age de l'employe : ")
        if age.isdigit() and (int(age) >= 18 and int(age) <60): 
            return age
        else:
            pass
        
        

def saisir_nom():
    while True:
        name = input("Saisir le nom de l'employe  : ")
        if name.isalpha() and name.count(" ") == 0:
            return name
        else:
            print("Nom invalide")

def saisir_prenom():
    prenom = input("Saisir le prenom de l'employe  : ")
    while True: 
        if prenom.isalpha() and prenom.count(" ") == 0:
            return prenom
        else:
            print("Prenom invalide ")


def saisir_decision():
    print("1 - Admis")
    print("2 - Refusé")
    print("3 - Ajourné")
    while True:
       desc = input("Saisir la decision finale : ")
       if desc == '1' :
           return "Ad"
       elif desc == '2' :
           return "R"
       elif desc == '3' :
           return "Aj"
       else:
           print(desc)
           print("descision invalide")
        
        


#TODOs:Définir la fonction saisir() qui permet de remplir les données relatives aux candidats 
# dans le fichier concours.txt en contrôlant la saisie de la décision.

# * This function will return Multiple variables : "" NCIN, NOM, PRENOM, AGE, DECISION " separted by ";"
def remplir_employe() -> None:
    cin  = saisir_CIN()
    name = saisir_nom()
    prenom = saisir_prenom()
    age = saisir_age()
    decision = saisir_decision()
    employe_list = [cin,name,prenom,age,decision]
    employe_final = ";".join(employe_list)
    
    
    del employe_list
    del cin
    del name
    del prenom
    del age
    del decision
    
    print(employe_final)
    try:
      with open("concours.txt","a") as f:
        f.write(employe_final)
    except:
      with open("concours.txt","w") as f:
        f.write(employe_final)
    
    del employe_final
    



# TODO : Définir la fonction admis() qui permet créer le fichier admis.txt comportant les 
# données relatives aux candidat admis

def admis():
    try:
        liste_des_admis = []
        with open("concours.txt","r") as f:
            for line in f:
                if line.endswith("ad\n"):
                    liste_des_admis.append(line)
        try:
          with open("admis.txt","a") as f:
              for line in liste_des_admis:
                  if line in f.readlines():
                      pass
                  else:   
                    f.write(line)
        except:
          with open("admis.txt","w") as f:
              for line in liste_des_admis:
                  f.write(line)
    except:
      print(" le fichier concours n'exsiste pas ")


# TODO: """créer la fonction attente() qui produira à partir du fichier admis.txt, un nouveau 
# fichier intitulé attente.txt comportant les données relatives aux candidats admis et âgés plus que 30 ans.
# Une ligne du fichier attente.txt comprend le NCIN, le NOM et PRENOM d’un candidat, séparés par point-virgule (;)

def attent():
    try:
      liste_employe = []
      with open("admis.txt","r") as f:
          for line in f:
              liste_employe = line.split(";")
              if int(liste_employe[3]) >= 30:
                  try:
                    with open("attent.txt","a") as at:
                        if liste_employe[0] not in at:    
                            final_employe = ";".join([x for x in liste_employe[:3]])
                            at.write(final_employe+"\n")
                  except:
                    with open("attent.txt","r") as at:
                        if liste_employe[0] not in at:
                            final_employe = ";".join([x for x in liste_employe[:3]])
                            at.write(final_employe+"\n")
                    del liste_employe
                  del final_employe
    except:
      print(" le fichier admis.txt n'exsiste pas")
#TODO: Définir la fonction statistiques(dec) qui permet de calculer le pourcentage des 
# candidats pour la décision dec (admis, refusé et ajourné). Exemple 
# Le pourcentage des candidats admis = (Nombre des candidats admis / Nombre des candidats) *100

def statistiques(desc):
    try:
      with open("concours.txt","r") as f:
            total_des_condidats = NbrLigne("concours.txt")
            nombre_des_condidats_admis = 0
            nombre_des_condidats_refuse = 0
            nombre_des_condidats_ajourne = 0
            for line in f:
                
                if line.endswith(";Ad\n") or line.endswith(";Ad"):
                    nombre_des_condidats_admis +=1
                elif line.endswith("R\n") or line.endswith(";R"):
                    nombre_des_condidats_refuse +=1
                else :
                    nombre_des_condidats_ajourne +=1

            if desc.strip().lower() == "admis" :
                return (nombre_des_condidats_admis / total_des_condidats) * 100
            elif desc.strip().lower() == "refuse" :
                return (nombre_des_condidats_refuse / total_des_condidats) * 100
            elif desc.strip().lower() == "ajourne":
                return (nombre_des_condidats_ajourne / total_des_condidats) * 100
            else:
                return None
            
    except:
      print("Le fichier concours n'exsiste pas")


#TODO  : Définir la fonction supprimer() qui supprimera du fichier admis.txt les candidats âgés plus que 30 ans
# ! opens the file in r with mode ("r+") and makes use of seek to reset the f-pointer then
# ! truncate to remove everything after the last write.
def supprimer():
    try:
        with open("admis.txt",'r+') as f:
            d = f.readlines()
            f.seek(0)
            for line in d:
                liste_employe = line.split(";")
                if int(liste_employe[3]) < 30:
                    f.write(line)
            f.truncate()
    except:
      print("Le fichier admis.txt n'exsiste pas")
if __name__ == '__main__':
    supprimer()

    