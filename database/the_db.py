import sqlite3

class TheSystemsDb(object):
    ''' The Database '''

    def __init__(self):
        ''' Constructor  '''
        self.db_name = 'test_system_databse.db'
        self.conn = sqlite3.connect(self.db_name)
        self.cursr = self.conn.cursor()
        
    def create_tables(self):
        '''create system and server tables if they don't exist'''
        if self._no_tables_exist():
            self.cursr.execute('''CREATE TABLE system (system_name)''')
            self.cursr.execute('''CREATE TABLE server (system_name,server_address,server_name)''')

    def _no_tables_exist(self):
        '''check to see if tables already exist'''
        return False

    def get_all_systems(self):
        '''get all system table entries and their servers and return as a dictionary'''
        
    def load_systems(self):
        '''get all system table entries and their servers and return as a dictionary'''
        self._insert_system_table_entry(('ts1',))
        self._insert_server_table_entry(("ts1","localhost:2001","ts1:michael",))
        self._insert_server_table_entry(("ts1","localhost:2002","ts1:clark",))
                
    def _insert_system_table_entry(self,cols):
        ''' Insert a row of data '''
        self.cursr.execute("insert into system values (?)", (cols[0],))
        self.conn.commit()

    def _insert_server_table_entry(self,cols):
        ''' Insert a row of data '''
        self.cursr.execute("insert into server values (?,?,?)", (cols[0],cols[1],cols[2]))
        self.conn.commit()
        
    def shutdown(self):
        '''We can also close the connection if we are done with it.
        Just be sure any changes have been committed or they will be lost.'''
        self.conn.close()
        
    ''' 
        Phase 2 will be able to add indivu=idual systems and servers within systems
    '''

