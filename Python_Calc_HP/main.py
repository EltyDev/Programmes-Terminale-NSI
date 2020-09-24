from Pile import *
from math import *

operation, fonction, pile = ('+', '-', '*', '/', '**'), ('sin', 'cos', 'tan', 'exp', 'log', 'log10'), Pile()

while True:
    prop = input('')   
    if prop.isdigit():
        pile.empiler(prop)
    else:
        if prop in operation:
            if len(pile) <= 1:
                print(pile)
                continue
            else:
                resultat = eval(str(pile.valeur[1]) + prop + str(pile.valeur[0]))
                pile.depiler()
                pile.depiler()
                pile.empiler(int(resultat))
                print(resultat)
                continue
        elif prop in fonction:
            if len(pile) >=2:
                print("Erreur : Apprend à compter")
                continue
            else:
                resultat = eval(prop + '(' + str(pile.valeur[0]) + ')')
                pile.depiler()
                pile.depiler()
                pile.empiler(int(resultat))
                print(resultat)
                continue
        elif prop == 'q':
            break
        elif prop == 'r':
            pile = Pile()
        else:
            print("Erreur: Je suis pas programmé pour cela")


