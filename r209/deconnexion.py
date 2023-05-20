#!/usr/bin/env python
# -*- coding: utf-8 -*-

from mod_python import Session
from mod_python import util

def index(req):
    req.content_type="text/html"
    session = Session.Session(req)
    session.delete()
    util.redirect(req, "./form-connexion.py")
    
