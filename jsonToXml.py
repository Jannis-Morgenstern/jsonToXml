import json
import xml.etree.ElementTree as ET

# import and parse json file
with open('original_converted.json', encoding='utf-8-sig') as file:
    data = json.load(file)


def dict_to_xml(data, root='root'):
    root = ET.Element(root)
    build_xml(root, data)
    tree = ET.ElementTree(root)
    tree.write('sample.xml', short_empty_elements=False)


def build_xml(root, data, listname='ListName'):
    if isinstance(data, dict):
        for key, val in data.items():
            if not (isinstance(val, tuple) or isinstance(val, list)) or len(val) == 0:
                s = ET.SubElement(root, key)
                build_xml(s, val)
            else:
                build_xml(root, val, key)
    elif isinstance(data, tuple) or isinstance(data, list):
        for val in data:
            s = ET.SubElement(root, listname)
            build_xml(s, val)
    elif isinstance(data, str):
        root.text = data
    else:
        root.text = str(data)
    return root


dict_to_xml(data, root='Cluster')
