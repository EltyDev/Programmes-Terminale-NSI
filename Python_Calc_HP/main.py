from Pile import *
from math import *

operation, fonction, pile = ('+', '-', '*', '/', '**'), ('sin', 'cos', 'tan', 'exp', 'log', 'log10'), Pile()

while True:
    prop = input('? ')   
    try:
        prop = float(prop)
        pile.empiler(prop)
        print("")
        pile.voir()
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
                    print('\n' + str(resultat) + '\n')
                except:
                    print("\nErreur: Impossible\n")
                    pile.depiler()
                    pile.depiler()
                continue
        elif prop in fonction:
            if len(pile) < 1:
                print("\nErreur : Vous ne pouvez pas faire d'opération avec moins de 1 élement\n")
                continue
            else:
                try:
                    resultat = eval(prop + '(' + str(pile.valeur[0]) + ')')
                    pile.depiler()
                    pile.depiler()
                    pile.empiler(float(resultat))
                    print('\n' + str(resultat) + '\n')
                except:
                    print("\nErreur: Impossible\n")
                    pile.depiler()
                    pile.depiler()
                continue
        elif prop == 'q':
            break
        elif prop == 'r':
            pile = Pile()
        elif prop == '':
            print('')
            pile.voir()
        else:
            print("\nErreur: Je suis pas programmé pour cela\n")
            pile.depiler()
