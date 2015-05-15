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
        '''  Constructor  '''
        self.id = name
        self.servers = {}
        for serverId in l:
            s = Server(serverId)
            s.create_server(serverId)
            self.servers.update({serverId: s})
    
    def deploy(self,serverId):
        s = Server(serverId)
        s.create_server(serverId)
        self.servers.update({serverId: s})
    
    def remove(self, serverId):
        value = self.servers.get(serverId)
        value.a.send('remove')
        if value.a.recv() != 'removed':
            print 'not removed'
            return None
        del self.servers[serverId]

    def check(self):
        for key,value in self.servers.iteritems():
            if value.p.is_alive() == False:
                print "server dead ", key
                return False
            print "server alive ", key
        return True

    def echo_command(self, serverId, l):
        value = self.servers.get(serverId)
        value.a.send(l)
        d = value.a.recv()
        print d
        return d
        
