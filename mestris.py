from operator import itemgetter, attrgetter

triage_age = lambda montuple: montuple[1]
triage_moy = lambda objet: objet.moyenne

class Etudiant:

    """Classe représentant un étudiant.

    On représente un étudiant par son prénom (attribut prenom), son âge
    (attribut age) et sa note moyenne (attribut moyenne, entre 0 et 20).

    Paramètres du constructeur :
        prenom -- le prénom de l'étudiant
        age -- l'âge de l'étudiant
        moyenne -- la moyenne de l'étudiant

    """

    def __init__(self, prenom, age, moyenne):
        self.prenom = prenom
        self.age = age
        self.moyenne = moyenne

    def __repr__(self):
        return "<Étudiant {} (âge={}, moyenne={})>".format(
                self.prenom, self.age, self.moyenne)

class LigneInventaire:

    """Classe représentant une ligne d'un inventaire de vente.

    Attributs attendus par le constructeur :
        produit -- le nom du produit
        prix -- le prix unitaire du produit
        quantite -- la quantité vendue du produit.

    """

    def __init__(self, produit, prix, quantite):
        self.produit = produit
        self.prix = prix
        self.quantite = quantite

    def __repr__(self):
        return "<Ligne d'inventaire {} ({}eur X {})>".format(
                self.produit, self.prix, self.quantite)

if __name__ == '__main__':
    
    prenoms = ["Jacques", "Laure", "André", "Victoire", "Albert", "Sophie"]
    print(prenoms)
    prenoms.sort()
    print(prenoms)
    prenoms = ["Jacques", "Laure", "André", "Victoire", "Albert", "Sophie"]
    print(sorted(prenoms))
    print(sorted([1, 8, -2, 15, 9]))
    print(sorted(["1", "8", "-2", "15", "9"]))
    # print(sorted([1, "8", "-2", "15", 9]))

    etudiants = [
        ("Clément", 14, 16),
        ("Charles", 11, 15),
        ("Oriane", 13, 18),
        ("Thomas", 11, 12),
        ("Damien", 12, 17),
    ]
    print(sorted(etudiants))
    print(sorted(etudiants, key=lambda montuple: montuple[2]))
    print(sorted(etudiants, key=itemgetter(2))) # plus rapide sur de gros volumes
    print(sorted(etudiants, key=triage_age))
    print(sorted(etudiants, key=itemgetter(1))) # plus rapide sur de gros volumes
    print(sorted(etudiants, key=itemgetter(1,2))) # plus rapide sur de gros volumes
    
    etudiants = [
        Etudiant("Clément", 14, 16),
        Etudiant("Charles", 11, 15),
        Etudiant("Oriane", 13, 18),
        Etudiant("Thomas", 11, 12),
        Etudiant("Damien", 12, 17),
    ]
    print(etudiants)
    print(sorted(etudiants, key=triage_moy, reverse=True))
    print(sorted(etudiants, key=attrgetter("moyenne"), reverse=True)) # plus rapide sur de gros volumes
    print(sorted(etudiants, key=attrgetter("age", "moyenne"), reverse=True)) # plus rapide sur de gros volumes

    # Création de l'inventaire
    inventaire = [
        LigneInventaire("pomme rouge", 1.2, 19),
        LigneInventaire("orange", 1.4, 24),
        LigneInventaire("banane", 0.9, 21),
        LigneInventaire("poire", 1.2, 24),
    ]
    print(sorted(inventaire, key=attrgetter("prix", "quantite")))
    print(sorted(sorted(inventaire, key=attrgetter("quantite"), reverse=True),key=attrgetter("prix")))
    inventaire.sort(key=attrgetter("quantite"), reverse=True)
    print(sorted(inventaire, key=attrgetter("prix")))
