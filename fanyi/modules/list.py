#!/usr/bin/env python
#
# Copyright Jifeng Zhang.
#
#
import os

from google.appengine.ext import webapp
from google.appengine.ext.webapp import util
from google.appengine.ext.webapp import template
from google.appengine.ext import db

class ListWordsHandler(webapp.RequestHandler):
    def get(self):
        #get word list
        query = db.GqlQuery("SELECT * FROM Word ORDER BY created DESC LIMIT 50")
        words = query.fetch(50)
        
        #get counter
        query = db.GqlQuery("SELECT * FROM Counter where name = :1",'translate_counter')
        counter = query.get()
        count = 0;
        if hasattr(counter, 'count'):
            count = counter.count

            
        template_values = {
            'words':words,
            'count':count,
        }
        path = os.path.join(os.path.dirname(__file__),'list.html')
        self.response.out.write(template.render(path,template_values))