'''
Created on May 15, 2015

@author: dragan
'''
from server import Server

class System(object):
    '''
    classdocs
    '''

    def __init__(self, name, l):
        '''
        Constructor
        '''
        # System id
        # Number of Servers
        # Server Ids
        # list of Servers
        self.id = name
        self.servers = {}
        for serverId in l:
            s = Server(serverId)
            s.create_server(serverId)
            self.servers.update({serverId: s})
#        print self.servers
    
    def deploy(self,serverId):
        s = Server(serverId)
        s.create_server(serverId)
        self.servers.update({serverId: s})
    
    def check(self):
        for key,value in self.servers.iteritems():
            if value.p.is_alive() == False:
                print "server dead ", key
                return False
            print "server alive ", key
        return True

    def remove(self, serverId):
        # create
        # destroy
        value = self.servers.get(serverId)
        value.q.put('remove')
#        print value
        del self.servers[serverId]
        #print self.servers
        