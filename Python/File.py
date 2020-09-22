class File:

    def __init__(self, *elements):
        self.valeur= []
        for element in elements:
            self.valeur.append(element)

    def entrer(self, valeur):
        self.valeur.append(valeur)

    def sortir(self):
        valeur = self.valeur[0]
        self.valeur.pop(0)
        return valeur

    def file_est_vide(self):
        if len(self) == 0:
            return True
        else:
            return False

    def __repr__(self):
        return f'{self.valeur}'

    def __len__(self):
        return len(self.valeur)

