# -*-coding:Latin-1 -*
import os
import pickle

print(os.getcwd())
os.chdir("./ZCasino")
print(os.getcwd())

# Écriture / lecture de texte dans un fichier
mon_fichier = open("config.txt","w")
contenu = mon_fichier.write("mise = 20\ndevise = EUR\n")
print(contenu)
mon_fichier.close()
mon_fichier = open("config.txt","r")
contenu = mon_fichier.read()
print(contenu)
mon_fichier.close()
mon_fichier = open("config.txt","a")
contenu = mon_fichier.write("devise = $\n")
print(contenu)
mon_fichier.close()
with open("config.txt","r") as mon_fichier:
     print(mon_fichier.read())
print(mon_fichier.closed)

# Écriture / lecture d'un objet Python dans un fichier
with open('data','wb') as ton_fichier:
     ton_pickler = pickle.Pickler(ton_fichier)
     score = {
          "joueur 1": 5,
          "joueur 2": 35,
          "joueur 3": 20,
          "joueur 4": 2
          }
     ton_pickler.dump(score)
print(score)
with open('data','rb') as ton_fichier:
     ton_depickler = pickle.Unpickler(ton_fichier)
     score_recupere = ton_depickler.load()
print(score_recupere)

          
