#!/usr/bin/env python
#
# Copyright Jifeng Zhang <zjfroot@gmail.com>.
#
#
import os,sys
import logging

from google.appengine.ext import webapp
from google.appengine.ext.webapp import util
from google.appengine.ext.webapp import template
sys.path.append('modules')
from add import AddWordHandler
from list import *
from delete import DeleteWordHandler

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

def main():
    logging.getLogger().setLevel(logging.DEBUG)
    #need to study more python object knowledge. if follwing two lines are removed, we get
    #strange errors
    list_handler = ListRecentWordsHandler()
    review_handler = ListWordsToReviewHandler()
    add_handler = AddWordHandler()
    delete_handler = DeleteWordHandler()
    application = webapp.WSGIApplication([('/', MainHandler),
                                          ('/add', AddWordHandler),
                                          ('/list', ListRecentWordsHandler),
                                          ('/delete', DeleteWordHandler),
                                          ('/review', ListWordsToReviewHandler)],
                                          debug=True)
    util.run_wsgi_app(application)


if __name__ == '__main__':
    main()