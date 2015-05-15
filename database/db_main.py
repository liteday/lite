'''
Created on May 15, 2015

@author: peter.cautley
'''
from day4.database.the_db import TheSystemsDb


if __name__ == '__main__':
    test_database = TheSystemsDb()
    test_database.create_tables()
    test_database.load_systems()
