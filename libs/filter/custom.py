#!/usr/bin/env python
#
# filter
# author: @arbo77
# date: 2013/01/21

# django custom filter

import random
from google.appengine.ext.webapp import template
from libs import dicts

register = template.create_template_register()


# sample register filter 
@register.filter('hello')
def hello(val):
	return "Hello, world"
