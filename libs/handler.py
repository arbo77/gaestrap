#!/usr/bin/env python
#
# Copyright 2012 Solusisoho.
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
from webapp2_extras import sessions
from google.appengine.ext.webapp import template
from libs import dicts

config = {}

config['webapp2_extras.sessions'] = {
	'cookie_name'	: 'agendamusik-token',
    'secret_key'	: 'e23e6286ba3fa450d65e779a35086736',
}

class SessionHandler(webapp2.RequestHandler):
	token = None

	def dispatch(self):
		self.session_store = sessions.get_store(request=self.request)
		try:
			webapp2.RequestHandler.dispatch(self)
		finally:
			self.session_store.save_sessions(self.response)

	@webapp2.cached_property
	def session(self):
		return self.session_store.get_session()
		

class BaseHandler(SessionHandler):
	def show_page(self):
		dicts.page["page"]["title"] = "Hello, world!"
		html = template.render("tpl/index.html",dicts.page)
		self.response.write(html)
