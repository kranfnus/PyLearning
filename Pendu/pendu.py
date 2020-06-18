# -*-coding:Latin-1 -*
from random import randrange
from donnees import *
from fonctions import *
    
pseudo = input("Votre pseudo? ")
pseudo = pseudo.strip().capitalize()

# Chargement des scores
les_scores = chargement_scores()
for nom in les_scores.keys():
    if nom == pseudo:
        pseudo_a_deja_joue = True
        pseudo_score = les_scores[nom]
        break
    
if pseudo_a_deja_joue:
    print("Heureux de vous revoir {0}, votre dernier score est de {1} points".format(pseudo,pseudo_score))
else:
    print("Bienvenue au jeu du pendu!\nVous avez {0} tentatives pour trouver le mot juste!".format(nombre_essais_max))
    pseudo_score = 0

rejouer = True
victoire = False
num_tentative = nombre_essais_max

while rejouer:
    taille_vocab = len(liste_de_mot)
    mot_tire= liste_de_mot[int(randrange(taille_vocab))]
    mot_tire = mot_tire.lower()
    # print("Le mot à deviner est {0}".format(mot_tire))
    mot_affiche = ""
    for i in range(len(mot_tire)): mot_affiche += "*"
    while not victoire and num_tentative > 0:
        print("Le mot à deviner est {0}".format(mot_affiche))
        proposition = input("Votre proposition? ")
        proposition = proposition.lower()
        proposition_trouvee = False
        for pos in range(len(mot_tire)):
            if mot_tire[pos:].find(proposition) >= 0:
                mot_affiche = mot_affiche[:pos+mot_tire[pos:].find(proposition)]  \
                    + proposition                                                 \
                    + mot_affiche[pos+mot_tire[pos:].find(proposition)+len(proposition):]
                proposition_trouvee = True

        if proposition_trouvee:
            print("Bien vu!")
        else:
            num_tentative -= 1
            if num_tentative >0: print("Raté! Vous avez encore {0} chances!".format(num_tentative))

        if proposition == mot_tire or mot_affiche == mot_tire:
            victoire = True

    if victoire:
        gain = nombre_essais_max - num_tentative
        pseudo_score += gain
        print("Bravo vous trouvé le mot juste (i.e. {0}) et vous avez gagné {1} points.\n" \
              "Votre score est de {2} points".format(mot_tire,gain,pseudo_score))
    else:
        gain = 0
        print("Pendu!! Le mot juste était {0} et votre score est de {1} points".format(mot_tire,pseudo_score))

    reponse = input("Souhaitez-vous refaire une partie(O/N)? ")
    rejouer = (reponse == "O") or (reponse == "Oui")
    if rejouer:
        victoire = False
        num_tentative = 0

# Sauvegarde des scores
if pseudo_a_deja_joue:
    for nom in les_scores.keys():
        if nom == pseudo:
            les_scores[nom] = pseudo_score
else:
    les_scores[pseudo] = pseudo_score
sauvegarde_scores(les_scores)
print("Au revoir!")
