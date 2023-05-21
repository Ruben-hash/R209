#!/usr/bin/env python
# -*- coding:utf-8 -*-

def liste(
def index(req):
    # Créer le contenu HTML du formulaire
    form_html = '''
    <!DOCTYPE html>
    <html>
    <head>
      <title>liste</title>
    </head>
    <body>
      <h1>Mon Formulaire</h1>
    
      <form action="/submit" method="post">
        <label for="nom">Nom :</label>
        <input type="text" id="nom" name="nom" required><br><br>

        <label for="email">Email :</label>
        <input type="email" id="email" name="email" required><br><br>

        <label for="message">Message :</label>
        
        <button type="submit">Envoyer</button>
      </form>
    </body>
    </html>
    '''

    return form_html

