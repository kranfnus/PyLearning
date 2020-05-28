# -*-coding:Latin-1 -*
import math

def table(nb,max=10):
    """ Fonction affichant les tables de multiplication de 1*nb � max*nb"""
    i = 0 # C'est notre variable compteur que nous allons incrÃ©menter dans la boucle
    while i < max:
        print(i + 1, "*", nb, "=", (i + 1) * nb)
        i += 1

def racines(valeur):
    return valeur**2,math.sqrt(valeur)

# chaine = "Bonjour les ZER0S"
# for lettre in chaine:
    # print(lettre)

f = lambda x:x**2

table(7)
help(table)
var1, var2 = racines(9)
print(var1,var2)
