## Coding : UTF-8 encoded
"""
# ! Ennoncée  : 

L'exercice consiste à créer une fonction NbrLigne qui a pour paramètre le nom d'un fichier (texte) 
et qui renvoie le nombre de lignes de ce fichier.

"""

 # ! Imports
 
import string
import random
 

list_of_phone_numbers=[]
 
def NbrLigne (texte):
    with open(texte,'r') as f:
        return len(f.readlines())
        

def generate_id(liste_id):
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    num = string.digits
    all = lower + upper + num 
    while True:
        temp = "".join(random.sample(all,9))
        if temp in liste_id:
            continue
        else:
            return temp
        
            
def generate_random_phones():
    prefix = ['20','26','22','50','56','54','90','91']
    num = string.digits
    while True:
        temp = "".join(random.sample(prefix,1))+"".join(random.sample(num,6))
        if temp in list_of_phone_numbers:
            continue
        else:
            list_of_phone_numbers.append(temp)
            return temp
                

def lire_contacts():
    while True:
        nom = input("Entrer le nom du contact :")
        if nom.isalpha():
            return nom
        else:
            continue
 
def lire_numero_tel():
    while True:
        numero = input("Enter le numero du contact : ")
        if (numero[0]+numero[1] in ['20','26','22','50','56','54','90','91']) and numero.isdigit() and len(numero)==8:
            return numero
        else:
            continue
             
# Structure des données :


list_contact = []
liste_of_names  = ['Mark', 'Amber', 'Todd', 'Anita', 'Sandy']
liste_of_phone_numbers =[]
for i in range(len(liste_of_names)):
    liste_of_phone_numbers.append(generate_random_phones())

global dictionaire_des_contact 
dictionaire_des_contact = dict(zip(liste_of_names, liste_of_phone_numbers))

