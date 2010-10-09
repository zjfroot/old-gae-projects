#!/usr/bin/env python
#
# Copyright Jifeng Zhang.
#
#
import logging

from google.appengine.ext import webapp
from google.appengine.ext import db
from dbmodels import *

class DeleteWordHandler(webapp.RequestHandler):
    def post(self):
        key = self.request.get('key')
        logging.debug('Trying to delete entity with key = '+key)
        obj = db.get(db.Key(key))
        obj.delete()