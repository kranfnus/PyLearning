class A:
    """Classe A, pour illustrer notre exemple d'héritage"""
    pass # On laisse la définition vide, ce n'est qu'un exemple

class B(A):
    """Classe B, qui hérite de A.
    Elle reprend les mêmes méthodes et attributs (dans cet exemple, la classe
    A ne possède de toute façon ni méthode ni attribut)"""
    
    pass

class Personne:
    """Classe représentant une personne"""
    def __init__(self, nom):
        """Constructeur de notre classe"""
        self.nom = nom
        self.prenom = "Martin"
    def __str__(self):
        """Méthode appelée lors d'une conversion de l'objet en chaîne"""
        return "{0} {1}".format(self.prenom, self.nom)

class AgentSpecial(Personne):
    """Classe définissant un agent spécial.
    Elle hérite de la classe Personne"""
    
    def __init__(self, nom, matricule):
        """Un agent se définit par son nom et son matricule"""
        # On appelle explicitement le constructeur de Personne :
        Personne.__init__(self, nom)
        self.matricule = matricule
    def __str__(self):
        """Méthode appelée lors d'une conversion de l'objet en chaîne"""
        return "Agent {0}, matricule {1}".format(self.nom, self.matricule)

# class MaClasseHeritee(MaClasseMere1, MaClasseMere2):
# L'ordre de définition des classes mères importe

# Hierarchie des exceptions: https://docs.python.org/3/library/exceptions.html
class MonException(Exception):
    """Exception levée dans un certain contexte… qui reste à définir"""
    def __init__(self, message):
        """On se contente de stocker le message d'erreur"""
        self.message = message
    def __str__(self):
        """On renvoie le message"""
        return self.message

class ErreurAnalyseFichier(Exception):
    """Cette exception est levée quand un fichier (de configuration)
    n'a pas pu être analysé.
    
    Attributs :
        fichier -- le nom du fichier posant problème
        ligne -- le numéro de la ligne posant problème
        message -- le problème proprement dit"""
    
    def __init__(self, fichier, ligne, message):
        """Constructeur de notre exception"""
        self.fichier = fichier
        self.ligne = ligne
        self.message = message
    def __str__(self):
        """Affichage de l'exception"""
        return "[{}:{}]: {}".format(self.fichier, self.ligne, \
                self.message)

if __name__ == '__main__':
    agent = AgentSpecial("Fisher", "18327-121")
    agent.nom
    print(agent)
    # les méthodes sont définies dans la classe alors que 
    # les attributs sont directement déclarés dans l'instance d'objet
    print(agent.prenom)
    print(Personne.__str__(agent))
    print(AgentSpecial.__str__(agent))

    print(issubclass(AgentSpecial, Personne)) # AgentSpecial hérite de Personne
    print(issubclass(AgentSpecial, object))
    print(issubclass(Personne, object))
    print(issubclass(Personne, AgentSpecial)) # Personne n'hérite pas d'AgentSpecial

    print(isinstance(agent, AgentSpecial)) # Agent est une instance d'AgentSpecial
    print(isinstance(agent, Personne)) # Agent est une instance héritée de Personne

    # Tutorials on errors / exceptions: https://docs.python.org/3/tutorial/errors.html
    # raise MonException("OUPS... j'ai tout cassé")
    raise ErreurAnalyseFichier("plop.conf", 34, \
                               "Il manque une parenthèse à la fin de l'expression")

