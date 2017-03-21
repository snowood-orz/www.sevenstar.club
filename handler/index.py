import tornado.web
import tornado.websocket
from settings import settings
import json
import yaml
import os.path

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        staff_data = yaml.load(open(os.path.join(settings['data_path'], "staff.yaml"), "r"))
        outsite_data = yaml.load(open(os.path.join(settings['data_path'], "outsite.yaml"), "r"))
        self.render("index.html", 
                    staffs=staff_data['staffs'],
                    outsites=outsite_data['outsites']
        )