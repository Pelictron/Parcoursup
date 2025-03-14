from random import *

def pause(s):
    #créé une pause du nombre de seconde donné
    import time
    time.sleep(s)

def jeu():
    print("""Bonjour, vous venez de lancer le jeu du juste prix. 
Je vous explique, un nombre au hasard compris entre 1 et 100 a été choisit par l'ordinateur. À vous de le trouvez. 
L'ordianteur vous indiquera si votre proposition est trop petite ou trop grande. 
Attention, au bout de dix tentatives fausses, la partie s'arrête vous avez perdu.
Les paroles de l'ordinateur seront en bleu clair.""")
    pause(10)
    print("Préparez vous, le jeu commence !")
    
    x = randint(0,100)
    nb_coups = 0
    print("\033[1;34m") #changer le texte de couleur
    pause(4)
    print("J'ai choisi un nombre à vous de le trouver.")
    
    while nb_coups<10 :
        pause(2)
        réponse = input("Quelle est votre proposition ? ")
        réponse = int(réponse)
        
        if réponse < x :
            pause(2)
            print(f"Votre proposition {réponse} est trop petite par rapport nombre cherché.")
            nb_coups = nb_coups +1 
        
        elif réponse == x :
            pause(2)
            nb_coups = nb_coups +1 
            return f"Bravo vous avez gagné en {nb_coups} coups."
        
        else :
            pause(2)
            print(f"Votre proposition {réponse} est trop grande par rapport au nombre cherché.")
            nb_coups = nb_coups +1
            
    pause(2)
    return "Perdu"