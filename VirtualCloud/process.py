'''
Created on May 15, 2015

@author: dragan
'''

from multiprocessing import Process, Queue

def f(q, i):
    q.put([42, None, 'hello'])
#    q.put([42, None, 'hello'])
    print i

if __name__ == '__main__':
    q1 = Queue()
    q2 = Queue()
    q3 = Queue()
    ip = (127,0,0,1)
    port = (8008,8009,8010)
    
    p1 = Process(target=f, args=(q1,ip, port[0]))
    p2 = Process(target=f, args=(q2,ip))
    p3 = Process(target=f, args=(q3,ip))

    p1.start()
    p2.start()
    p3.start()
#     print q1.get()    # prints "[42, None, 'hello']"
#     print q2.get()    # prints "[42, None, 'hello']"
#     print q3.get()    # prints "[42, None, 'hello']"
    p1.join()
    p2.join()
    p3.join()

