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


# 4. make dict of (position: character) dict of user_text

# 5. loop over user_text_dict and replace with encr character.

# 6. Glue up text by char positions

import webapp2
import os
import jinja2
import encrypt

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir),

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
        self.render("rot13.html")

    def post(self):
        user_text = self.request.get('text')
        input_text = user_text

        # creates a list of characters in text, skips others than a-z
        user_char_list = [t for t in enumerate(input_text)]

        # encripts user text with rot13 by replacing characters

        def encript(some_text, char_list):
            for i in char_list:
                # if i in char_list: # assuming char_list contains only a-z 
                new_char = encript_rot13(i)
                some_text = some_text.replace(i, new_char)
            return some_text
            
        user_text = self.request.get('text')
        
        input_text = user_text
        input_char_list = make_char_list(input_text)
        output_text = encript(input_text, input_char_list)     
      
        self.render("rot13.html", text = output_text, char_list=input_char_list, user_text=user_text)


app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/rot13', Rot13Handler),


], debug=True)
