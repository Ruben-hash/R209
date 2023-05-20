#!/usr/bin/env python
# -*- coding: utf-8 -*-


from mod_python import apache

def generate_form():
    # Créer le contenu HTML du formulaire d'ajout
    form_html = '''
    <!DOCTYPE html>
    <html>
    <head>
      <title>Ajout d'un contact</title>
    </head>
    <body>
      <h1>Ajout d'un contact</h1>
      <form action="ajout.py" method="post">
        <label for="nom">Nom :</label>
        <input type="text" id="nom" name="nom" required><br><br>

        <label for="email">Email :</label>
        <input type="email" id="email" name="email" required><br><br>

        <label for="tel">Téléphone :</label>
        <input type="text" id="tel" name="tel"><br><br>

        <label for="adresse">Adresse :</label>
        <input type="text" id="adresse" name="adresse"><br><br>

        <input type="submit" value="Ajouter">
      </form>
      <br>
      <a href="menu.py">Retour au menu</a>
    </body>
    </html>
    '''

    return form_html

def index(req):
    # Définir le type de contenu de la réponse HTTP
    req.content_type = 'text/html'

    # Générer le contenu HTML du formulaire d'ajout
    form_content = generate_form()

    # Renvoyer le contenu généré en tant que réponse
    return form_content
