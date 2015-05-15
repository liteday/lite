import VirtualCloud.system as system

class Coordinator(object):
    
    def __init__(self):
        self.systems = {}
    
    def check_system(self,sys_name):
        # validate ID?
        sys = self.systems[sys_name]
        return sys.check()        
    
    def deploy_system(self,config):
        sys = system.System(config["name"], config["servers"])
        for serv in sys.servers:
            sys.deploy(serv)
        self.systems[config["name"]] = sys
        return "Deploying"

    def end_system(self,sys):
        sys = self.systems[sys]
        servers = [ s for s in sys.servers.iteritems() ]
        print servers
        for serv in servers:
            print "Server for removal: ",serv
            sys.remove(serv[0])
        return True
            
if __name__ == '__main__':
    dummy_data = {"name" :"ts1",
                  "servers" : [ "localhost:2002" ] }
    # test methods here
    coord = Coordinator()
    coord.deploy_system(dummy_data)
    coord.check_system("ts1")
    coord.end_system("ts1")
