#!/usr/bin/env python
#
# Copyright Jifeng Zhang <zjfroot@gmail.com>.
#
#
import os,random
from datetime import datetime

from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from google.appengine.ext import db
from google.appengine.api import memcache

class RandomWordsHandler(webapp.RequestHandler):
    def get(self):
        key = 'wordList'
        wordList = memcache.get(key)
        
        #If words lists is not in memcache, then get it from db
        if wordList is None:
            query = db.GqlQuery("SELECT * FROM Word ORDER BY created DESC LIMIT 1500")
            wordList = query.fetch(1500)
            memcache.add(key,wordList,360000)
            
        count = len(wordList)
        
        if count > 0:
            #get a random word from the word list
            index = random.randrange(0,count,1)
            word = wordList[index]
        else:
            word = 'Word not found'
        
        template_values = {
            'word':word,
        }
        path = os.path.join(os.path.dirname(__file__),'random.html')
        self.response.out.write(template.render(path,template_values))