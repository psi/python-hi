import cherrypy
import re
import string

import endpoints

app = cherrypy.tree

app_config = {
    '/': {'tools.trailing_slash.on': False}
}

for m in endpoints.__all__:
    if m == 'root':
        endpoint_path = '/'
    else:
        endpoint_path = '/' + m

    endpoint_class = 'endpoints.' + m + '.' + string.capwords(m, '_') + '()'
    cherrypy.tree.mount(eval(endpoint_class), endpoint_path, config=app_config)

if __name__=='__main__':

    cherrypy.config.update({
        'server.socket_host': '127.0.0.1',
        'server.socket_port': 8080,
    })

    # Run the application using CherryPy's HTTP Web Server
    cherrypy.engine.start()
    cherrypy.engine.block()
