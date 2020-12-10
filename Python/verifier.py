def verifier(op,a,b):
    """
    Prend en entrée un opérateur entre guillemet, puis deux nombre entiers positifs
    retourne True, si l'opératoin entre a et b est un entier supérieur à zèro, 
    sinon retourne false
    """
    operateur = ["+","-","*","/"]
    assert(op in operateur), "il faut que l'opérateur existe ou sois entre guillemet"
    assert(isinstance(a,int) and a > 0), "il faut que a soit un entier supérieur à zéro."
    assert(isinstance(b,int) and b > 0), "il faut que b soit un entier supérieur à zéro."
    if eval(str(a) + op + str(b)) > 0 and type(eval(str(a) + op + str(b))) == int:
        return True
    else:
        return False

def test():
    """
    fonction pour tester la fonction vérifier; elle ne prend pas d'entrée
    et sors une string si le test à fonctionné  
    """
    assert(isinstance(verifier("+",7,5), bool)), "Erreur dans le programme"
    assert(verifier("+",5,8) == True), "Erreur dans le programme"
    assert(verifier("/",5,3) == False), "Erreur dans le programme"
    assert(verifier("-",4,5) == False), "Erreur dans le programme"
    assert(verifier("*",5,6) == True), "Erreur dans le programme"
    assert(verifier("-",4,10) == False), "Erreur dans le programme"
    assert(verifier("+",6,8) == True), "Erreur dans le programme"

test()