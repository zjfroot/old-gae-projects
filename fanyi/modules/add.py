#!/usr/bin/env python
#
# Copyright Jifeng Zhang <zjfroot@gmail.com>.
#
#
from google.appengine.ext import webapp
from google.appengine.ext.webapp import util
from google.appengine.ext.webapp import template
from google.appengine.ext import db
from dbmodels import *

class AddWordHandler(webapp.RequestHandler):
    def post(self):
        #if the word is never been translated before, save it in db
        new_word = self.request.get('src')
        words = db.GqlQuery("SELECT * FROM Word where word = :1",new_word)
        count = 0
        for w in words:
            count = count + 1
        
        if count < 1:
            word = Word()
            word.word = new_word
            word.translation_en = self.request.get('translation_en')
            word.translation_zh = self.request.get('translation_zh')
            word.put()
        
        #update the counter of how many times in total has been performed
        query = db.GqlQuery("SELECT * FROM Counter where name = :1",'translate_counter')
        counter = query.get()
        if hasattr(counter, 'count'):
            counter.count = counter.count + 1
        else:
            counter = Counter()
            counter.name = 'translate_counter'
            counter.count = 1
        counter.put()