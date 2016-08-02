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
import validate

form="""
<form>
    <label>
        One
        <input type="radio" name="q" value="one">
    </label>
    <label>
        Two
        <input type="radio" name="q" value="two">
    </label>
    <label>
        Three
        <input type="radio" name="q" value="three">
    </label>
</form>

<form>
    <select name="z">
        <option value="1">One</option>
        <option value="2">Two, digit 2 will appear in URL</option>
        <option>Three will appear in URL, as it has no value parameter</option>
    </select>

</form>
<form method='post'>
    <label>
        Day
        <input type="text" name="day">
    </label>
    <label>
        Month
        <input type="text" name="month">
    </label>
    <label>
        Year
        <input type="text" name="year">
    </label>
    <br>
    <input type="submit">
</form>
"""

class MainHandler(webapp2.RequestHandler):
    def get(self):
        # self.response.headers['Content-type']='text/html'
        self.response.write(form)
    def post(self):
        day = validate.valid_day(self.request.get(day))
        month = validate.valid_month(self.request.get(month))
        year = validate.valid_year(self.request.get(year))
        if not (day and month and year):    
            self.response.out.write(form)
        else: 
            self.response.out.write("Thanks! Thats a totally valid date!")


class TestHandler(webapp2.RequestHandler):
    def get(self):
        q=self.request.get("q")
        self.response.write(q)
        # self.response.headers['Content-type']='text/plain'
        # self.response.write(self.request)

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/testform', TestHandler)


], debug=True)
