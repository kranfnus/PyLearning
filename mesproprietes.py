class Personne:
    """Classe définissant une personne caractérisée par :
    - son nom ;
    - son prénom ;
    - son âge ;
    - son lieu de résidence"""
    
    def __init__(self, nom, prenom):
        """Constructeur de notre classe"""
        
        self.nom = nom
        self.prenom = prenom
        self.age = 33
        self._lieu_residence = "Paris" # Notez le souligné _ devant le nom
        
    def _get_lieu_residence(self):
        """Méthode qui sera appelée quand on souhaitera accéder en lecture
        à l'attribut 'lieu_residence'"""     
        
        print("On accède à l'attribut lieu_residence !")
        return self._lieu_residence

    def _set_lieu_residence(self, nouvelle_residence):
        """Méthode appelée quand on souhaite modifier le lieu de résidence"""

        print("Attention, il semble que {} déménage à {}.".format( \
                self.prenom, nouvelle_residence))
        self._lieu_residence = nouvelle_residence

    def _del_lieu_residence(self):
        """Méthode appelée quand on souhaite supprimer le lieu de résidence"""

        print("On supprime l'attribut lieu_residence !")
        del self._lieu_residence

    def _help_lieu_residence(self):
        """Méthode appelée quand on souhaite obtenir de l'aide sur la propriété lieu de résidence"""
        
        chaine = "C'est un lieu de résidence"
        print(chaine)
        
    # On va dire à Python que notre attribut lieu_residence pointe vers une propriété
    lieu_residence = property(_get_lieu_residence, _set_lieu_residence, \
                              _del_lieu_residence, _help_lieu_residence)

if __name__ == '__main__':
    
    bernard = Personne(nom="Nanard", prenom="Bernard")
    print("bernard.nom:",bernard.nom)
    print("bernard.nom:",bernard.prenom)
    print("bernard.nom:",bernard.age)
    bernard.lieu_residence
    bernard.lieu_residence = "Berlin"
    bernard._lieu_residence = "Nouméa"
    print("bernard.lieu_residence:",bernard._lieu_residence)
    help(bernard.lieu_residence)
    # del bernard.lieu_residence
    
    
    
