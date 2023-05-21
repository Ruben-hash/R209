#!/usr/bin/env python
# -*- coding: utf-8 -*-

import fonctions
from mod_python import Session, apache

def index(req):
    connexion = fonctions.connexionBD()
    curseur = connexion.cursor()
    nom = req.form['nom']
    #!/usr/bin/env python
# -*- coding: utf-8 -*-

import fonctions
from mod_python import apache

def index(req):
    connexion = fonctions.connexionBD()
    curseur = connexion.cursor()
    nom = req.form['nom']
    email = req.form['email']
    tel = req.form['tel']
    adresse = req.form['adresse']
    curseur.execute("INSERT INTO contact (nom,email,tel,adresse) VALUES({},{},{},{]);'".format(nom,email,tel,adresse))
    resultat= curseur.commit()
    rep = 'Ajout de ' + req.form['nom']
    link= fonctions.lien('menu.py', 'Menu du site')
    return fonctions.codeHTML('Ajout ', rep+link)
