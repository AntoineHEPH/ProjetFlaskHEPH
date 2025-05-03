from flask import render_template, url_for
from . import app, models

@app.route('/')

@app.route('/accueil')
def accueil():
    return render_template('accueil.html',title='Bienvenue')

@app.route('/autres')
def autres():
    return render_template('autres.html',title='Et non !')

@app.route('/tous_tuteurs')
def tuteurs():
    liste_tuteurs = models.Tuteur.query.all()
    return render_template('tous_tuteurs.html', title='Tous les tuteurs', liste_tuteur = liste_tuteurs)

@app.route('/tous_tuteurs/<type_etablissement>')
def tuteurs_tries(type_etablissement):
    liste_trie = models.Tuteur.query.filter(models.Tuteur.type_etablissement == type_etablissement).all()
    return render_template('tuteur_trie.html', title='Tuteurs de lycée', liste_tuteur_trie = liste_trie, etablissement = type_etablissement)


