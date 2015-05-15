from mako.template import Template
import cherrypy

import database
import coordinator


class System(object):
    def __init__(self):
        pass

    @cherrypy.expose
    def index(self):
        systems = database.list_all_systems()
        return Template(filename='index.tpl').render(systems=systems)

    @cherrypy.expose
    def check(self, system):
        system_data = database.get_system_by_name(system)
        if coordinator.check(system_data):
            return 'green'
        else:
            return 'red'

    @cherrypy.expose
    def deploy(self, system):
        system_data = database.get_system_by_name(system)
        coordinator.deploy(system_data)
        raise cherrypy.HTTPRedirect("/")
