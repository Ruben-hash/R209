#!/usr/bin/python
# -*- coding: utf-8 -*-

import urllib
import urllib2
from xml.dom import minidom

def geocodage(adresse):
    try:
        url = "http://nominatim.openstreetmap.org/search?format=xml&q=" + \
              urllib.quote_plus(adresse)
        reponse = urllib2.urlopen(url)
        xml = reponse.read()
        doc = minidom.parseString(xml)
        place = doc.getElementsByTagName("place")[0]
        lat = place.attributes["lat"].value
        lon = place.attributes["lon"].value
        return lat, lon
    except:
        return None
    
#  fonction de test (ne pas utiliser dans votre code)
def index(req):
    req.content_type = "text/html"
    pos = geocodage(req.form["adresse"])
    if pos == None:
        req.write("Adresse non trouvée")
    else:
        lat, lon = pos
        req.write("Latitude = " + str(lat) + ", Longitude = " + str(lon))
