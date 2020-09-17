from math import sqrt

class Vecteur:
    #builder
    def __init__(self, x=0, y=0) : #par défaut, x=0 et y=0
        self.x = x
        self.y = y

    #module du vecteur
    def module(self):
        return sqrt(self.x**2+self.y**2)

    def __add__(self, v):
        return Vecteur(self.x + v.x, self.y + v.y)
    
    def __str__(self):
        return "("+ str(self.x)+str(self.y)+")"