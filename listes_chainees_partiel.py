#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  listes_chainees.py
#  

############################################
# fonctions pour l'interface liste chaînée #
############################################

# ajouter une valeur à la liste chaînée
def ajouter(liste,valeur):
	if liste[0]==None and liste[1]==None:	# si la liste chaînée est vide
		liste[0]=valeur
	else:
		pointeur=liste
		while pointeur[1]!=None:	# on se place en fin de liste chaînée
			pointeur=pointeur[1]
		pointeur[1]=[valeur,None]	# on ajoute en fin de liste chaînée
		
# accéder à l'élément d'indice i (0 à longueur-1)
def acceder(liste,indice):
	i=0
	pointeur=liste
	valeur=None
	if pointeur[0]!=None:	# si liste non vide
		while pointeur[1]!=None and i!=indice:	# tant que indice ou fin de liste pas atteint
			i=i+1
			pointeur=pointeur[1]
		if i==indice:
			valeur=pointeur[0]
	return valeur

#####################################
# programme pour tester l'interface #
#####################################

listec=[None,None]	# initialisation liste chaînée (constructeur)
ajouter(listec,"premier")
ajouter(listec,"second")
ajouter(listec,"troisième")
print(listec)
print(acceder(listec,2))


