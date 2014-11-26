import cherrypy

from app.root import Root
from app.echo import Echo

app = cherrypy.tree

cherrypy.tree.mount(Root(), '/')
cherrypy.tree.mount(Echo(), '/echo')

if __name__=='__main__':

    cherrypy.config.update({
        'server.socket_host': '127.0.0.1',
        'server.socket_port': 8080,
    })

    # Run the application using CherryPy's HTTP Web Server
    cherrypy.engine.start()
    cherrypy.engine.block()
