from Pile import *
from math import *

operation, fonction, pile = ('+', '-', '*', '/', '**'), ('sin', 'cos', 'tan', 'exp', 'log', 'log10'), Pile()

while True:
    prop = input('$ ')   
    try:
        float(prop)
        pile.empiler(prop)
    except:
        if prop in operation:
            if len(pile) <= 1:
                print("Erreur : Vous ne pouvez pas faire d'opération avec 1 ou moins de 1 élement")
                continue
            else:
                try:
                    resultat = eval(str(pile.valeur[1]) + prop + str(pile.valeur[0]))
                    pile.depiler()
                    pile.depiler()
                    pile.empiler(float(resultat))
                    print(pile)
                except:
                    print("Erreur: Impossible")
                    pile.depiler()
                    pile.depiler()
                continue
        elif prop in fonction:
            if len(pile) < 1:
                print("Erreur : Vous ne pouvez pas faire d'opération avec moins de 1 élement")
                continue
            else:
                try:
                    resultat = eval(prop + '(' + str(pile.valeur[0]) + ')')
                    pile.depiler()
                    pile.depiler()
                    pile.empiler(float(resultat))
                    print(pile)
                except:
                    print("Erreur: Impossible")
                    pile.depiler()
                    pile.depiler()
                continue
        elif prop == 'q':
            break
        elif prop == 'r':
            pile = Pile()
        elif prop == '':
            print('\n' + str(pile) + '\n')
        else:
            print("Erreur: Je suis pas programmé pour cela")
