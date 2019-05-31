import xml.etree.ElementTree as ET

filename = 'c:\\myfilepath\\myworkflow.yxmc'

tree = ET.parse(filename)
root = tree.getroot()


def UpdateConstant(elementName, replaceWith):
    replaced = False
    for constant in root.find(".//Constants"):
        if constant.find("./Name").text == elementName:
            constant.find("./Value").text = replaceWith
            replaced = True
            tree.write(filename)
        else:
            pass
    return replaced


print(UpdateConstant('Foo_Name', 'Foo_Value'))
