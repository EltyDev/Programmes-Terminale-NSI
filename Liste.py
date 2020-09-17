class Liste: #création de la classe

#initialisation de l'objet
    def __init__(self, *elements):
        self.list = [None, None] #inititialisation de la liste
        for element in elements: #pour chaque élémment de la liste
            if type(element) == list or type(element) == tuple:
                for element1 in element:
                    if self.list[0] == None: #si le 1er élément la liste est vide
                        self.list[0] = element1 #le 1er élement de la liste devient élément
                        suivant = self.list #et suivant deviens la liste
                    else:
                        suivant[1] = [element1, None] #sinon, le 2e élément de la liste devient [élément, None]
                        suivant = suivant[1] #et suivant avance dans la liste chainée
            else:
                if self.list[0] == None: #si le 1er élément la liste est vide
                    self.list[0] = element #le 1er élement de la liste devient élément
                    suivant = self.list #et suivant deviens la liste
                else:
                    suivant[1] = [element, None] #sinon, le 2e élément de la liste devient [élément, None]
                    suivant = suivant[1] #et suivant avance dans la liste chainée

#ajouter un élément à la liste
    def ajouter(self, element):
        suivant = self.list #suivant devient la liste
        while suivant[1] != None: #tant que le deuxième émént du duo n'est pas None
            suivant = suivant[1] #suivant avance dans la liste chainée
        suivant[1] = [element, None] #quand suivant à atteind le None, il remplace le None par l'élément

#inserer un élément dans une liste à un indice donné
    def inserer(self, index, element):
        suivant = self.list #suivant devient la liste
        if index > len(self):
            return
        for _ in range(index-1): #on atteind le
            suivant = suivant[1] #bon rang
        suivant[1] = [element, suivant[1]] #on insère le bon élément à la bonne place

#acceder à un rang particulier
    def acceder(self, index):
        suivant = self.list #suivant devient la liste
        for _ in range(index): #on atteind le bon rang
            suivant = suivant[1]
        return suivant[0]

#longueur de la liste avec len
    def __len__(self):
        suivant = self.list #suivant devient la liste
        i = 0 #on crée un indice pour compter
        if self.list[0] == None: #si le première élément du duo est vaut None
            return i #la liste fait i éléments
        else:
            while suivant[1] != None: #sinon, tant que la dervière valeur du duo n'est pas nulle
                i +=  1 # i prend un point en plus
                suivant = suivant[1] #et on avance dans la liste
        return i+1 # et on retourne i+1

#supprimer un valeur à un indice donné
    def supprimer_ind(self, index):
        suivant = self.list #suivant devient la liste
        if index == 0:
            suivant[0] = suivant[1][0]
            suivant[1] = suivant[1][1]
        else:
            for _ in range(index-1): #on se déplace
                suivant = suivant[1] #jusqu'à l'élément que l'on veut supprimer
            suivant[1] =  suivant[1][1] #et on l'écrase avec la valeur suivante

#pour remplacer la liste
    def remplacer(self, index, valeur):
        suivant = self.list #On lui donne la valeur de la liste
        if index > len(self):
            return
        for _ in range(index): #on se déplace
            suivant = suivant[1] #jusqu'à l'élément que l'on veut modifier
        suivant[0] = valeur #et on modifie la valeur

    def supprimer_val(self, valeur):
        ancien = None
        suivant = self.list #On lui donne la valeur de la liste
        while suivant[0] != valeur: #tant que la valeur de suivant[0] n'est pas égale à la valeur demandée,
            ancien = suivant #on sauvegarde suivant
            suivant = suivant[1] #et on avance dans la liste
        if ancien == None: #si ancien est vide, alors on supprime la premiève valeur
            suivant[0] = suivant[1][0]
            suivant[1] = suivant[1][1]
        else:
            ancien[1] = suivant[1] #sinon, on remplace ancien par suivant[1]

    #on vide la liste
    def vider(self):
        self.list = [None, None] #on remet à zéro la valeur de la liste

    def copie(self):
        prems = Liste()
        suivant = self.list #suivant devient la liste
        while suivant[1] != None: #tant que le deuxième émént du duo n'est pas None
            prems.ajouter(suivant[0])
            suivant = suivant[1] #suivant avance dans la liste chainée
        prems.supprimer_ind(0)
        return prems
    
    def vers_liste(self):
        tab = []
        suivant = self.list #suivant devient la liste
        while suivant[1] != None: #tant que le deuxième émént du duo n'est pas None
            tab.append(suivant[0])
            suivant = suivant[1] #suivant avance dans la liste chainée
        tab.append(suivant[0])
        return tab

    def __repr__(self):
        suivant = self.list #suivant devient la liste
        objet = "|"
        if self.list == [None, None]:
            return f'{objet}{self.list[0]}, {self.list[1]}{objet}'
        while suivant[1] != None: #tant que le deuxième émént du duo n'est pas None
            objet += str(suivant[0]) + ", "
            suivant = suivant[1] #suivant avance dans la liste chainée
        objet += str(suivant[0]) + "|"
        return f'{objet}'
    
    def __str__(self):
        suivant = self.list #suivant devient la liste
        objet = "|"
        if self.list == [None, None]:
            return f'{objet}{self.list[0]}, {self.list[1]}{objet}'
        while suivant[1] != None: #tant que le deuxième émént du duo n'est pas None
            if type(suivant[0]) == str:
                objet += "'" + suivant[0] + "'" + ", "
            else:
                objet += str(suivant[0]) + ", "
            suivant = suivant[1] #suivant avance dans la liste chainée
        objet += str(suivant[0]) + "|"
        return f'{objet}'
    
    def __setitem__(self, index, valeur):
        return self.remplacer(index, valeur)

    def __add__(self, x):
        tab = self.copie()
        suivant = tab.list #suivant devient la liste
        while suivant[1] != None: #tant que le deuxième émént du duo n'est pas None
            suivant = suivant[1] #suivant avance dans la liste chainée
        suivant[1] = x.list  #quand suivant à atteind le None, il remplace le dernier élement par la ouvelle liste
        return tab #On retourne la valeur

a = Liste(1,3,3,5)

b = Liste(7,9,11,11)
j = Liste( 1,2)
print(a, b, j)
a.supprimer_val(3)
print(a)
b.supprimer_ind(3)
print(b)
b.ajouter(13)
print(b)
b.inserer(3,12)
print(b)
b.remplacer(3,'douze')
print(b)
j.vider()
print(j)
c = a + b
c[0] = 3
print(c)
print(c[2])