#!/usr/bin/env python
#
# Copyright Jifeng Zhang <zjfroot@gmail.com>.
#
#
import os,sys

from google.appengine.ext import webapp
from google.appengine.ext.webapp import util
from google.appengine.ext.webapp import template
from google.appengine.api import users
from google.appengine.ext import db

sys.path.append('modules')
from add import AddNoteHandler

class MainHandler(webapp.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            if user.email() == "zjfroot@gmail.com":
                #get word list
                query = db.GqlQuery("SELECT * FROM Note ORDER BY created DESC LIMIT 20")
                notes = query.fetch(20)
                
                author = 'Jifeng Zhang'
                action = 'programming'
                template_values = {
                    'author':author,
                    'action':action,
                    'notes':notes,
                }
                path = os.path.join(os.path.dirname(__file__),'index.html')
                self.response.out.write(template.render(path,template_values))
            else:
                self.redirect(users.create_login_url(self.request.uri))
        else:
            self.redirect(users.create_login_url(self.request.uri))
    
        


def main():
    add_handler = AddNoteHandler()
    
    application = webapp.WSGIApplication([('/', MainHandler),
                                          ('/add', AddNoteHandler)],
                                         debug=True)
    util.run_wsgi_app(application)


if __name__ == '__main__':
    main()
