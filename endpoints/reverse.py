import cherrypy
import json

class Reverse(object):
    @cherrypy.expose
    def index(self, string=''):
        cherrypy.response.headers['Content-Type'] = "application/json"
        return json.dumps({'result': string[::-1]})
