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

# ! File path will be used :  /files/Contact.txt
output_file = "files\Contacts.txt"
file_copie  = "files\Copie_Contact.txt"
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
    
    def set_name (self,new_name):
        self.name = new_name
    
    def set_phone (self,new_phone):
        self.numero_tel = new_phone
        
    def __repr__(self) -> str:
        return "Contact ID : {} , Nom : {} , Numero de téléphone : {}".format(self.get_contact_id(),self.nom,self.numero_tel)

# * Debug

for i in range(3):
    C =contact("Abderrahen","20202020")
    list_contact.append(C)
    
liste_contact = []

for key,value in dictionaire_des_contact.items():
    C = contact(key,value)
    liste_contact.append(C)



# TODO: Une Methode qui retourne une liste des contact unpickled
def get_unpickled_contact(file_name):
    list_contact_unpickled = []
    with open(file_name,'rb') as Contact_file:
        while True:
            try:
                test = pickle.load(Contact_file)
                list_contact_unpickled.append(test)
            except EOFError:
                break    
        return list_contact_unpickled
    return "File empty"

def affichier_contacts():
    list_contact_unpickled = get_unpickled_contact(output_file)
    for item in list_contact_unpickled:
        print(item)
        
# TODO: Écrire la procédure CreerFichier() qui permet de créer ce fichier en utilisant le
# TODO: package Pickle contentant N contacts.

#liste_contact = []
def CreerFichier(N):
    """
    for i in range(N):
        nom_contact = lire_contacts()
        numero_tel = lire_numero_tel()
        C = contact (nom_contact, numero_tel)
        liste_contact.append(C)
    """ 
    with open(output_file,'w+b') as Contact_file:
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
    C = contact(nom_contact, numero_tel)
    with open(output_file,'a+b') as Contact_file:
        pickled_file = pickle.Pickler(Contact_file)
        pickled_file.dump(C)

def ajoutercontacts(liste):
    with open(output_file,'a+b') as Contact_file:
        for item in liste:
            pickled_file = pickle.Pickler(Contact_file)
            pickled_file.dump(item)
        
# TODO: Écrire la fonction Recherche(nom) qui renvoi le numéro de la personne dont le nom est passé en 
# TODO: paramètre. Si le nom de la personne n'existe pas dans le répertoire alors la fonction renvoi la 
# TODO: constante None (rien).

def Recherche(Nom):
    list_contact_unpickled = get_unpickled_contact(output_file) 
    for item in list_contact_unpickled:
        if item.nom == Nom :
            return item.numero_tel
    return None

def recheche_avance(numero_tel):
    
    list_des_numero = []
    for item in get_unpickled_contact(output_file):
        list_des_numero.append(item.numero_tel)
        
    list_des_indices = []
    if list_des_numero.count(numero_tel) > 1 :
        for i,item in enumerate(list_des_numero):
            if item == numero_tel:
                list_des_indices.append(i)
        return list_des_indices
    else : return -1
    
# TODO: Écrire la fonction modifierContact(nom,num) qui modifie le numéro du contact dont le nom est 
# TODO: transmet en paramètre, cette fonction retourne True si la modification est effectuée correctement  sinon False.
def modifierContact(name , new_phone):
    if Recherche(name) == None: return False
    else:
        list_contact_unpickled = get_unpickled_contact(output_file)
        for item in list_contact_unpickled:
            if item.nom == name:
                item.set_phone(new_phone)
                with open(output_file,'rb+') as f:
                    f.seek(0)
                    for i in list_contact_unpickled:
                         pickled_file = pickle.Pickler(f).dump(i)
                    f.truncate()
                return True
        return False

# TODO: Écrire la procédure Copie() qui crée une copie du fichier Contacts.txt
def Copie():
    with open(file_copie, 'wb+') as copie:
        list_contact_unpickled = get_unpickled_contact(output_file)
        for item in list_contact_unpickled:
            pickled_file = pickle.Pickler(copie).dump(item)
    
# TODO: Écrire la procédure affiche(nomFich) qui affiche à l'écran (objet par objet) les données de tous les 
# TODO: contacts contenus dans le fichier nomFich.

def affiche(Nomfich):
    with open(Nomfich, 'rb') as Contact_file:
        while True:
            try:
                print(pickle.load(Contact_file))
            except EOFError:
                break    
        return None
        
# TODO: Dans un répertoire téléphonique un numéro de téléphone doit exister une seule fois, on suppose que par 
# TODO: erreur nous avons répété quelques numéros sous des noms différents. Écrire la procédure suppDoublants(nomFich)
# TODO: qui affiche à l'écran les numéros en double avant de les supprimer
def suppDoublants(nomFich):
    list_contact_unpickled = get_unpickled_contact(output_file) 
    list_supprimer = []
    list_recuperation = []
    
    for i,item in enumerate(list_contact_unpickled):
        if recheche_avance(item.numero_tel) == -1:
            pass
        else:
            if i not in list_supprimer + list_recuperation:
                list_des_indice_local = recheche_avance(item.numero_tel)
                print("******************************** Duplicated number : {} ********************************".format(item.numero_tel))
                for ix,indice in enumerate(list_des_indice_local):
                    print("{} : {} ".format(ix+1,list_contact_unpickled[indice]))  
                    
                while True:
                    choice = input("Which number you would like to keep in the diractory? : ")
                    dict_helper = dict(zip([i for i in range(1,len(list_des_indice_local)+1)],list_des_indice_local))
                    if int(choice) in dict_helper.keys():
                        for value in dict_helper.values():
                            if value == dict_helper[int(choice)]:
                                list_recuperation.append(value)
                            else:
                                list_supprimer.append(value)
                        break
                    else:
                        print("Wrong choice !")
            else:
                pass
    if list_supprimer:
        list_contact_unpickled = [x for i,x in enumerate(list_contact_unpickled) if i not in list_supprimer]
        with open(output_file,'rb+') as file:
            file.seek(0)
            for item in list_contact_unpickled:
                pickled_file = pickle.Pickler(file).dump(item)
            file.truncate()
    else:
        pass
   
    
# TODO: Écrire la procédure Trier() qui permet de trier les contacts du fichier « Contact.txt » selon l'ordre alphabétique des noms  
def Trie(file_name):
    list_contact_unpickled = get_unpickled_contact(file_name) 
    list_contact_unpickled.sort(key = lambda x:x.nom)

    with open(file_name,'rb+') as file:
            file.seek(0)
            for item in list_contact_unpickled:
                pickled_file = pickle.Pickler(file).dump(item)
            file.truncate()
            return True
    return False
# -------------------------------- MAIN ----------------------------------------------------

if __name__ == '__main__':
    ajoutercontacts(liste_contact)
    ajoutercontacts(liste_contact)
    ajoutercontacts(liste_contact)
    ajoutercontacts(liste_contact)
    affiche(output_file)
    suppDoublants(output_file)
    print("______new file _______")
    affiche(output_file)
    affiche(output_file)
    Trie(output_file)
    print("______sorted file _______")
    affiche(output_file)
     

     
