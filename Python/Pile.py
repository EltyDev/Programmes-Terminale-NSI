class Pile:

    def __init__(self, *elements):
        self.valeur= []
        for element in elements:
            self.valeur.append(element)
        self.valeur.reverse()

    def empiler(self, valeur):
        self.valeur.insert(0, valeur)

    def depiler(self):
        valeur = self.valeur[0]
        self.valeur.pop(0)
        return valeur

    def pile_est_vide(self):
        if len(self) == 0:
            return True
        else:
            return False

    def __repr__(self):
        valeur = ""
        for element in self.valeur:
            valeur += str(element) + "\n" 
        return valeur

    def __len__(self):
        return len(self.valeur)

