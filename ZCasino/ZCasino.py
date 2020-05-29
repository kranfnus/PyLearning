# -*-coding:Latin-1 -*

from random import *
from math import *
import os

mise_numero = 0
mise_montant = 0
total_montant = 10

rejouer = True
print("Bienvenue à notre jeu de roulette! ------------------->")
while rejouer:
    print("\nVous disposez de", total_montant,"$")
    print("Faites vos jeux!")
    numero_nok = True
    while numero_nok:
        try:
            mise_numero = int(input("Numéro (0-49):"))
            assert(mise_numero >= 0 and mise_numero <= 49)
        except AssertionError:
            print("Le numéro choisi n'est pas valide!")
        except ValueError:
            print("La valeure saisie n'est pas valide.")
        else:
            numero_nok = False
    mise_nok = True
    while mise_nok:
        try:
            prompt = "Mise (1-" + str(total_montant) + "$):"
            mise_montant = int(input(prompt))
            assert(mise_montant > 0 and mise_montant <= total_montant)
        except AssertionError:
            print("Le montant misé n'est pas valide!")
        except ValueError:
            print("La valeure saisie n'est pas valide.")
        else:
            mise_nok = False
    total_montant -= mise_montant
    print("Rien ne va plus!")
    os.system("pause")

    numero_tire= int(randrange(50))

    parite = lambda numero_tire:numero_tire % 2 == 0
    if parite(numero_tire):
        print("Le numéro gagnant est le:", numero_tire, "noir")
    else:
        print("Le numéro gagnant est le:", numero_tire, "rouge")
    if mise_numero == numero_tire:
        gain = 3 * mise_montant
    elif parite(mise_numero - numero_tire):
        gain = ceil(mise_montant / 2)
    else:
        gain = 0
    total_montant += gain
    if gain > 0:
        print("Vous avez gagné:",gain,"$ et vous disposez maintenant de", total_montant,"$")
    else:
        print("Vous avez perdu!")
    rejouer = (total_montant>0 and input("Voulez-vous rejouer (O/N)? ")[:1] == "O")
    

    
