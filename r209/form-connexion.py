#!/usr/bin/env python
# -*- coding: utf-8 -*-

# form-connexion.py

def index(req):
    req.content_type = "text/html"
    form_html = '''
    <form action="connexion.py" method="post">
        <label for="login">Login:</label>
        <input type="text" id="login" name="login"><br><br>
        <label for="password">Password:</label>
        <input type="password" id="password" name="password"><br><br>
        <input type="submit" value="Submit">
    </form>
    '''
    return form_html
