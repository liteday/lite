__author__ = 'root'

import lxml
from lxml import etree

#variables
filename="demo.xml"

#parse xml
tree=etree.parse(filename)
#print etree.tostring(tree)

print type(tree)

xmlDictionary={}
xmlDictionary["system"]={}

current_system_name=""

for element in tree.iter():
    #print type(element)
    #print element.tag
    if element.tag == "system":
        #print "system"
        for name, value in element.items():
            current_system_name=value
            xmlDictionary["system"][value]={}
            print "name " + name
            print "value " + value
            #rint (name,value)

            for child in element:
                 for name, value in child.items():
                     xmlDictionary["system"][name]=value

print xmlDictionary


# "DELETE * from serve"r

#option to wipe the database (via command line arguments)
#argparse

# reader.py demo.xml
#
# reader.py --create demo.xml
#
# reader.py -c demo.xml

#sql strings
#sql_delete_system_table="DELETE * FROM system"
#sql_delete_server_table="DELETE * FROM server"

#INSERT INTO system (name) VALUES (systemnamevalue)
#INSER INTO server (address, name) VALUES (addressvalue, servernamevalue)

