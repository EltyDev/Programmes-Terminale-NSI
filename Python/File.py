class File:

    def __init__(self, *elements):
        self.valeur= []
        for element in elements:
            self.valeur.append(element)

    def entrer(self, valeur):
        self.valeur.append(valeur)

    def sortir(self):
        if not self.valeur:
            return None
        valeur = self.valeur[0]
        self.valeur.pop(0)
        return valeur

    def file_est_vide(self):
        if not self.valeur:
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

