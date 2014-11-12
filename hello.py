import cherrypy
import json

class Root(object):
    @cherrypy.expose
    def index(self):
        return '<div>Call /hello, /echo or /reverse</div>'

class Hello(object):
    @cherrypy.expose
    def index(self):
        return json.dumps({'result': 'hi'})

class Echo(object):
    @cherrypy.expose
    def index(self, string=''):
        return json.dumps({'result': string})

class Reverse(object):
    @cherrypy.expose
    def index(self, string=''):
        return json.dumps({'result': string[::-1]})

if __name__ == '__main__':
    app_config = {
        '/': {'tools.trailing_slash.on': False}
    }

    cherrypy.config.update({
        'server.socket_host': '0.0.0.0',
        'server.socket_port': 8080
    })

    cherrypy.tree.mount(Root(),    '/',        config=app_config)
    cherrypy.tree.mount(Hello(),   '/hello',   config=app_config)
    cherrypy.tree.mount(Echo(),    '/echo',    config=app_config)
    cherrypy.tree.mount(Reverse(), '/reverse', config=app_config)

    cherrypy.engine.start()
    cherrypy.engine.block()
