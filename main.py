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

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir))

html_form = """
<h2> Enter your food </h2>
<form>
    <input type="text" name="food">
    <input type="hidden" name="food" value="eggs">
    <button>Add</button>
</form>
"""

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
        n = self.request.get('n')
        # if n.isdigit():
        if n:
            n = int(n)
        # else:
        #     n =0
        self.render("shopping_list.html", n=n)

app = webapp2.WSGIApplication([
    ('/', MainPage),
    # ('/thanks', ThanksHandler),
    # ('/testform', TestHandler)


], debug=True)
