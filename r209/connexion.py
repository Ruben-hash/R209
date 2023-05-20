#!/usr/bin/env python
# -*- coding: utf-8 -*-

import fonctions
from mod_python import Session, apache

def index(req):
    connexion = fonctions.connexionBD()
    curseur = connexion.cursor()
    login = req.form['login']
    curseur.execute("Select id_util,mdp from util where login = '{}'".format(login))
    resultat= curseur.fetchone()
    if resultat is not None:
        id_util, mdp = resultat
        if mdp == req.form['password']:
            session = Session.Session(req)
            session['id_util']=id_util
            session['login']=login
            session.save()
            rep = 'Connexion Réussite'
            link= fonctions.lien('menu.py', 'Menu du site')
            return fonctions.codeHTML('Connexion', rep+link)
        rep = 'Mot de passe incorect'
        link= fonctions.lien('./form-connexion', 'retour')
        return fonctions.codeHTML('Connexion', rep+link)
    rep = 'utilisateur inexistant'
    link= fonctions.lien('./form-connexion.py', 'Retour')
    return fonctions.codeHTML('Connexion', rep+link)
