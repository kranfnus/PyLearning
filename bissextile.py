# Programme testant si une année, saisie par l'utilisateur, est bissextile ou non
# -*-coding:utf-8 -*

annee = input("Saisissez une année : ") # On attend que l'utilisateur fournisse l'année qu'il désire tester
try:
    annee = int(annee)
    if annee<=0:
        raise ValueError("l'année saisie est négative ou nulle")
except ValueError:
    print("La valeur saisie est invalide (l'année est peut-être négative).")
else:    
    if annee % 400 == 0 or (annee % 4 == 0 and annee % 100 != 0):
        print("L'année choisie est bissextile.")
    else:
        print("L'année choisie n'est pas bissextile.")
