#!/usr/bin/env python
# -*- coding: utf-8 -*-
from sys import exit
from pyramid.paster import get_app
from tornado.autoreload import add_reload_hook, start
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.options import options, define, parse_command_line
from tornado.wsgi import WSGIContainer

__autor__ = "William Mendez"
__version__ = "0.006"

define('port', type= int, default=8080)

server = u"El servidor de desarrollo está iniciando en la url http://127.0.0.1: " + str(options.port)

def auto_reload_hook():
    print  server

if __name__ == "__main__":
	parse_command_line()
	app = get_app('development.ini')
	container = WSGIContainer(app)
	http_server = HTTPServer(container)
	http_server.listen(options.port)
	add_reload_hook(auto_reload_hook)
    start()
    print server
    try:
        IOLoop.instance().start()
    except KeyboardInterrupt:
        print ""
        print "Saliendo"
        exit(0)
