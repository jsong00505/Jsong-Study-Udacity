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
import string

rot13Form = """
<!DOCTYPE html>

<html>
  <head>
    <title>Unit 2 Rot 13</title>
  </head>

  <body>
    <h2>Enter some text to ROT13:</h2>
    <form method="post">
      <textarea name="text"
                style="height: 100px; width: 400px;">%s</textarea>
      <br>
      <input type="submit">
    </form>
  </body>

</html>
"""

def doRot13(text):
	lowerCase = string.lowercase
	upperCase = string.uppercase
	result = []
	for s in text:
		if lowerCase.find(s) > -1:
			index = lowerCase.find(s)
			new_index = (index + 13) % 26
			new_s = lowerCase[new_index]
			result.append(new_s)
		elif upperCase.find(s) > -1:
			index = upperCase.find(s)
			new_index = (index + 13) % 26
			new_s = upperCase[new_index]
			result.append(new_s)
		else:
			result.append(s)
	return ''.join(result)
	
class Rot13Handler(webapp2.RequestHandler):
	def get(self):
		#self.response.headers['Content-Type'] = 'text/plain'
		self.response.out.write(rot13Form % "")
	def post(self):
		text=self.request.get("text")
		text=doRot13(text)
		self.response.out.write(rot13Form % text)
