#!/usr/bin/python
# -*- coding: utf-8 -*-

import psycopg2
from mod_python import util
def codeHTML(titre, corps):
    # Créer la chaîne de caractères contenant le code HTML
    html = '''
    <!DOCTYPE html>
    <html>
    <head>
      <title>{titre}</title>
    </head>
    <body>
      <h1>{corps}</h1>
    </body>
    </html>
    '''.format(titre=titre, corps=corps)
    return html


def connexionBD():
    # Paramètres de connexion à la base de données
    conn_params = {
        "host":"localhost",
        "dbname": "devweb",
        "user":"devweb",
        "password": "123456"
    }

    # Connexion à la base de données
    conn = psycopg2.connect(**conn_params)
    
    return conn

def lien(url, texte):
    html = '<a href="{}">{}</a>'.format(url,texte)
    return html

def redirectionSiNonconnecte(req, session):
    req.content_type = "text/html"
    if session.is_new():
        util.redirect(req,"./form-connexion.py")
        
