# -*-coding:Latin-1 -*
import math

ma_liste = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

i = 0 # Notre indice pour la boucle while
while i < len(ma_liste):
    print(ma_liste[i])
    i += 1 # On incr�mente i, ne pas oublier !

# Cette m�thode est cependant pr�f�rable
for elt in ma_liste: # elt va prendre les valeurs successives des �l�ments de ma_liste
    print(elt)

ma_chaine = "Bonjour � tous"
ma_liste2 = ma_chaine.split(" ")
print(ma_liste2)

ma_liste3 = ['Bonjour', '�', 'tous']
ma_chaine2 = " ".join(ma_liste3)
print(ma_chaine2)

def afficher_flottant(flottant):
    if type(flottant) is not float:
        raise TypeError("Le param�tre attendu est un flottant")
    flottant = str(flottant)
    partie_entiere, partie_flottante = flottant.split(".")
    return ",".join([partie_entiere,partie_flottante[:4]])

def afficher(*parametres, sep=' ', fin='\n'):
    """Fonction charg�e de reproduire le comportement de print.
    
    Elle doit finir par faire appel � print pour afficher le r�sultat.
    Mais les param�tres devront d�j� avoir �t� format�s. 
    On doit passer � print une unique cha�ne, en lui sp�cifiant de ne rien mettre � la fin :

    print(chaine, end='')"""
    
    # Les param�tres sont sous la forme d'un tuple
    # Or on a besoin de les convertir
    # Mais on ne peut pas modifier un tuple
    # On a plusieurs possibilit�s, ici je choisis de convertir le tuple en liste
    parametres = list(parametres)
    # On va commencer par convertir toutes les valeurs en cha�ne
    # Sinon on va avoir quelques probl�mes lors du join
    for i, valeur in enumerate(parametres):
        parametres[i] = str(valeur)
    # La liste des param�tres ne contient plus que des cha�nes de caract�res
    # � pr�sent on va constituer la cha�ne finale
    chaine = sep.join(parametres)
    # On ajoute le param�tre fin � la fin de la cha�ne
    chaine += fin
    # On affiche l'ensemble
    print(chaine, end='')

liste_des_parametres = [1, 4, 9, 16, 25, 36]
print(*liste_des_parametres)

qtt_a_retirer = 7 # On retire chaque semaine 7 fruits de chaque sorte
fruits_stockes = [15, 3, 18, 21] # Par exemple 15 pommes, 3 melons...
# [nb_fruits-qtt_a_retirer for nb_fruits in fruits_stockes if nb_fruits>qtt_a_retirer]
fruits_stockes = [nb_fruits-qtt_a_retirer for nb_fruits in fruits_stockes]
for i,nb_fruits in enumerate(fruits_stockes):
    if nb_fruits < 0:
        fruits_stockes[i] = 0
print(fruits_stockes)

inventaire = [
     ("pommes", 22),
     ("melons", 4),
     ("poires", 18),
     ("fraises", 76),
     ("prunes", 51),
    ]
print(inventaire)
inventaire_permute = [(quantite, fruit) for fruit, quantite in inventaire]
inventaire =[(fruit,quantite) for quantite, fruit in sorted(inventaire_permute, reverse=True)]
print(inventaire)
