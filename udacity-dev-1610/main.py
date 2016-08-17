#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import os
import logging
import webapp2
import jinja2

import rot13
import signup
import welcome

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir))

class Handler(webapp2.RequestHandler):
    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)
    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)
    def render(self, template, **kw):
        self.write(self.render_str(template, **kw))

class MainHandler(Handler):
    def get(self):
        #self.response.headers['Content-Type'] = 'text/plain'
        self.render("navigation.html")
    def post(self):
        path=self.request.get("path")
        if path == "rot13":
            self.redirect("/unit2/rot13")
        elif path == "signup":
            self.redirect("/unit2/signup")
        else:
            self.redirect("/testform")


class TestHandler(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.out.write(self.request)
        #q=self.request.get("q")
		#self.response.out.write(q)


		
app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/testform', TestHandler),
	('/unit2/rot13', rot13.Rot13Handler),
    ('/unit2/signup', signup.SignupHandler),
    ('/unit2/welcome', welcome.WelcomeHandler)
], debug=True)
