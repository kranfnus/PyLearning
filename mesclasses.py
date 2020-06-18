class Personne: # Définition de notre classe Personne
    """Classe définissant une personne caractérisée par :
    - son nom
    - son prénom
    - son âge
    - son lieu de résidence"""

    # attribut de classe qui s'incrémente à chaque fois que l'on crée un objet de ce type
    nombre_personnes = 0 # Le compteur vaut 0 au départ
    def __init__(self, nom = "Dupont", prenom = "Jean"): # Notre méthode constructeur
        """Constructeur de notre classe. Chaque attribut va être instancié
        avec une valeur par défaut... original
        À chaque fois qu'on crée un objet, on incrémente le compteur"""
        
        self.nom = nom
        self.prenom = prenom
        self.age = 33 # Cela n'engage à rien
        self.lieu_residence = "Paris"
        Personne.nombre_personnes += 1

class TableauNoir:
    """Classe définissant une surface sur laquelle on peut écrire,
    que l'on peut lire et effacer, par jeu de méthodes. L'attribut modifié
    est 'surface'"""
    
    def __init__(self):
        """Par défaut, notre surface est vide"""
        
        self.surface = ""
    def ecrire(self, message_a_ecrire):
        """Méthode permettant d'écrire sur la surface du tableau.
        Si la surface n'est pas vide, on saute une ligne avant de rajouter
        le message à écrire"""

        if self.surface != "":
            self.surface += "\n"
        self.surface += message_a_ecrire
    def lire(self):
        """Cette méthode se charge d'afficher, grâce à print,
        la surface du tableau"""
        
        print(self.surface)
    def effacer(self):
        """Cette méthode permet d'effacer la surface du tableau"""
        self.surface = ""

class Compteur:
    """Cette classe possède un attribut de classe qui s'incrémente à chaque
    fois que l'on crée un objet de ce type"""

    
    objets_crees = 0 # Le compteur vaut 0 au départ
    def __init__(self):
        """À chaque fois qu'on crée un objet, on incrémente le compteur"""
        Compteur.objets_crees += 1
    def combien(cls):
        """Méthode de classe affichant combien d'objets ont été créés"""
        print("Jusqu'à présent, {} objets ont été créés.".format(
                cls.objets_crees))
    combien = classmethod(combien)

class Test:
    """Une classe de test tout simplement"""
    def afficher():
        """Fonction chargée d'afficher quelque chose"""
        print("On affiche la même chose.")
        print("peu importe les données de l'objet ou de la classe.")
    afficher = staticmethod(afficher)

class Test2:
    """Une classe de test tout simplement"""
    def __init__(self):
        """On définit dans le constructeur un unique attribut"""
        self.mon_attribut = "ok"
    
    def afficher_attribut(self):
        """Méthode affichant l'attribut 'mon_attribut'"""
        print("Mon attribut est {0}.".format(self.mon_attribut))

if __name__ == '__main__':
    print("Personne.nombre_personnes:", Personne.nombre_personnes)
    bernard = Personne(prenom="Bernard")
    print("type(bernard):",type(bernard))
    print("bernard.nom:",bernard.nom)
    print("bernard.nom:",bernard.prenom)
    print("bernard.nom:",bernard.age)
    print("bernard.lieu_residence:",bernard.lieu_residence)
    bernard.lieu_residence = "Berlin"
    print("bernard.lieu_residence:",bernard.lieu_residence)
    print("Personne.nombre_personnes:", Personne.nombre_personnes)

    tab = TableauNoir()
    print("tab.surface:",tab.surface)
    tab.ecrire("Cool, ce sont encore les vacances!")
    print("tab.surface:",tab.surface)
    tab.ecrire("Profitez bien de l'été covid!")
    print("tab.surface:",tab.surface)
    print(tab.ecrire)
    print(TableauNoir.ecrire)
    print(help(TableauNoir.ecrire))
    TableauNoir.ecrire(tab,"essai")
    tab.lire()
    print(help(TableauNoir))

    Compteur.combien()
    a = Compteur()
    Compteur.combien()
    b = Compteur()
    Compteur.combien()

    second_test = Test2()
    print(dir(second_test))
    print(second_test.__dict__)
    second_test.__dict__["mon_attribut"] = "plus ok"
    second_test.afficher_attribut()
    print(second_test.__dict__)
    
    
