# coding=utf-8

from flask import Flask, render_template, request, redirect
import jeu

app = Flask(__name__)

@app.route("/")
def index():
    """Initialisation du jeu, avant la première proposition"""
    jeu.mot_a_trouver = jeu.choisir_mot()
    jeu.nb_erreurs = 0
    jeu.deja_proposees = ""
    return render_template("index.html",
                           cache = "_"*len(jeu.mot_a_trouver),
                           nb_erreurs = jeu.nb_erreurs,
                           image = "/static/images/pendu_score_0.png" )


@app.route("/jouer",  methods=["POST"])
def jouer():
    if request.method == "POST":
        proposition = request.form.get("prop")
 
        jeu.nb_erreurs = jeu.verifier_si_erreur(proposition, jeu.mot_a_trouver, jeu.nb_erreurs)
        jeu.deja_proposees = jeu.ajout_lettre(proposition, jeu.deja_proposees)
        affichage = jeu.construction_affichage(jeu.mot_a_trouver, jeu.deja_proposees)
        if jeu.victoire(affichage):
            return render_template("fin.html",
                                   mot = jeu.mot_a_trouver,
                                   nb_erreurs = jeu.nb_erreurs)
        elif jeu.nb_erreurs==9:
            return render_template("fin.html",
                                   mot = jeu.mot_a_trouver,
                                   nb_erreurs = jeu.nb_erreurs,
                                   image = f"/static/images/pendu_score_{jeu.nb_erreurs}.png")
        else :
            
            return render_template("index.html",
                                   nb_erreurs = jeu.nb_erreurs,
                                   cache = affichage,
                                   image = f"/static/images/pendu_score_{jeu.nb_erreurs}.png")


if __name__ == "__main__":
    app.run(debug=True)
    