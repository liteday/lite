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
        self.cursr.execute("SELECT name FROM sqlite_master WHERE type='table'")
        if self.cursr.fetchone() is None:
            return True
        else:
            return False

    def get_all_systems(self):
        '''get all system table entries and their servers and return as a dictionary'''
        system_dict={}
        sys_list=[]
        for sys in self.conn.execute('SELECT DISTINCT system_name FROM system'):
            sys_list.append(sys)
        #print sys_list

        for sys in sys_list:
            server_dict={}
            for server_name, ip in self.cursr.execute(
                            'SELECT DISTINCT server_name, server_address FROM server WHERE system_name=?', sys):
                server_dict[server_name]=ip
            system_dict[sys]=server_dict
            #print sys, server_dict
        print system_dict
        return system_dict

    def load_systems(self, system_dict):
        '''get all system table entries and their servers and return as a dictionary'''
        if type(system_dict) is not dict:
            raise Exception('load_systems invalid parameter: {0}'.format(system_dict))
        for sys in system_dict.keys():
            if type(sys) is not str:
                raise Exception('load_systems invalid system name: {0}'.format(sys))
            self._insert_system_table_entry((sys,))
            server_dict = system_dict[sys]
            if type(server_dict) is not dict:
                raise Exception('load_systems invalid server dict: {0}'.format(server_dict))
            for server_name, ip in server_dict.items():
                if type(server_name) is not str:
                    raise Exception('load_systems invalid server name: {0}'.format(server_name))
                if type(ip) is not str:
                    raise Exception('load_systems invalid server ip: {0}'.format(ip))
                self._insert_server_table_entry((sys,ip,server_name))
                
    def _insert_system_table_entry(self,cols):
        ''' Insert a row of data '''
        #print '_insert_system_table_entry {0}'.format(cols)
        self.cursr.execute("insert into system values (?)", (cols[0],))
        self.conn.commit()

    def _insert_server_table_entry(self,cols):
        ''' Insert a row of data '''
        #print '_insert_server_table_entry {0}'.format(cols)
        self.cursr.execute("insert into server values (?,?,?)", (cols[0],cols[1],cols[2]))
        self.conn.commit()

    def clear_tables(self):
        ''' Insert a row of data '''
        self.cursr.execute("DELETE FROM system")
        self.cursr.execute("DELETE FROM server")
        self.conn.commit()
        
    def shutdown(self):
        '''We can also close the connection if we are done with it.
        Just be sure any changes have been committed or they will be lost.'''
        self.conn.close()
        
    ''' 
        Phase 2 will be able to add indivu=idual systems and servers within systems
    '''

