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

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir))

def valid_subject(subject):
    return subject

def valid_blog(blog):
    return blog

class Handler(webapp2.RequestHandler):
    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)
    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)
    def render(self, template, **kw):
        self.write(self.render_str(template, **kw))

class BlogHandler(Handler):
    def get(self):
        self.render("blog_index.html")
    def post(self):
        self.render("blog_index.html")

class NewPostHandler(Handler):
    def get(self):
        self.render("blog_newpost.html")
    def post(self):
        subject = self.request.get("subject")
        blog = self.request.get("blog")

        error_msg = ""
        error_flag = False

        if not valid_subject(subject) or not valid_blog(blog):
            error_msg = "subject and blog, please!"
            error_flag = True

        if error_flag:
            self.render("blog_newpost.html", error_msg=error_msg)
        else:
            #need to update the content of the post
            self.render("blog_posting_succeed.html", msg="succeed")
