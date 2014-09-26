__author__ = 'jetbrains'

import xml.etree.ElementTree as ET


path = 'version.xml'
fr = open(path, 'r')

tree = ET.parse('version.xml')
root = tree.getroot()

versionChild = root.find('version')
version = int(versionChild.text) + 1
versionChild.text = str(version)
tree.write(path)

