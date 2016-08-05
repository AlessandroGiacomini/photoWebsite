import os
import webapp2
import jinja2
from google.appengine.ext import db

jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader('templates'),
                               autoescape = True)

loader=jinja2.FileSystemLoader('templates')

class Handler(webapp2.RequestHandler):
    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        self.write(self.render_str(template, **kw))

class MainPage(Handler):
    def get(self):
        self.render("index.html")

app = webapp2.WSGIApplication([('/', MainPage),
                               ],
                              debug=True)




