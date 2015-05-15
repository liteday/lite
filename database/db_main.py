'''
Created on May 15, 2015

@author: peter.cautley
'''
from the_db import TheSystemsDb

if __name__ == '__main__':
    test_database = TheSystemsDb()
    test_database.create_tables()
    test_database.clear_tables()

    #test_database.load_systems({1:'val'})
    #test_database.load_systems(['sys1', 'sys2'])
    test_database.load_systems({'ts1' : { 'serv1':'localhost101', 
                                          'serv2':'localhost102' },
                                'ts2' : { 'serv3':'localhost101', 
                                          'serv4':'localhost102' },
                                'ts3' : { 'serv5':'localhost103', 
                                          'serv6':'localhost104' } 
                               })
    test_database.get_all_systems()

