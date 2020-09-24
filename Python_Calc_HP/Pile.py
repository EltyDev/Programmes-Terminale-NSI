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
        valeur = ""
        if len(self.valeur) == 0:
            return str(self.valeur[0])
        for element in self.valeur:
            valeur += str(element) + "\n" 
        return valeur

    def __len__(self):
        return len(self.valeur)

    def __str__(self):
        valeur = ""
        if len(self.valeur) == 0:
            return str(self.valeur[0])
        for element in self.valeur:
            valeur += str(element) + "\n" 
        return valeur
