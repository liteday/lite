'''
Created on May 15, 2015

@author: peter.cautley
'''
from the_db import TheSystemsDb

if __name__ == '__main__':
    test_database = TheSystemsDb()
    test_database.create_tables()
    test_database.load_systems({'sys1' : { 'serv1':'localhost101', 
                                           'serv2':'localhost102' },
                                'sys2' : { 'serv3':'localhost103', 
                                           'serv4':'localhost104' } 
                               })
