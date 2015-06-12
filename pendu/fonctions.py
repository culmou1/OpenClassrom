import os
from donnees import *
# -*-coding:latin-1 -*

def nombre_de_vie(lettre,mot):
    if lettre != mot: #regarde si la lettre est dans le mot
        global vie_joueur
        vie_joueur -=1
        print("Vous êtes maintenant a {}".format(vie_joueur))
    else :

def convert_mot(mot):
    transformer_mot_en_liste = mot.split(" ") # convert the world into a list
    return transformer_mot_en_liste

def cree_object(nom_personnage,point_total):
    mon_object = {
        nom_personnage : point_total,
    }
    return mon_object

def enregistrer_score(score_du_personnage):
    with open("donness","ab") as fichier:
        mon_pickler = pickle.Pickler(fichier)
        mon_pickler.dump(score_du_personnage)


def parcourir_mot(mot_transformer):
    for i,lettre in enumerate(mot_transformer):
        return lettre[i]

def decision_lettre(lettre,mot):
    trouver_lettre = False
    for i, len(mot):
        if lettre != parcourir_mot(mot):# envoie chaque lettre du mot
            print("Aucune lettre de trouver")
        else:
            trouver_lettre = True
            return lettre

    if trouver_lettre == True:
        print("Vous avez trouver une lettre")

