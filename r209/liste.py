#!/usr/bin/python

import fonctions
from mod_python import Session, apache

def index(req):
    s = Session.Session(req)

    req.content_type = "text/html"

    html = fonctions.codeHTML("Liste des Contact","""<form method="get">
    <p><b>Liste des contacts</b></p>
    <span>Rechercher un nom: </span><input type="text" name="login" onkeyup=liste() id="text"/>
    <div id='div'></div>
    <a href="menu.py">Retour au menu</a>
    </form>
    
    <script>
    function liste(){
        req = new XMLHttpRequest(); 
        var text = document.getElementById("text").value;
        console.log(text)
        
        req.open('GET', 'affiche-liste.py?nom='+text, false);
        req.send();
        if (req.readyState == 4 && req.status == 200) {
            var div = document.getElementById("div");
            console.log("Request: "+req.responseText);
            div.innerHTML = req.responseText;
        }

    }
    </script>
    """) 
    req.write(html)



