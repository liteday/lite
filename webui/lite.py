from mako.template import Template
import cherrypy

from database import the_db
from controller import controller


class System(object):
    def __init__(self):
        self.controller = controller.Coordinator()
        pass

    @cherrypy.expose
    def index(self):
        db = the_db.TheSystemsDb()
        systems = db.get_all_systems()
        print systems
        return Template(filename='index.tpl').render(systems=systems)

    @cherrypy.expose
    def check(self, system, server):
        print system, server
        return 'green' if self.controller.check_system(system, server) else 'red'

    @cherrypy.expose
    def deploy(self, system_name):
        db = the_db.TheSystemsDb()
        system_servers = db.get_all_systems()[system_name]
        system = {'name': system_name, 'servers': [system_servers[server_name] for server_name in system_servers]}
        self.controller.deploy_system(system)
