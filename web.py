# -*- coding: utf-8 -*-
import tornado
import tornado.web
import os
from settings import settings
from handler import index


class SevenStarTornado(tornado.web.Application):
    def __init__(self):
        tornado.web.Application.__init__(self, urls, **settings)


urls = [
        (r'/', index.IndexHandler),
        (r'/static/(.*)', tornado.web.StaticFileHandler, dict(path=settings['static_path'])),
        (r'/favicon.ico', tornado.web.StaticFileHandler, dict(path=settings['favicon_path'])),
]



if __name__ == "__main__":
    import tornado.ioloop
    import tornado.httpserver
    import tornado.options
    from tornado.options import define,options
    app = SevenStarTornado()
    options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(app)
    #http_server = tornado.httpserver.HTTPServer(app, ssl_options={
    #       "certfile": os.path.join(os.path.abspath("."), "server.crt"),
    #       "keyfile": os.path.join(os.path.abspath("."), "server.key"),
    #})
    http_server.listen(settings["port"])
    print 'Development server is running at http://0.0.0.0:%s/' % (settings["port"])
    print 'Quit the server with Control-C'
    tornado.ioloop.IOLoop.instance().start()