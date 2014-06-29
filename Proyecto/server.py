from pyramid.paster import get_app
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.options import options, define, parse_command_line
from tornado.wsgi import WSGIContainer

define('port', type= int, default=8080)

if __name__ == "__main__":
	parse_command_line()
	app = get_app('development.ini')
	container = WSGIContainer(app)
	http_server = HTTPServer(container)
	http_server.listen(options.port)
	IOLoop.instance().start()


