from pickle import *

class Exemple:
    """Un petit exemple de classe"""
    
    def __init__(self, nom):
        """Méthode spéciale appelée quand l'objet est créé"""
        
        self.nom = nom
        self.autre_attribut = "une valeur"
        print("C'est le début ! On me créé !")

    def __del__(self):
        """Méthode spéciale appelée quand l'objet est supprimé"""
        
        print("C'est la fin ! On me supprime !")

class Personne:
    """Classe représentant une personne"""
    def __init__(self, nom, prenom):
        """Constructeur de notre classe"""
        
        self.nom = nom
        self.prenom = prenom
        self.age = 33

    def __repr__(self):
        """Quand on entre notre objet dans l'interpréteur
        Appellée si on affiche l'objet directement ou
                 si aucune méthode __str__ n'est définie"""
        
        return "Personne: nom({}), prénom({}), âge({})".format(
                self.nom, self.prenom, self.age)

    def __str__(self):
        """Méthode permettant d'afficher plus joliment notre objet
        Appelée pour afficher l'objet avec print
                ou le convertir en chaîne avec le constructeur str"""
        
        return "{} {}, âgé de {} ans".format(
                self.prenom, self.nom, self.age)

class Protege:
        """Classe possédant une méthode particulière d'accès à ses attributs :
        Si l'attribut n'est pas trouvé, on affiche une alerte et renvoie None"""

        def __init__(self):
            """On crée quelques attributs par défaut"""

            self.a = 1
            self.b = 2
            self.c = 3

        def __getattr__(self, nom):
            """Si Python ne trouve pas l'attribut nommé nom, il appelle
            cette méthode. On affiche une alerte"""

            print("Alerte ! Il n'y a pas d'attribut {} ici !".format(nom))
            print("Par défaut je vous propose la valeur de l'attribut c")

        def __setattr__(self, nom_attr, val_attr):
            """Méthode appelée quand on fait objet.nom_attr = val_attr. On se charge d'enregistrer l'objet"""

            object.__setattr__(self, nom_attr, val_attr)
            # self.nom_attr = val_attr # will generate an infinite loop

        def __delattr__(self, nom_attr):
            """On ne peut supprimer d'attribut, on lève l'exception AttributeError"""
            # raise AttributeError("Vous ne pouvez supprimer aucun attribut de cette classe")

            """Méthode appellée lorsqu'on fait del objet.nom_attr"""
            object.__delattr__(self, nom_attr)

class ZDict:
    """Classe enveloppe d'un dictionnaire"""
    
    def __init__(self):
        """Notre classe n'accepte aucun paramètre"""
        self._dictionnaire = {}
    
    def __del__(self):
        """Méthode appelée quand l'objet est supprimé"""
        print("C'est la fin ! On me supprime !")

    def __getitem__(self, index):
        """Cette méthode spéciale est appelée quand on fait objet[index]
        Elle redirige vers self._dictionnaire[index]"""
        try:
            if index in self._dictionnaire.keys():
                return self._dictionnaire[index]
            else:
                return "Alerte ! Notre objet ne contient pas d'index {} !".format(index)
        except:
            print("Cet objet ne contient plus notre dictionnaire")
            
    def __setitem__(self, index, valeur):
        """Cette méthode est appelée quand on écrit objet[index] = valeur
        On redirige vers self._dictionnaire[index] = valeur"""
        try:
            self._dictionnaire[index] = valeur
        except:
            print("Cet objet ne contient plus notre dictionnaire")

    def __delitem__(self, index):
        """Cette méthode est appelée quand on écrit del objet[index]
        On redirige vers del self._dictionnaire[index]"""
        try:
            del self._dictionnaire[index]
        except:
            print("Cet objet ne contient plus notre dictionnaire")

    def __repr__(self):
        """Quand on entre notre objet dans l'interpréteur
        Appellée si on affiche l'objet directement ou
                 si aucune méthode __str__ n'est définie"""
        try:
            return str(self._dictionnaire)
        except:
            return "Cet objet ne contient plus notre dictionnaire"

    def __str__(self):
        """Méthode permettant d'afficher plus joliment notre objet
        Appelée pour afficher l'objet avec print ou
                pour le convertir en chaîne avec le constructeur str"""
        ma_chaine = ""
        try:
                for cle, val in self._dictionnaire.items():
                    ma_chaine += "La clé {} contient la valeur {}.\n".format(cle, val)
                return ma_chaine
        except:
            return "Cet objet ne contient malheureusement plus notre dictionnaire"
        
    def __getattr__(self, nom):
            """Si Python ne trouve pas l'attribut nommé nom, il appelle
            cette méthode. On affiche une alerte"""
            raise AttributeError("Cet attribut n'existe pas")            

    def __setattr__(self, nom_attr, val_attr):
            """Méthode appelée quand on fait objet.nom_attr = val_attr.
            On se charge d'enregistrer l'objet"""
            object.__setattr__(self, nom_attr, val_attr)
            print("L'attribut {0} a été enregistré avec la valeur {1}".format(nom_attr, val_attr))

    def __delattr__(self, nom_attr):
            """Méthode appellée lorsqu'on fait del objet.nom_attr"""
            object.__delattr__(self, nom_attr)
            print("L'attribut {0} a été supprimé!".format(nom_attr))

    def __contains__(self, nom_attr):
            """Méthode appellée lorsqu'on utilise le mot clé in sur notre objet"""
            try:
                return self._dictionnaire.__contains__(nom_attr)
            except:
                return False

    def __len__(self):
            """Méthode appellée lorsqu'on souhaite connaître la taille de notre objet"""
            try:
                return self._dictionnaire.__len__()
            except:
                return 0

class Duree:
    """Classe contenant des durées sous la forme d'un nombre de minutes
    et de secondes"""
    
    def __init__(self, heure=0, min=0, sec=0):
        """Constructeur de la classe"""
        self.heure = heure # Nombre de minutes
        self.min = min # Nombre de minutes
        self.sec = sec # Nombre de secondes

    def __str__(self):
        """Affichage un peu plus joli de nos objets"""
        return "{0:02}:{1:02}:{2:02}".format(self.heure, self.min, self.sec)

    def __add__(self, objet_a_ajouter):
        """L'objet à ajouter est un entier, le nombre de secondes"""
        # On ajoute la durée
        self.sec += objet_a_ajouter
        # Si le nombre de secondes >= 60
        if self.sec >= 60:
            self.min += self.sec // 60
            self.sec  = self.sec % 60
        if self.min >= 60:
            self.heure += self.min // 60
            self.min    = self.min % 60
            
        # On renvoie la nouvelle durée
        return self

    def __iadd__(self, objet_a_ajouter):
        """L'objet à ajouter est un entier, le nombre de secondes"""
        return self + objet_a_ajouter

    def __eq__(self, autre_duree):
        """Test si self et autre_duree sont égales"""
        return self.sec == autre_duree.sec and self.min == autre_duree.min

    def __gt__(self, autre_duree):
        """Test si self > autre_duree"""
        # On calcule le nombre de secondes de self et autre_duree
        nb_sec1 = self.sec + self.min * 60 + self.heure *3600
        nb_sec2 = autre_duree.sec + autre_duree.min * 60  + autre_duree.heure * 3600
        return nb_sec1 > nb_sec2

class Temp:
    """Classe contenant plusieurs attributs, dont un temporaire"""
    
    def __init__(self):
        """Constructeur de notre objet"""
        self.attribut_1 = "une valeur"
        self.attribut_2 = "une autre valeur"
        self.attribut_temporaire = 5
   
##    def __getstate__(self):
##        """Renvoie le dictionnaire d'attributs à sérialiser avant pickler dump"""
##        dict_attr = dict(self.__dict__)
##        dict_attr["attribut_temporaire"] = 1
##        return dict_attr

    def __setstate__(self, dict_attr):
        """Méthode appellée lors de la désérialisation de l'objet après pickler load"""
        dict_attr["attribut_temporaire"] = 0
        self.__dict__ = dict_attr

def mon_chargement():
    try:
        with open('temp.txt','rb') as mon_fichier:
            mon_depickler = Unpickler(mon_fichier)
            mytemp = mon_depickler.load()
            return mytemp
    except:
        ma_sauvegarde()
        return {}
        
def ma_sauvegarde(mytemp=Temp()):
    with open('temp.txt','wb') as mon_fichier:
        mon_pickler = Pickler(mon_fichier)
        mon_pickler.dump(mytemp)

if __name__ == '__main__':
    
    print("Écrire une méthode spéciale permet de modifier ce comportement par défaut...")
    print("mon_objet = Exemple(""un premier exemple"")")
    mon_objet = Exemple("un premier exemple")
    print("print(mon_objet)")
    print(mon_objet)
    print("del(mon_objet)")
    del(mon_objet)

    p1 = Personne("Micado", "Jean")
    print(repr(p1))
    print(p1)
    chaine = str(p1)
    print(chaine)

    pro = Protege()
    print(pro.a)
    print(pro.b)
    print(pro.e)

    myd = ZDict()
    myd["tom"] = 10
    myd["jim"] = 100
    myd["mag"] = 1000
    myd.pi = 355/113
    print(hasattr(myd,"pi"))
    print(hasattr(myd,"teta"))
    del myd._dictionnaire
    print(len(myd)) # len est compilé en C et attend que __len__ renvoie un entier
                    # En C, le typage est statique (on donne un type à ta variable au moment où on la crée)
                    # Python peut gérer un None, mais pas C si tu lui a dit "ça sera un entier"
                    
    print(myd.__len__())

    d1 = Duree(3, 3, 5)
    print(d1)
    d1 = d1 + 3600
    print(d1)
    d2 = Duree(1, 3, 5)
    print(d2)
    d2 += 3600
    print(d2)
    print("d1 > d2:", d1 > d2)

    vartemp = Temp()
    print(vartemp.__dict__)
    ma_sauvegarde(vartemp)
    vartemp = mon_chargement()
    print(vartemp.__dict__)
    
 
