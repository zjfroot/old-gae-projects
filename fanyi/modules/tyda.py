#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright Jifeng Zhang <zjfroot@gmail.com>.
#
#
import urllib2
import re
from types import *

from google.appengine.ext import webapp
from google.appengine.ext.webapp import util
from google.appengine.ext.webapp import template
from google.appengine.ext import db
from dbmodels import *

class TydaHandler(webapp.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        
        original_word = self.request.get('src')
        
        query = db.GqlQuery("SELECT * FROM Word where word = :1",original_word)
        
        word = query.get()
        
        en_words = ''
        if not isinstance(word.translation_tyda_en, NoneType):
            en_words = word.translation_tyda_en
            self.response.out.write(en_words)
        else:
            #url = "http://tyda.se/search?form=1&w=krasslig"
            url = "http://tyda.se/search/"+original_word.encode('utf-8')
            
            try:
                response = urllib2.urlopen(url)
                result = response.read()
                m = re.findall('a id="tyda_transR\d+" href="/search/\w+',result)
                words = ''
                for s in m:
                    word = s.split('"')[3].split('/')[2]
                    words = words + word +','
            
                #remove the last comma,
                words = words[:-1]
                
                self.response.out.write(words)
            except urllib2.URLError, e:
                self.response.out.write("error")
        
        