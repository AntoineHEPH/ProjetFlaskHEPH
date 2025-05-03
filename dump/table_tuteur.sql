CREATE TABLE tuteur(
    id_tuteur INT PRIMARY KEY,
    nom VARCHAR(100),
    prenom VARCHAR(100),
    telephone VARCHAR(20),
    date_naissance DATE,
    lieu_naissance VARCHAR(100),
    pays VARCHAR(50),
    nb_heures_prestees DECIMAL(5,2),
    nb_annulation INT,
    nb_absence INT,
    type_etablissement VARCHAR(20)
);
