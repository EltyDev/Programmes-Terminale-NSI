from Pile import *
from math import *
#On crées les variables
operation, fonction, pile = ('+', '-', '*', '/', '**'), ('sin', 'cos', 'tan', 'exp', 'log', 'log10'), Pile()

while True: #On brée une boucle infinie
    prop = input('$ ') #On demande chaques propositions avec un style qui fait penser au shell
    try:
        float(prop) #On regarde si c'est une on peut la transformer en nombre décimal
        pile.empiler(prop) #Et si c'est le cas, on l'empile
        print("")
        pile.voir()
    except: #Sinon
        if prop in operation: #Si la proposition est dans les la variable opérations; 
            if len(pile) <= 1:  #et si la longueur de la pile est inférieure ou égale à 1
                print("Erreur : Vous ne pouvez pas faire d'opération avec 1 ou moins de 1 élement") #le programme ne fonctionne pas, et cela retourne un erreur
                continue#on reviens au départ
            else: # si la longueur des bonne
                try: #on essaye de voir si l'opération est faisable
                    resultat = eval(str(pile.valeur[1]) + prop + str(pile.valeur[0])) #si c'est faisable, on l'exécute
                    pile.depiler()#et on enlève les 2 nombres qu'on à utilisé
                    pile.depiler()
                    pile.empiler(float(resultat)) #puis on empile le résultat
                    print(pile)
                    continue #on reviens au départ
                except:# si l'opération est impossible (division par zéro par exemple)
                    print("Erreur: Impossible") #on retourne le fait que ce soit impossible
                    pile.depiler()# et on permet à l'utilisateur de se corriger
                    pile.depiler()
                continue #on reviens au départ
        elif prop in fonction: #si la proposition est dans les fonctions
            if len(pile) < 1: # et que la pile est vide 
                print("Erreur : Vous ne pouvez pas faire d'opération si la pile est vide")
                continue #on reviens ou départ 
            else:# si la pile à au moins un élément
                try:#on essaye si la fonction est possible 
                    resultat = eval(prop + '(' + str(pile.valeur[0]) + ')')
                    pile.depiler() #on dépile les nombres utilisés 
                    pile.depiler()
                    pile.empiler(float(resultat)) #et on empile la réponse
                    print(pile)
                except:#et si l'opération est impossible (log(-n)) 
                    print("Erreur: Impossible")#on revoies que c'est impossible
                    pile.depiler()#et on laisse l'utilisateur se corriger 
                    pile.depiler()
                continue
        elif prop == 'q':
            break #si la proposition est 'q', on quitte le programme
        elif prop == 'r': #si c'est 'r' on remet la pile à zéro
            pile = Pile()
        elif prop == '': #si la proposition est vide, affiche la pile si elle est non vide
            if len(pile) == 0:
                print('Vide')
            else:
                print('\n' + str(pile))
        else: #sinon on revoies une erreur
            print("Erreur: Je suis pas programmé pour cela.")
