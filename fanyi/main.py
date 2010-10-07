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

class Word(db.Model):
    word = db.StringProperty();
    translation = db.StringProperty();
    created = db.DateTimeProperty(auto_now_add=True);

class MainHandler(webapp.RequestHandler):
    def get(self):
        author = 'Jifeng Zhang'
        action = 'programming'
        template_values = {
            'author':author,
            'action':action,
        }
        path = os.path.join(os.path.dirname(__file__),'index.html')
        self.response.out.write(template.render(path,template_values))
        
        
class AddWordHandler(webapp.RequestHandler):
    def post(self):
        new_word = self.request.get('src')
        words = db.GqlQuery("SELECT * FROM Word where word = :1",new_word)
        count = 0
        for w in words:
            count = count + 1
        
        if count < 1:
            word = Word()
            word.word = new_word
            word.translation = self.request.get('translation')
            word.put()
            
class ListWordsHandler(webapp.RequestHandler):
    def get(self):
        words = db.GqlQuery("SELECT * FROM Word ORDER BY created DESC LIMIT 10")
        for word in words:
            self.response.out.write(word.word+'<br />');


def main():
    application = webapp.WSGIApplication([('/', MainHandler),
                                          ('/add', AddWordHandler),
                                          ('/list', ListWordsHandler)],
                                         debug=True)
    util.run_wsgi_app(application)


if __name__ == '__main__':
    main()
