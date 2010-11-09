#!/usr/bin/env python
#
# Copyright Jifeng Zhang <zjfroot@gmail.com>.
#
#
import urllib2
import re
from google.appengine.ext import webapp
from google.appengine.ext.webapp import util
from google.appengine.ext.webapp import template
from google.appengine.ext import db
from dbmodels import *

class TydaHandler(webapp.RequestHandler):
    def get(self):
        original_word = self.request.get('src')
        #url = "http://tyda.se/search?form=1&w=krasslig"
        url = "http://tyda.se/search/"+original_word
        
        self.response.headers['Content-Type'] = 'text/plain'
        try:
            response = urllib2.urlopen(url)
            result = response.read()
            m = re.findall('a id="tyda_transR\d+" href="/search/\w+',result)
            words = []
            for s in m:
                word = s.split('"')[3].split('/')[2]
                words.append(word)
            
            self.response.out.write(words)
        except urllib2.URLError, e:
            self.response.out.write("error")
        
        