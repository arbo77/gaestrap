#!/usr/bin/env python
#
# development application handler
# author: @arbo77
# date: 2013/01/21

import webapp2
from google.appengine.ext.webapp import template
from libs import dicts
from libs import handler

template.register_template_library('libs.filter.custom')

class HomeHandler(handler.BaseHandler):
	def get(self):
		self.show_page()
	
	def post(self):
		self.show_page()
		

app = webapp2.WSGIApplication([
        ('/', HomeHandler)
			],
      debug=True,
      config=handler.config)

