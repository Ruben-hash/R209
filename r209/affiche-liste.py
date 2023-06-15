import fonctions
import psycopg2
from mod_python import Session, apache

def index(req):
    req.content_type = "text/plain"
    s = Session.Session(req)
    connexion = fonctions.connexionBD()
    curseur = connexion.cursor()
    input_text = req.form["nom"].lower()
    req.write("<ul>")
    curseur.execute("select nom, id_contact, id_util from contact where lower(nom) like '%{}%' and id_util = {};".format(input_text, s['id_util']))
    resultat = curseur.fetchall()
    for elem in resultat: 
        req.write("<li>{}</li>".format(fonctions.lien("fiche.py?id_contact={}".format(elem[1]), elem[0])))
    req.write("</ul>")
