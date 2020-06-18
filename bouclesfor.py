class RevStr(str):
    """Classe reprenant les méthodes et attributs des chaînes construites
    depuis 'str'. On se contente de définir une méthode de parcours
    différente : au lieu de parcourir la chaîne de la première à la dernière
    lettre, on la parcourt de la dernière à la première.
    
    Les autres méthodes, y compris le constructeur, n'ont pas besoin
    d'être redéfinies"""
    
    def __iter__(self):
        """Cette méthode renvoie un itérateur parcourant la chaîne
        dans le sens inverse de celui de 'str'"""
        
        return ItRevStr(self) # On renvoie l'itérateur créé pour l'occasion

class ItRevStr:
    """Un itérateur permettant de parcourir une chaîne de la dernière lettre
    à la première. On stocke dans des attributs la position courante et la
    chaîne à parcourir"""
    
    def __init__(self, chaine_a_parcourir):
       """On se positionne à la fin de la chaîne"""
       self.chaine_a_parcourir = chaine_a_parcourir
       self.position = len(chaine_a_parcourir)
       
    def __next__(self):
        """Cette méthode doit renvoyer l'élément suivant dans le parcours,
        ou lever l'exception 'StopIteration' si le parcours est fini"""
        
        if self.position == 0: # Fin du parcours
            raise StopIteration
        self.position -= 1 # On décrémente la position
        return self.chaine_a_parcourir[self.position]

class Reverse:
    """Iterator for looping over a sequence backwards."""
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index -= 1
        return self.data[self.index]

def mon_generateur():
    yield 1
    yield 2
    yield 3
    
def intervalle(borne_inf, borne_sup):
    """Générateur parcourant la série des entiers entre borne_inf et borne_sup."""
    
    while borne_inf < borne_sup-1:
        borne_inf += 1
        yield borne_inf

    while borne_inf > borne_sup+1:
        borne_inf -= 1
        yield borne_inf

def intervalle2(borne_inf, borne_sup):
    """Générateur parcourant la série des entiers entre borne_inf et borne_sup.
    Notre générateur doit pouvoir "sauter" une certaine plage de nombres
    en fonction d'une valeur qu'on lui donne pendant le parcours. La
    valeur qu'on lui passe est la nouvelle valeur de borne_inf.
    
    Note: borne_inf doit être inférieure à borne_sup"""
    borne_inf += 1
    while borne_inf < borne_sup:
        valeur_recue = (yield borne_inf)
        if valeur_recue is not None: # Notre générateur a reçu quelque chose
            borne_inf = valeur_recue
        borne_inf += 1

if __name__ == '__main__':

    ma_liste = ["abel", "bernard", "dinonid"]
    for element in ma_liste:
        ma_chaine = element
        print(ma_chaine[::-1])

    ma_chaine = "test"
    iterateur_de_ma_chaine = iter(ma_chaine)
    print(iterateur_de_ma_chaine)
    print(next(iterateur_de_ma_chaine))
    print(next(iterateur_de_ma_chaine))
    print(next(iterateur_de_ma_chaine))
    print(next(iterateur_de_ma_chaine))
    # print(next(iterateur_de_ma_chaine))

    ma_chaine = RevStr("Bonjour")
    print(ma_chaine)
    for lettre in ma_chaine:
        print(lettre)

    ma_chaine = Reverse("Révolution")
    print(ma_chaine)
    for lettre in ma_chaine:
        print(lettre)

    ma_chaine = "Solution"
    print(ma_chaine)
    for lettre in ma_chaine[::-1]:
        print(lettre)

    print(mon_generateur)
    print(mon_generateur())
    mon_iterateur = iter(mon_generateur())
    print(mon_iterateur)
    print(next(mon_iterateur))
    print(next(mon_iterateur))
    print(next(mon_iterateur))

    for nombre in mon_generateur(): # Attention on exécute la fonction
        print(nombre, end=" ")
    print(end="\n")
    for nombre in intervalle(5, 10):
        print(nombre, end=" ")
    print(end="\n")
    for nombre in intervalle(10, 5):
        print(nombre, end=" ")
    print(end="\n")
    
    generateur = intervalle(5, 20)
    for nombre in generateur:
        print(nombre, end=" ")
        if nombre > 17:
            generateur.close() # Interruption de la boucle
    print(end="\n")
        
    generateur = intervalle2(10, 25)
    for nombre in generateur:
        if nombre == 15: # On saute à 20
            generateur.send(20)
        print(nombre, end=" ")
    print(end="\n")

    # Plus d'infos ici: https://docs.python.org/3/reference/expressions.html#yield-expressions
    
