import cherrypy
import lite

system = lite.System()

cherrypy.tree.mount(system, '/')
cherrypy.engine.start()
cherrypy.engine.block()
