from mako.template import Template
import cherrypy

from database import the_db
from controller import controller


class System(object):
    def __init__(self):
        self.db = the_db.TheSystemsDb()
        self.controller = controller.Coordinator()
        pass

    @cherrypy.expose
    def index(self):
        systems = self.db.get_all_systems()
        return Template(filename='index.tpl').render(systems=systems)

    @cherrypy.expose
    def check(self, system):
        if self.controller.check_system(system):
            return 'green'
        else:
            return 'red'

    @cherrypy.expose
    def deploy(self, system_name):
        system_servers = self.db.get_all_systems()[system_name]
        system = {'name': system_name, 'servers': [system_servers[server_name] for server_name in system_servers]}
        self.controller.deploy_system(system)
 dummy_data = {"name" :"ts1", "servers" : [ "localhost:2002" ] }