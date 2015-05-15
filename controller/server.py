'''
Created on May 15, 2015

@author: dragan
'''
from multiprocessing import Process, Pipe
class Server(object):
    '''
    classdocs
    '''

    def kill_server(self, server):
        server.join()
    
    def f(self):
        print "process running", self.port
        while True:
            data = self.b.recv()
            if data == 'remove':
                self.b.send('removed')
                return 1
            else:
                self.b.send(data)
                print data

   
    def create_server(self, port):
        self.a,self.b = Pipe()
        self.port = port
        self.p = Process(target=self.f)
        self.p.start()
#        return self.p,self.q

    def __init__(self, params):
        '''
        Constructor
        '''
        self.server_name = params
#        print self.server_name
        
