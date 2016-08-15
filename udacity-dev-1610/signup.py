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
import webapp2
import re

signupForm = """
<!DOCTYPE html>
<html>
  <head>
    <title>Sign Up</title>
    <style type="text/css">
      .label {text-align: right}
      .error {color: red}
    </style>
  </head>
  <body>
    <h2>Signup</h2>
    <form method="post">
      <table>
        <tr>
          <td class="label">
            Username
          </td>
          <td>
            <input type="text" name="username" value="">
          </td>
          <td class="error">
            %(error_username)s
          </td>
        </tr>
        <tr>
          <td class="label">
            Password
          </td>
          <td>
            <input type="password" name="password" value="">
          </td>
          <td class="error">
            %(error_password)s
          </td>
        </tr>
        <tr>
          <td class="label">
            Verify Password
          </td>
          <td>
            <input type="password" name="verify" value="">
          </td>
          <td class="error">
            %(error_verify)s
          </td>
        </tr>
        <tr>
          <td class="label">
            Email (optional)
          </td>
          <td>
            <input type="text" name="email" value="">
          </td>
          <td class="error">
            %(error_email)s
          </td>
        </tr>
      </table>
      <input type="submit">
    </form>
  </body>
</html>
"""



USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
PASSWORD_RE = re.compile(r"^.{3,20}$")
EMAIL_RE = re.compile(r"^[\S]+@[\S]+.[\S]+$")

def valid_username(username):
    return username and USER_RE.match(username)

def valid_password(password):
    return password and PASSWORD_RE.match(password)

def valid_email(email):
    return email or EMAIL_RE.match(email)

class SignupHandler(webapp2.RequestHandler):
    def get(self):
        #self.response.headers['Content-Type'] = 'text/plain'
        self.response.out.write(signupForm % {"error_username": "",
                                              "error_password":"",
                                              "error_verify":"",
                                              "error_email":""})
    def post(self):
        username = self.request.get("username")
        password = self.request.get("password")
        verify = self.request.get("verify")
        email = self.request.get("email")

        error_username = ""
        error_password = ""
        error_verify = ""
        error_email = ""
        error_flag = False
        if not valid_username(username):
            error_username = "That's not a valid username."
            error_flag = True
        if not valid_password(password):
            error_password = "That wasn't a valid password."
            error_flag = True
        elif password != verify:
            error_verify = "Your passwords didn't match."
            error_flag = True
        if valid_email(email):
            error_email = "That's not a valid email."
            error_flag = True

        if error_flag == True:
            self.response.out.write(signupForm % {"error_username": error_username,
                                                  "error_password":error_password,
                                                  "error_verify":error_verify,
                                                  "error_email":error_email})
        else:
            self.redirect("/unit2/welcome?username="+username)
