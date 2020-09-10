tab = [None, None]

def ajouter(tab, element):
    next = tab #On lui donne la valeur de la liste
    while next[1] != None: #On incrémente i jusqu'a qu'on trouve le "None" du dernier tableau
        next = next[1] #A chaque fois on prend le tableau suivant
    next[1] = [element, None] #Et donc on crée le nouveau tableau avec la valeur à la place de "None"

def inserer(tab, index, element):
    next = tab #On lui donne la valeur de la liste
    for _ in range(index-1): #On refait l'opération jusqu'à l'index voulu
        next = next[1] #A chaque fois on prend le tableau suivant
    next[1] = [element, next[1]] #On redéfinis la valeur à celle donné

def acceder(tab, index):
    next = tab #On lui donne la valeur de la liste
    for _ in range(index): #On refait l'opération jusqu'à l'index voulu
        next = next[1] #A chaque fois on prend le tableau suivant
    print(next[0]) #On affiche la valeur

def longueur(tab):
    next = tab #On lui donne la valeur de la liste
    i = 0 #Correspondra à la taille
    tab[0] == None: #Si la liste est vide
        return i
    while next[1] != None: #On incrémente i jusqu'a qu'on trouve le "None" de la dernière valeur
        i += 1
        next = next[1] #A chaque fois on prend le tableau suivant
    return i+1 #On ajoute 1 car il y a une valeur en trop

def supprimer_ind(tab, index):
    next = tab #On lui donne la valeur de la liste
    for _ in range(index-1): #On continue jusqu'à l'index-1 donné pour avoir le tableau juste avant celui de l'index
         next = next[1] #A chaque fois on prend le tableau suivant
    next[1] =  next[1][1] : #Et donc remet à l'ancienne valeur la suite de la liste

def modifier(tab, index, value):
    next = tab #On lui donne la valeur de la liste
    for _ in range(index): #On continue jusqu'à l'index donné
        next = next[1] #A chaque fois on prend le tableau suivant
    next[0] = value #Et donc on donne à l'index donné, la valeur donné

def vider(tab):
    tab = [None, None] #Je remet les valeurs initiales

def supprimer_val(tab,value):
	next = tab
	while next[0] != value:
		next = next[1]
	next[1] = next[1][1]
	next[0] = next[1][0]
