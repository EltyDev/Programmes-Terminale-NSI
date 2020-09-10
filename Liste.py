class Liste: #création de la classe


#initialisation de l'objet
    def __init__(self, *elements):
        self.list = [None, None] #inititialisation de la liste
        for element in elements: #pour chaque élémment de la liste
            if self.list[0] == None: #si le 1er élément la liste est vide
                self.list[0] = element #le 1er élement de la liste devient élément
                suivant = self.list #et suivant deviens la liste
            else:
                suivant[1] = [element, None] #sinon, le 2e élément de la liste devient [élément, None]
                suivant = suivant[1] #et suivant avance dans la liste chainée

#ajouter un élément à la liste
    def ajouter(self, element):
        suivant = self.list #suivant devien la liste
        while suivant[1] != None: #tant que le deuxième émént du duo n'est pas None
            suivant = suivant[1] #suivant avance dans la liste chainée
        suivant[1] = [element, None] #quand suivant à atteind le None, il remplace le None par l'élément

#inserer
def inserer(self, index, element):
        suivant = self.list
        for _ in range(index-1):
            suivant = suivant[1]
        suivant[1] = [element, suivant[1]]

    def get(self, index):
        suivant = self.list
        for _ in range(index):
            suivant = suivant[1]
        print(suivant[0])

    def __len__(self):
        suivant = self.list
        i = 0
        if self.list[0] == None:
            return i
        while suivant[1] != None:
            i +=  1
            suivant = suivant[1]
        return i+1

    def remove(self, index):
        suivant = self.list
        for _ in range(index-1):
            suivant = suivant[1]
        suivant[1] =  suivant[1][1]

    def replace(self, index, value):
        suivant = self.list
        for _ in range(index):
            suivant = suivant[1]
        suivant[0] = value

    def clear(self):
        self.list = [None, None]

    def __repr__(self):
        return f'{self.list}'
