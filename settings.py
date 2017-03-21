import os
import logging

settings = {
    "debug": logging.DEBUG,
    "template_path": os.path.join(os.path.dirname(__file__), "template"),
    "static_path": os.path.join(os.path.dirname(__file__), "static"),
    "favicon_path": os.path.join(os.path.dirname(__file__), "static"),
    "data_path": os.path.join(os.path.dirname(__file__), "data"),
    "static_url_prefix": "/static/",
    "port": 8000,
    "cookie_secret": "sevenstar"
}