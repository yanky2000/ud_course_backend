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
<form method='post'>
    <h1> What is your birhtday?</h1>
    <label>
        Day
        <input type="text" name="day" value='%(day)s'>
    </label>
    <label>
        Month
        <input type="text" name="month" value="%(month)s">
    </label>
    <label>
        Year
        <input type="text" name="year" value="%(year)s">
    </label>
    <div style="color:red">
        %(error)s
    </div>
    <br>
    <input type="submit">
</form>
"""

months = ['January',
          'February',
          'March',
          'April',
          'May',
          'June',
          'July',
          'August',
          'September',
          'October',
          'November',
          'December']
          
months_abbr = dict((m[:3].lower(), m) for m in months)

def valid_month(month):
    if month:
        short_month = month[:3].lower() #if first 3 correct the user is on the right track
        return months_abbr.get(short_month)

def valid_day(day):
    if day and day.isdigit(): #First check if day consists of digits only
        day = int(day)
        if 0 < day <= 31:
            return day

def valid_year(year):
    if year and year.isdigit(): #First check if year consists of digits only
        year = int(year)
        if 1900 < year <= 2016:
            return year

import cgi
def escape_html(s):
    return cgi.escape(s, quote = True) # html escaping
    
class MainHandler(webapp2.RequestHandler):

    def write_form(self, error="", day="", month="", year=""):
        params = {
            "error": error, 
            "day": escape_html(day),
            "month": escape_html(month),
            "year": escape_html(year),
            }
        return self.response.out.write(form % params)


    def get(self):
        # self.response.headers['Content-type']='text/html'
        self.write_form()

    def post(self):
       
        user_day = self.request.get('day')
        user_month = self.request.get('month')
        user_year = self.request.get('year')

        day = valid_day(user_day)
        month = valid_month(user_month)
        year = valid_year(user_year)

        if not (day and month and year):
            self.write_form("Looks like you entered not a valid date", user_day, user_month, user_year)
        else: 
            self.redirect("/thanks")

class TestHandler(webapp2.RequestHandler):
    def get(self):
        q=self.request.get("q")
        self.response.write(q)
        # self.response.headers['Content-type']='text/plain'
        # self.response.write(self.request)

class ThanksHandler(webapp2.RequestHandler):
    def get(self):
        self.response.out.write("You have been redirected here. Date is perfectly valid!")

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/thanks', ThanksHandler),
    # ('/testform', TestHandler)


], debug=True)
