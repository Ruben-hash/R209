#!/usr/bin/env python
# -*- coding: utf-8 -*-

import fonctions
from mod_python import Session, apache
import psycopg2

def index(req):
    connexion = fonctions.connexionBD()
    curseur = connexion.cursor()
    session = Session.Session(req)
    nom = req.form['nom']
    email = req.form['email']
    tel = req.form['tel']
    adresse = req.form['adresse']
    curseur.execute("INSERT INTO contact (nom, adresse, email, tel, id_util) VALUES (%s, %s, %s, %s, %s);", (nom, adresse, email, tel, session["id_util"]))

    
    connexion.commit()
    connexion.close()
    req.content_type ="text/html"
    rep = 'Ajout de ' + req.form['nom']
    link= fonctions.lien('menu.py', 'Menu du site')
    return fonctions.codeHTML('Ajout ', rep+link)
