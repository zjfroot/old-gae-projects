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
        #url = "http://tyda.se/search?form=1&w=krasslig"
        url = "http://tyda.se/search/krasslig"
        
        self.response.headers['Content-Type'] = 'text/plain'
        try:
            response = urllib2.urlopen(url)
            result = response.read()
            p = re.compile('.*<a id="tyda_transR\d.* href="/search/.*')
            m = p.match(result)
            
            self.response.out.write(m.group(0))
        except urllib2.URLError, e:
            self.response.out.write("error")
        
        