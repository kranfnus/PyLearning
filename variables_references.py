# -*-coding:Latin-1 -*

# Variables ----->
a = 5
def print_a():
     """Fonction charg�e d'afficher la variable a.
     Cette variable a n'est pas pass�e en param�tre de la fonction.
     On suppose qu'elle a �t� cr��e en dehors de la fonction, on veut voir
     si elle est accessible depuis le corps de la fonction"""
     
     print("La variable a = {0}.".format(a))
     # L'instruction ci-dessous cause une erreur car a est ext�rieur � l'espace locale
     # a = 4
print_a()

def set_var(nouvelle_valeur):
    """Fonction nous permettant de tester la port�e des variables
    d�finies dans notre corps de fonction"""
    
    # On essaye d'afficher la variable var, si elle existe
    try:
        print("Avant l'affectation, notre variable var vaut {0}.".format(var))
    except NameError:
        print("La variable var n'existe pas encore.")
    var = nouvelle_valeur
    print("Apr�s l'affectation, notre variable var vaut {0}.".format(var))
    
set_var(5)
# var a �t� d�fini dans le corps de la fonction donc dans son espace local
# A la fin de l'ex�cution de la fonction l'espace est d�truit
# print(var)

def ajouter(liste, valeur_a_ajouter):
     """Cette fonction ins�re � la fin de la liste la valeur que l'on veut ajouter"""
     liste.append(valeur_a_ajouter)
 
ma_liste=['a', 'e', 'i']
print(ma_liste)
ajouter(ma_liste, 'o')
print(ma_liste)

# R�f�rences ----->
ma_liste1 = [1, 2, 3]
ma_liste2 = ma_liste1
ma_liste2.append(4)
print("Adresse de ma_liste2:{0} et son contenu {1}".format(id(ma_liste2),ma_liste2))
print("Adresse de ma_liste2:{0} et son contenu {1}".format(id(ma_liste1),ma_liste1))
ma_liste2 = list(ma_liste1)
ma_liste2.append(5)
print("Adresse de ma_liste2:{0} et son contenu {1}".format(id(ma_liste2),ma_liste2))
print("Adresse de ma_liste2:{0} et son contenu {1}".format(id(ma_liste1),ma_liste1))
ma_liste1 = [7, 8]
ma_liste2 = [7, 8]
print(ma_liste1 == ma_liste2)
print(ma_liste1 is ma_liste2)

i = 4 # Une variable, nomm�e i, contenant un entier
j = 7
def inc_ij():
     """Fonction charg�e d'incr�menter i et j de 1"""
     global i, j # Python recherche i et j en dehors de l'espace local de la fonction
     i += 1
     j += 1

inc_ij()
print(i, j)
