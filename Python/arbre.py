from graphviz import *
from Pile import *
##definition des fonctions
def creerNoeud(valeur,f_gauche,f_droit):
    noeud=[valeur,f_gauche,f_droit]
    return noeud


def valeur(noeud):
    a= noeud[0]
    return a

def fil_gauche(noeud):
    a= noeud[1]
    return a

def fil_droit(noeud):
    a= noeud[2]
    return a

noeud_racine = creerNoeud('A','B','C')
B = creerNoeud('B',None,None)
C = creerNoeud('C','D',None)
D = creerNoeud('D',None,None)



