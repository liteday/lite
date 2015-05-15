'''
Created on May 15, 2015

@author: dragan
'''
from multiprocessing import Process, Queue
class Server(object):
    '''
    classdocs
    '''

    def kill_server(self, server):
        server.join()
    
    def f(self):
        print "process running", self.port
        while True:
            data = self.q.get()
            if data == 'remove':
                return 1
            else:
                print data

   
    def create_server(self, port):
        self.q = Queue()
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
        
