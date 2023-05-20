#!/usr/bin/python
# -*- coding: utf-8 -*-

from mod_python import apache
from fonctions import codeHTML
def index(req):
    html = codeHTML("Mon premier script", "Voici mon premier script")
    req.content_type="text/html"
    
    return html
