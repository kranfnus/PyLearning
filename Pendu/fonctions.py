import pickle

def chargement_scores():
    try:
        with open('score','rb') as mon_fichier:
            mon_depickler = pickle.Unpickler(mon_fichier)
            les_scores = mon_depickler.load()
            return les_scores
    except:
        sauvegarde_scores()
        return {}
        
def sauvegarde_scores(scores={}):
    with open('score','wb') as mon_fichier:
        mon_pickler = pickle.Pickler(mon_fichier)
        mon_pickler.dump(scores)
