from . import app, db
from flask_sqlalchemy import SQLAlchemy

"""class produit(db.Model):
    id_produit = db.Column(db.Integer, primary_key=True)
    nom_produit = db.Column(db.String(100), nullable=True)
    prix_produit = db.Column(db.Float, nullable=False)
    image = db.Column(db.String(100), nullable=True)
    description = db.Column(db.String(100), nullable=True)
    id_cat = db.Column(db.Integer, db.ForeignKey('id_cat'), nullable=False)

    def __repr__(self):
        return '<Produit %r>' % self.id_produit"""


class Tuteur(db.Model):
    id_tuteur = db.Column(db.Integer, primary_key=True, nullable=False)
    nom = db.Column(db.String(50), nullable=True)
    prenom = db.Column(db.String(50), nullable=True)
    telephone = db.Column(db.String(50), nullable=True)
    date_naissance = db.Column(db.Date, nullable=True)
    lieu_naissance = db.Column(db.String(50), nullable=True)
    pays = db.Column(db.String(50), nullable=True)
    nb_heures_prestees = db.Column(db.Numeric(15, 2), nullable=True)
    nb_annulation = db.Column(db.Integer, nullable=True)
    nb_absence = db.Column(db.Integer, nullable=True)
    type_etablissement = db.Column(db.String(50), nullable=True)

    def __repr__(self):
        return f'<Tuteur {self.id_tuteur}>'

