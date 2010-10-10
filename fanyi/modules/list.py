#!/usr/bin/env python
#
# Copyright Jifeng Zhang <zjfroot@gmail.com>.
#
#
import os
from datetime import datetime

from google.appengine.ext import webapp
from google.appengine.ext.webapp import util
from google.appengine.ext.webapp import template
from google.appengine.ext import db

class ListRecentWordsHandler(webapp.RequestHandler):
    def get(self):
        #get word list
        query = db.GqlQuery("SELECT * FROM Word ORDER BY created DESC LIMIT 100")
        words = query.fetch(100)
        
        #Reset counts
        #for w in words:
        #    w.reviewed_times = 0
        #    w.put()
        
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
        
        
class ListWordsToReviewHandler(webapp.RequestHandler):
    def get(self):
        query = db.GqlQuery("SELECT * FROM Word ORDER BY reviewed_times ASC, created DESC, last_reviewed ASC LIMIT 10")
        words = query.fetch(10)
        
        for w in words:
            w.reviewed_times = w.reviewed_times + 1
            w.last_reviewed = datetime.utcnow()
            w.put()
        
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