# -*-coding:Latin-1 -*
from operator import itemgetter, attrgetter

class DictionnaireOrdonne():
    """ Classe d�finissant un dictionnaire d'un nouveau type caract�ris� par:
    - cl�
    - valeur"""

    # attribut de classe qui s'incr�mente � chaque fois que l'on cr�e un objet de ce type
    nombre_de_dicos = 0 # Le compteur vaut 0 au d�part
    
    def __init__(self, parametre={}, **parametres_nommes):
        """ Constructeur de notre classe.
            Chaque attribue est instanci� par d�faut par une liste vide
            Les param�tres non nomm�s sont �valu�s:
                - S'il s'agit d'un dictionnaire, ses cl�s et valeurs sont ajout� � nos deux listes
                - Sinon, on ne peut pas cr�er notre dictionnaire
            Les param�tres nomm�s sont r�cup�r�s dans un dictionnaire et ses cl�s et valeurs sont ajout� � nos deux listes"""

        try:
            self._dico = {}
            self._cle = []
            self._val = []
            self._pos = -1

            if type(parametre) is dict:
                for par_cle, par_val in parametre.items():
                    self._cle.append(par_cle)
                    self._val.append(par_val)
                    self._dico[par_cle] = par_val

            if parametres_nommes != {}:
                for par_cle, par_val in parametres_nommes.items():
                    self._cle.append(par_cle)
                    self._val.append(par_val)
                    self._dico[par_cle] = par_val

            if type(parametre) is not dict and parametres_nommes == {}:
                raise MyError

            DictionnaireOrdonne.nombre_de_dicos += 1

        except:
            print("D�sol� je ne peux pas cr�er de dictionnaire ordonn� sur la base de vos inputs!")
            
        
    def __getitem__(self, index):
        """Cette m�thode sp�ciale est appel�e quand on fait objet[index]
        Elle redirige vers self._dictionnaire[index]"""
        try:
            if index in self._dico.keys():
                return self._dico[index]
            else:
                return "Alerte ! Notre objet ne contient pas d'index {} !".format(index)
        except:
            print("Cet objet ne contient plus notre dictionnaire (1)")
            
    def __setitem__(self, index, valeur):
        """Cette m�thode est appel�e quand on �crit objet[index] = valeur
        On redirige vers self._dictionnaire[index] = valeur"""
        try:
            self._dico[index] = valeur
            cle_existe = False
            for pos in range(len(self._cle)):
                if self._cle[pos] == index:
                    self._val[pos] = valeur
                    cle_existe = True

            if not cle_existe:
                self._cle.append(index)
                self._val.append(valeur)
                    
        except:
            print("Cet objet ne contient plus notre dictionnaire (2)")

    def __delitem__(self, index):
        """Cette m�thode est appel�e quand on �crit del objet[index]
        On redirige vers del self._dictionnaire[index] et
        on supprime les �l�ments correspondants des deux attributs cle et val"""

        del self._dico[index]
        for pos in range(len(self._cle)):
            if self._cle[pos] == index:
                del self._cle[pos]
                del self._val[pos]           

    def __repr__(self):
        """Quand on entre notre objet dans l'interpr�teur
        Appell�e si on affiche l'objet directement ou
                 si aucune m�thode __str__ n'est d�finie"""
        
        return "{}".format(self._dico)

    def __iter__(self):
        """Cette m�thode renvoie un it�rateur de l'objet"""

        self._pos = 0
        return self # On renvoie l'it�rateur cr�� pour l'occasion

    def __next__(self):
        self._pos += 1
        if self._pos == len(self)+1:
            raise StopIteration
        return self._cle[self._pos-1]

    def __len__(self):
            """M�thode appell�e lorsqu'on souhaite conna�tre la taille de notre objet"""
            try:
                return self._dico.__len__()
            except:
                return 0

    def keys(self):
        """M�thode qui renvoie les cl�s sous forme d'une liste"""
        
        return self._cle

    def values(self):
        """M�thode qui renvoie les valeurs sous forme d'une liste"""
        
        return self._val

    def items(self):
        """M�thode qui renvoie les cl�s et valeurs sous forme d'une liste de tuples"""
        
        return [(self._cle[i],self._val[i]) for i in range(len(self))]

    def sort(self, alpha=True):
        """ M�thode qui trie notre dictionnaire dans l'ordre alphab�tique ou son contraire g�ce au param�tre ordre.
        La m�thode trie l'objet instanci� sans rien retourner"""
  
        matrice = [(x,y) for x, y in self.items()]
        matrice_triee = sorted(matrice, reverse=not alpha)

        self._cle = []
        self._val = []
        self._dico = {}
        
        for i,j in matrice_triee:
            self._dico[i]=j
            self._cle.append(i)
            self._val.append(j)

    def reverse(self):
        """ M�thode qui trie notre dictionnaire dans l'ordre alphab�tique inverse
        en appellant la m�thode sort et le param�tre False"""
  
        self.sort(alpha=False)

    def __add__(self, objet_a_ajouter):
        """L'objet � ajouter est un DictionnaireOrdonne"""

        total = DictionnaireOrdonne()

        for every in self:
            total[every] = self[every]

        for each in objet_a_ajouter:
            if each in total:
                total[each] = total[each] + objet_a_ajouter[each]
            else:
                total[each] = objet_a_ajouter[each]

        return total

    def __iadd__(self, objet_a_ajouter):
        """L'objet � ajouter est un DictionnaireOrdonne"""

        return self + objet_a_ajouter


if __name__ == '__main__':

    dico_fruits = {'pomme': 52, 'poire': 34, 'prune': 128, 'melon': 15}
    dico_legumes = {'carotte': 26, 'haricot': 48}
    fruits = DictionnaireOrdonne()
    fruits["pomme"] = 52
    fruits["poire"] = 34
    fruits["prune"] = 128
    fruits["melon"] = 15
    print(fruits)
    legumes = DictionnaireOrdonne(carotte = 26, haricot = 48)
    print(legumes)
    extras = DictionnaireOrdonne(prune = -7)
    print(extras)
    res = fruits + legumes
    res += extras
    print(res)
