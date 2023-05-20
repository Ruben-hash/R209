-- Supprimer les tables si elles existent déjà
DROP TABLE IF EXISTS contact;
DROP TABLE IF EXISTS util;

-- Créer la table UTIL
CREATE TABLE util (
  id_util SERIAL PRIMARY KEY,
  login VARCHAR(20) NOT NULL,
  mdp VARCHAR(20) NOT NULL
);

-- Insérer les deux utilisateurs initiaux
INSERT INTO util (login, mdp) VALUES ('truc', '12345');
INSERT INTO util (login, mdp) VALUES ('utilisateur', 'io5ffsz');

-- Créer la table CONTACT
CREATE TABLE contact (
  id_contact SERIAL PRIMARY KEY,
  nom VARCHAR(100) NOT NULL,
  email VARCHAR(100) NOT NULL,
  tel VARCHAR(10),
  adresse VARCHAR(100),
  id_util INT REFERENCES util(id_util)
);
