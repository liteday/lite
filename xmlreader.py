__author__ = 'root'
import sys
import lxml
import database
from lxml import etree
from database.the_db import TheSystemsDb
import argparse

servername=""
address=""

parser=argparse.ArgumentParser(description="xmlreader")
parser.add_argument('-c', '--cleardb', action='store_true')
parser.add_argument('-f', '--filename', action='store')
args = parser.parse_args()


def parse_xml(filename):
    servername=""
    address=""
    xmlDictionary={}
    tree=etree.parse(filename)
    for element in tree.iter():
        if element.tag == "system":
            for name, value in element.items():
                current_system_name=value
                xmlDictionary[value]={}
                for child in element:
                    for child2 in child.items():
                        if child2[0] == "name" :
                            servername=child2[1]
                        elif child2[0] == "addr":
                            address=child2[1]
                        xmlDictionary[current_system_name][servername]=address
    return xmlDictionary


def populate_database(xmldict):
    test_database = TheSystemsDb()
    test_database.load_systems(xmldict)

def clear_tables():
    test_database = TheSystemsDb()
    test_database.clear_tables()


if __name__ == "__main__":

    if args.filename == None or args.filename =="":
        print "No filename given.. exiting.."
        sys.exit()

    print "Parsing file " + args.filename
    xml_dict=parse_xml(args.filename)
    print "********************"
    print xml_dict
    print "******************"
    if args.cleardb == "True":
        print "clearing tables"
        clear_tables()
    print "Populating database"
    populate_database(xml_dict)
