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

import logging
import webapp2
import rot13
import signup
import welcome

form = """
<form method="post">
    <select name="path">
        <option>rot13</option>
        <option>signup</option>
        <option>test</option>
    </select>
    <input type="submit">
</form>
"""


class MainHandler(webapp2.RequestHandler):
    def get(self):
        #self.response.headers['Content-Type'] = 'text/plain'
        self.response.out.write(form)
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
