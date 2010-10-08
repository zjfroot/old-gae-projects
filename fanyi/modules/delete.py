#!/usr/bin/env python
#
# Copyright Jifeng Zhang.
#
#
from google.appengine.ext import webapp
from google.appengine.ext import db
from dbmodels import *

class DeleteWordHandler(webapp.RequestHandler):
    def post(self):
        word = self.request.get('word')
        print word
        words = db.GqlQuery("SELECT * FROM Word where word = :1",word)
        for w in words:
            w.delete()