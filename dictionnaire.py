# -*-coding:Latin-1 -*

mon_dictionnaire = dict()
my_dico = {}

mon_dictionnaire["pseudo"] = "Prolixe"
mon_dictionnaire["mot de passe"] = "*"
print(mon_dictionnaire)
mon_dictionnaire["pseudo"] = "6pri1"
print("mon_dictionnaire[\"pseudo\"] = {}".format(mon_dictionnaire["pseudo"]))
print(mon_dictionnaire)

echiquier = {}
echiquier[("a",1)] = "Tb"
echiquier["b",1] = "Cb"
echiquier["c",1] = "Fb"
echiquier["d",1] = "rb"
echiquier["e",1] = "Rb"
echiquier["f",1] = "Fb"
echiquier["g",1] = "Cb"
echiquier["h",1] = "Tb"
echiquier["a",2] = "Pb"
echiquier["b",2] = "Pb"
echiquier["c",2] = "Pb"
echiquier["d",2] = "Pb"
echiquier["e",2] = "Pb"
echiquier["f",2] = "Pb"
echiquier["g",2] = "Pb"
echiquier["h",2] = "Pb"
print(echiquier)

placard = {"pantalon":6, "chemise":3, "tee-shirt":7}
print(placard)
# del placard["chemise"]
# print(placard)
# placard.pop("pantalon")

autre_dictionnaire = {'pseudo', 'mot de passe'} #ceci est un set et non un dictionnaire
print(autre_dictionnaire)
print(type(autre_dictionnaire))

def fete():
     print("C'est la fête.")

def oiseau():
     print("Fais comme l'oiseau...")

fonctions = {}
fonctions["fete"] = fete # on ne met pas les parenthèses
fonctions["oiseau"] = oiseau
fonctions["oiseau"]() # on essaye de l'appeler

for cle in placard.keys():
    print(cle)
for val in placard.values():
    print(val)
for cle, val in placard.items():
    print("La clé {} contient la valeur {}.".format(cle, val))

qtt_a_retirer = 7 # On retire chaque semaine 7 fruits de chaque sorte
inventaire = {
     "pommes":22,
     "melons":4,
     "poires":18,
     "fraises":76,
     "prunes":51,
    }
print(inventaire)
for fruit in inventaire.keys():
     if inventaire[fruit] > qtt_a_retirer:
          inventaire[fruit] -= qtt_a_retirer
print(inventaire)

def fonction_inconnue(**parametres_nommes):
     """Fonction permettant de voir comment récupérer les paramètres nommés
        dans un dictionnaire"""


     print("J'ai reçu en paramètres nommés : {}.".format(parametres_nommes))
fonction_inconnue() # Aucun paramètre
fonction_inconnue(p=4, j=8)

parametres = {"sep":" >> ", "end":" -\n"}
print("Voici", "un", "exemple", "d'appel", **parametres)
