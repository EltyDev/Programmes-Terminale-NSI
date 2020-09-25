class Pile:

    def __init__(self, *elements):
        self.valeur= []
        for element in elements:
            self.valeur.append(element)
        self.valeur.reverse()

    def empiler(self, valeur):
        self.valeur.insert(0, valeur)

    def depiler(self):
        if not self.valeur:
            return None
        valeur = self.valeur[0]
        self.valeur.pop(0)
        return valeur

    def pile_est_vide(self):
        if not self.valeur:
            return True
        else:
            return False

    def __repr__(self):
        return f'{self.valeur}'

    def voir(self):
        valeur = ""
        if len(self.valeur) == 0:
            print('1 : ' + str(self.valeur[0]))
        else:
            for index, element in enumerate(self.valeur):
                if index == len(self):
                    valeur += str(index+1) + " : " + str(element)
                else:
                    valeur += str(index+1) + " : " + str(element) + "\n" 
            print(valeur)

    def __len__(self):
        return len(self.valeur)

    def __str__(self):
        return str(self.valeur)
