import random 

def choisir_mot():
    """renvoie un mot pris au hasard pris dans le fichier dicionnaire.txt
    Les mots contenus dans le dictionanire n'ont pas d'accent ni de majuscule."""
    with open("dictionnaire.txt", "r") as fichier:
          dico = fichier.read().splitlines()
    mot = random.choice(dico)
    return mot


def verifier_si_erreur(prop, mot, nb_erreurs):
    """Vérifie si la lettre prop est présente dans la chaîne de caractères mot ou non.
    Si non, l'entier nb_erreur est augmenté de 1.
    Si oui, nb_erreur n'est pas modifié.
    La fonction renvoie l'entier nb_erreur"""
    if prop[0] in mot :
        return nb_erreurs
    else :
        nb_erreurs += 1
        return nb_erreurs


def ajout_lettre(prop, deja_proposées):
    """Si la lettre prop n'est pas dans la chaîne de caractères deja_proposées,
    on ajoute prop à deja_proposé.
    La fonction renvoie une chaîne de caractères contenant les lettres déjà proposées."""
    if prop[0] in deja_proposées :
        return deja_proposées
    else :
        deja_proposées += prop[0]
        return deja_proposées
    
    
def construction_affichage(mot, deja_proposées):
    """Fonction qui renvoie une chaîne de caractères de même longueur que mot.
    Chaque lettre présente dans déja_proposées est conservées, les autres sont remplacées par _"""
    mot_affiché = ""
    for i in range(len(mot)):
        if mot[i] in deja_proposées :
            mot_affiché += mot[i]
        else :
            mot_affiché += "_"
    return mot_affiché


def victoire(mot_affiché):
    """Vérifie si mot_affiché contient des "_".
    Si c'est le cas, la fonction renvoie False, la partie n'est pas gagnée.
    S'il n'y en a plus, c'est que la partie est gagnée, la fonction renvoie True."""
    if "_" in mot_affiché :
        return False
    else :
        return True


if __name__=="__main__":
    #partie pour écrire des tests.
    # Ce morceau du code ne sera pas exécuté par l'import de ce module.
    mot = choisir_mot()
    print(mot)