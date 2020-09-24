from Pile import *
pile = Pile()

while True:
    resultat = 0
    prop = input('')
    try:
        prop = int(prop)
    except:
        if prop == 'q':
           break
        elif prop == '+':
            if len(pile) <= 1:
                print("Erreur")
                continue
            else:
                for element in pile.value:
                    resultat += element
                print(resultat) 
            pass
        elif  prop == '-':
            pass
        elif prop == '*':
            pass
        elif prop == '/':
            pass
        elif prop == '**':
            pass
        elif prop == 'sin':
            pass
        elif prop == 'cos':
            pass
        elif prop == 'tan':
            pass
        elif prop == 'exp':
            pass
        elif prop == 'log':
            pass
        elif prop == 'log10':
            pass