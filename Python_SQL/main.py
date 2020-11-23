from sqlite3 import *

connexion, curseur = None, None # On définis ces variables en dehors de la boucle infini pour pouvoir les stocké à l'extérieur d'elle

def ouverture_base(fichier):
    connexion = connect(fichier) # On ouvre la base de donnée
    curseur = connexion.cursor() # On crée un curseur
    return (connexion, curseur) # Et on les retournes

def fermeture_base(connexion, curseur):
    curseur.close() # On ferme avant le curseur
    connexion.close() # Puis la base 
    curseur, connexion = None, None # Et enfin on remet à zéro les variables

def requete(requete_sql, curseur):
    curseur.execute(requete_sql) # On exécute la requête
    return curseur.fetchall() # On retourne le résultat de la requête

def modification(connexion):
    connexion.commit() # On sauvegarde les modifications

def affichage(liste_resultat):
    affichage = "\n" # Contiendra l'affichage de la requête
    maximum = [] # Contiendra les longueurs maximales en chaine de caractère de chaque attributs de la requête
    for index in range(len(liste_resultat[0])):
        maximum.append(len(str(liste_resultat[0][index]))) # On ajoute au tableau à chaque itération la premieur longueur correspondant à l'index
        for ligne in liste_resultat:
            if maximum[index] <= len(str(ligne[index])): # On vérifie pour chaque ligne si sa longueur est supérieur à la précédente 
                maximum[index] = len(str(ligne[index])) # Si c'est le cas, sa valeur devient la maximum de l'attribut en attendant la prochaine itération
    for ligne in liste_resultat:
        for _ in range(sum(maximum)+3*len(maximum)+1): # On met la somme total des longueur maximal de chaque attribut + le nombre d'espaces qui correspond à 2 fois le nombre d'attribut + le nombre de barre qui correspont au nombre total des attributs + 1
            affichage += "-" # On affiche une barre pour chaque itération
        affichage += "\n| " # On commence l'itération de la ligne en passant une ligne puis en mettant une barre et un espace
        for index, valeur in enumerate(ligne):
            affichage += str(valeur) + " " # On ajoute la chaine de caractère correspondant à l'attribut avec un espace
            if len(str(valeur)) < maximum[index]: # On vérifie si l'attribut est plus petit que la longueur maximal de l'attribut
                for _ in range(maximum[index] - len(str(valeur))): #  Si c'est le cas, on itère le nombre manquant d'espace
                    affichage += " " # On affiche les espaces 
            affichage += "| " # On affiche une barre et un espace avant de passer à un autre attribut
        affichage += "\n" # On passe une ligne avant de changer de "ligne" 
        if liste_resultat[-1] == ligne: # On regarde si la ligne est la dernière
            for _ in range(sum(maximum)+3*len(maximum)+1): # On met le nombre total de longueur maximal de chaque attribut + le nombre d'espaces qui correspond à 2 fois le nombre d'attribut + le nombre de barre qui correspont au nombre total des attributs + 1
                affichage += "-" # On affiche une barre pour chaque itération
    return affichage # On retourne le résultat

while True:
    commande = input("\n$ ")
    if commande == "o":
        while connexion == None:
            fichier = input("$ Nom du fichier : ") # On demande le nom de la base de donnée
            if fichier[-3:] == ".db":
                print("\nLa base de donnée a été ouverte/créée avec succès.")    
                connexion, curseur = ouverture_base(fichier) # On récupère ces deux variables depuis un table
            else:
                print("\nLa base de donnée n'est pas dans une extension conforme, veuillez réessayer.\n")
    elif commande == "f":
        if connexion == None: # Si aucune base est ouverte
            print("\nVous n'avez pas de base de donnée ouverte.")
        else:
            fermeture_base(connexion, curseur)
    elif commande == "e":
        modification(connexion)
        print("\nLa base donnée a été sauvegardé avec succès.")
    elif commande == "r":
        if connexion == None:  # Si aucune base est ouverte
            print("\nVous n'avez pas de base de donnée ouverte.")
        else:
            sortie = None
            while sortie == None:
                requete_sql = input("$ Requête SQL : ") # On demande la requête SQL voulu
                try: # On essaye les 2 lignes suivant car elles sont suceptible de crée une erreur
                    sortie = requete(requete_sql, curseur) # On envoie la requête
                    print(affichage(sortie)) # On affiche la requête formaté
                except Exception as erreur: # Si on a une erreur, on la met dans la variable error
                    print('\nRequête SQL invalide : "' + str(erreur) + '"\n') # Et on affiche l'erreur
    elif commande == "q":
        if connexion != None: # Si une base est encore ouverte
            print("\nVous devez fermez la base de donnée avant de quitter.")
        else:
            break # On sort de la boucle
    else:
        print("\nCommande inconnue.")

