#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# activité 09 : création d'un tableau de données (entiers)

import random

donnees=[]
# génération d'un tableau de 100 entiers
for i in range(100):
	donnees.append(random.randint(1,1000))	# choix aleatoire entier entre 1 et 1000
print(donnees)

def maximum(table):
	'''
	Cette fonction donne le maximum d'une liste de nombre.
	Elle prend comme argument 'table' une liste.
	Elle retourne un nombre.
	'''
	assert(isinstance(table,list)), "La table doit être une liste." #On vérifie si la variable 'table' est une liste
	maxi = table[0] #La première valeur de maxi sera la première valeur de la liste
	for nombre in table: #On itére tout les valeurs de la liste
		if maxi < nombre: #Si la valeur maxi est plus petit que la valeur de la liste 
			maxi = nombre  #On lui donne cet valeur
	return maxi #On retourne maxi

def minimum(table):
	'''
	Cette fonction donne le maximum d'une liste de nombre.
	Elle prend comme argument 'table' une liste.
	Elle retourne un nombre.
	'''
	assert(isinstance(table,list)), "La table doit être une liste." #On vérifie si la variable 'table' est une liste
	mini = table[0] #La première valeur de maxi sera la première valeur de la liste
	for nombre in table: #On itére tout les valeurs de la liste
		if mini > nombre: #Si la valeur mini est plus grand que la valeur de la liste 
			mini = nombre #On lui donne cet valeur
	return mini #On retourne mini

def rechercher(table, valeur):
	'''
	Cette fonction donne une liste contenant les indexs des occurence d'une valeur dans une liste.
	Elle prend comme argument 'table' une liste et valeur un nombre entier naturel.
	Elle retourne une liste même si elle est vide.
	'''
	assert(isinstance(table,list)), "La table doit être une liste." #On vérifie si la variable 'table' est une liste
	assert(isinstance(valeur,int)), "La valeur doit être un nombre entier naturel." #On vérifie si la variable 'valeur' est un nombre entier naturel
	occurrence = [] #Contiendra la liste des indexs des occurences
	for index in range(len(table)): #On itére tout nombre de 0 à la longueur de la liste - 1
		if table[index] == valeur: #Si la valeur du tableau est égale à la valeur donnée
			occurrence.append(index) #On ajoute l'index de la valeur au tableau
	return occurrence #On retourne les occurences

print(maximum(donnees))
print(minimum(donnees))
print(rechercher(donnees, 434))
print(rechercher(donnees, 4000))
print(maximum(['Octet','Bit']))