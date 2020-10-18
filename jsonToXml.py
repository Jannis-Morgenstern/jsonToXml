import time
import json
import glob
import xml.etree.ElementTree as ET


def files_to_dicts(files, encoding='utf-8-sig'):
    dicts = []
    for file in files:
        with open(file, encoding=encoding) as file:
            dicts.append(json.load(file))
    return dicts


def dict_to_xml(data, output_file_name='sample.xml', root='root'):
    root = ET.Element(root)
    build_xml(root, data)
    tree = ET.ElementTree(root)
    tree.write(output_file_name, short_empty_elements=False)


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


file_names = glob.glob('**/*.json', recursive=True)

data = files_to_dicts(file_names)

# for idx, dictionary in enumerate(data):
#     dict_to_xml(
#         dictionary, output_file_name=file_names[idx][:-5] + '.xml', root='Cluster')


def foo():
    print(time.ctime())


while True:
    foo()
    time.sleep(1)
