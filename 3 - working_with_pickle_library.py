"""
    Author : Gharsa  Abderrahen
    Coding : UTF-8 
    Date   : 10 / 31 / 2021


    [Exercice 3] :


Un opérateur téléphonique propose de créer un répertoire téléphonique contenant les noms des  personnes et leurs
numéros de téléphones.

 * Ce répertoire est représenté par un fichier texte nommé  # !'Contacts.txt '
 * Ce fichier contiendra des objets de type Contact. Ce dernier est caractérisé par un nom et le numéro de téléphone.

"""
# ! Imports :
from Utilities import *
import pickle 

# ! Class : Contact

class contact(object):
    

    __list_ids = []
    
    def __init__(self,nom,numero_tel) -> None:
        self.__id = generate_id(contact.__list_ids)
        self.nom = nom
        self.numero_tel = numero_tel
        contact.__list_ids.append(self.__id)

    def get_contact_id(self):
     return self.__id
    
    def __str__(self) -> str:
        return "Contact ID : {} , Nom : {} , Numero de téléphone : {}".format(self.get_contact_id(),self.nom,self.numero_tel)

# * Debug
"""
for i in range(3):
    C =contact("Abderrahen","20202020")
    list_contact.append(C)
    
for C in list_contact:
    print(C)

liste_contact = []

for key,value in dictionaire_des_contact.items():
    C = contact(key,value)
    liste_contact.append(C)

"""

# ! File path will be used :  /files/Contact.txt
file_name  = "\files\Contact.txt"

# TODO: Écrire la procédure CreerFichier() qui permet de créer ce fichier en utilisant le
# TODO: package Pickle contentant N contacts.

liste_contact = []
def CreerFichier(N):
    for i in range(N):
        nom_contact = lire_contacts()
        numero_tel = lire_numero_tel()
        C = contact (nom_contact, numero_tel)
        liste_contact.append(C)
        
    with open(r"\files\Contacts.txt",'wb') as Contact_file:
        pickled_file = pickle.Pickler(Contact_file)
        for C in liste_contact:
            pickled_file.dump(C)
            
        




# TODO: Écrire la procédure ajouterContact(nom,telephone) qui ajoute les données d'une personne (nom,téléphone)  
# TODO: sur un enregistrement à la fin du fichier Contacts.txt. Si le numéro de téléphone ne contient 
# TODO: pas huit chiffres un message d’erreur sera affiché.

def ajouterContact():
    
    print("**************** Ajouter un contact ! **************** ")
    nom_contact = lire_contacts()
    numero_tel = lire_numero_tel()
    


# TODO: Écrire la fonction Recherche(nom) qui renvoi le numéro de la personne dont le nom est passé en 
# TODO: paramètre. Si le nom de la personne n'existe pas dans le répertoire alors la fonction renvoi la 
# TODO: constante None (rien).


# TODO: Écrire la fonction modifierContact(nom,num) qui modifie le numéro du contact dont le nom est 
# TODO: transmet en paramètre, cette fonction retourne True si la modification est effectuée correctement  sinon False.


# TODO: Écrire la procédure Copie() qui crée une copie du fichier Contacts.txt


# TODO: Écrire la procédure affiche(nomFich) qui affiche à l'écran (objet par objet) les données de tous les 
# TODO: contacts contenus dans le fichier nomFich.

# TODO: Dans un répertoire téléphonique un numéro de téléphone doit exister une seule fois, on suppose que par 
# TODO: erreur nous avons répété quelques numéros sous des noms différents. Écrire la procédure suppDoublants(nomFich)
# TODO: qui affiche à l'écran les numéros en double avant de les supprimer

# TODO: Écrire la procédure Trier() qui permet de trier les contacts du fichier « Contact.txt » selon l'ordre alphabétique des noms  


# -------------------------------- MAIN ----------------------------------------------------

if __name__ == '__main__':
    CreerFichier(2)