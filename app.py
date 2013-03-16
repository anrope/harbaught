#!/usr/bin/env python
"""
Harbaught APP
"""
import os
import sys

import tornado.httpserver
import tornado.ioloop
import tornado.web
import tornado.wsgi

from optparse import OptionParser

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('templates/harbot.html')


url_mapping = [
    (r'/.*', MainHandler),
]



app_settings = {
    "cookie_secret": "this_is_a_secret_cookie",
    "debug": False,
    "static_path": os.path.join(os.path.dirname(__file__), "static"),
    "autoescape": None,
}

if __name__ == "__main__":

    parser = OptionParser(usage="usage: %prog [options]",
                          version="%prog 1.0")
    parser.add_option("-p", "--port",
                      action="store",
                      dest="port",
                      default="8000",
                      help="Port To Run",)
    (options, args) = parser.parse_args()

    application = tornado.web.Application(url_mapping, **app_settings)
    http_server = tornado.httpserver.HTTPServer(application, xheaders=True)
    http_server.listen(int(options.port))
    tornado.ioloop.IOLoop.instance().start()