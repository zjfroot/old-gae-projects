#!/usr/bin/env python
#
# Copyright Jifeng Zhang.
#
#
import os,sys

from google.appengine.ext import webapp
from google.appengine.ext.webapp import util
from google.appengine.ext.webapp import template
sys.path.append('modules')
from add import AddWordHandler
from list import ListWordsHandler

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
    #need to study more python object knowledge. if follwing two lines are removed, we get
    #strange errors
    list_handler = ListWordsHandler()
    add_handler = AddWordHandler()
    application = webapp.WSGIApplication([('/', MainHandler),
                                          ('/add', AddWordHandler),
                                          ('/list', ListWordsHandler)],
                                         debug=True)
    util.run_wsgi_app(application)


if __name__ == '__main__':
    main()
