import cherrypy

class Root(object):
    @cherrypy.expose
    def index(self):
        return '<div>Call /hello, /echo or /reverse</div>'
