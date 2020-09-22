class File:

    def __init__(self, *elements):
        self.valeur= []
        for element in elements:
            self.valeur.append(element)

    def entrer(self, valeur):
        self.valeur.insert(0, valeur)

    def sortir(self):
        valeur = self.valeur[-1]
        self.valeur.pop()
        return valeur

    def file_est_vide(self):
        if len(self) == 0:
            return True
        else:
            return False

    def __repr__(self):
        valeur = ""
        for element in self.valeur:
            if element == self.valeur[-1]:
                valeur += str(element)
            else:
                valeur += str(element) + ", "
        return valeur

    def __len__(self):
        return len(self.valeur)
