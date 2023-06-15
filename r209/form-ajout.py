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
    
      <form action="ajout.py" method="post" id="monform">
        <label for="nom">Nom :</label>
        <input type="text" id="nom" name="nom" required><br><br>

        <label for="email">Email :</label>
        <input type="email" id="email" name="email" required><br><br>

        <label for="tel">telephone :</label>
        <input type="text" id="tel" name="tel"><br><br>

        <label for="adresse">Adresse :</label>
        <input type="text" id="adresse" name="adresse"><br><br>
        
        
        <button type="submit">S'enregistrer</button><br>
        <span id="error"></span>
      </form>
    <script>
    document.getElementById('monform').addEventListener('submit', function checkForm(event){
        // Empêcher l'envoi du formulaire par défaut
        event.preventDefault();
    
        // Tester le nom
        var nom = document.getElementById("nom");
        if (nom.value === "") {
            alert("Veuillez renseigner le nom");
            return false;
        }

        // Tester l'adresse email
        var email = document.getElementById("email");
        var emailRegex = /^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$/;
        if (email.value !== "" && !emailRegex.test(email.value)) {
            alert("Veuillez renseigner une adresse email valide");
            return false;
        }

        // Tester le numéro de téléphone
        var num = document.getElementById("tel");
        if (num.value.length !== 10 || isNaN(num.value)) {
            alert("Veuillez renseigner un numéro de téléphone valide");
            return false;
        }
    
        // Soumettre le formulaire si toutes les validations sont réussies
        document.getElementById('monform').submit();
    });
    </script>
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
