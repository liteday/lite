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
parser.add_argument('filename')
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

    print "Parsing file " + args.filename
    xml_dict=parse_xml(args.filename)
    if args.cleardb:
        print "clearing tables"
        clear_tables()
    populate_database(xml_dict)
