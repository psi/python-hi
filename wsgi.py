import cherrypy

from app.root import Root
from app.echo import Echo

app = cherrypy.tree

app_config = {
    '/': {'tools.trailing_slash.on': False}
}

cherrypy.tree.mount(Root(), '/',     config=app_config)
cherrypy.tree.mount(Echo(), '/echo', config=app_config)

if __name__=='__main__':

    cherrypy.config.update({
        'server.socket_host': '127.0.0.1',
        'server.socket_port': 8080,
    })

    # Run the application using CherryPy's HTTP Web Server
    cherrypy.engine.start()
    cherrypy.engine.block()
