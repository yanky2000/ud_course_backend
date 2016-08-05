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
# distributed under the  is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import os
import jinja2
import encrypt

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir),
                                autoescape = True)

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
        self.redirect("/rot13")

class Rot13Handler(Handler):
    def get(self):
        self.render("rot13.html", is_encrypted=False)

    def post(self):
        # Collect data before start doing anything
        user_text = self.request.get('text')
        is_encrypted = self.request.get('is_encrypted')
        output_text = ""
        d = encrypt.Rot13()

        # First we check if user wants to encrypt or decrypt the text
        if is_encrypted:
            dic = d.encrypted_dic()
        else:
            dic = d.decrypted_dic()
        is_encrypted = not is_encrypted


        # Now we start changing letters in text one-by-one
        for char in user_text:

            # Some adjustments to preserve letter case    
            is_capitalized = False
            if char.isupper():
                is_capitalized = True
                char = char.lower()
            
            # We also skip non-in-the-range characters  
            subst = dic.get(char)
            if subst:
                char = subst
            
            if is_capitalized:
                char = char.upper()
            
            # Finally glue up the resulting text 
            output_text += char
            
        # Start rendering the page with new values
        self.render("rot13.html", text = output_text, user_text = user_text, is_encrypted = is_encrypted)


app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/rot13', Rot13Handler),


], debug=True)
