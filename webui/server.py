import sys
import os

base_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(base_dir, '..'))

import cherrypy
import lite

system = lite.System()

cherrypy.tree.mount(system, '/')
cherrypy.engine.start()
cherrypy.engine.block()
