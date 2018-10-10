from lxml import etree

#xpath_in = str(input("xpath: "))


tree = etree.parse(r'C:\PyCharm\Projects\xmlMapper\input.xml')

print(etree.tostring(tree))     #print whole tree

xpath_value = tree.xpath('//root/one/text()', smart_strings=False)    #pull value from //root/one

xpath = tree.xpath("/root/one")     #stores in to array
xpath_tag = xpath[0].tag            #choose tag of first array value

#print(xpath_value)

"""
for record in tree.xpath('/root/one'):     #loops through xpaths with this value and outputs tags, not the whole file only the store xpaths
    print(record.tag)
"""

"""
for element in tree.iter("one"):        #iterate through tree and find tags with labelled one
    print(element.tag)
"""

#tree_children = tree.getchildren()
#print(tree_children)

#x = tree.xpath("/root/child::*")
#print(x)

attribute_list = ""

for record in tree.xpath("/root[@attribute='1']/child::*"):     #loops through child nodes and output child tags
    tag = record.tag
    #print(record.tag)
    #print(record.attrib.keys())        #print attribute key values. attributes stored as dictionary with key=attribute value

    if record.attrib.keys():            #if dictionary is not empty loop through and get the attributes and join them to the tag
        for i in record.attrib.keys():
            attribute = "[@" + i + "]"
            attribute_list = attribute_list + attribute     #concatonate sting with all values of

            if attribute == attribute_list:
                print(tag + attribute)
            else:
                print(tag + attribute_list)

    else:
        print(record.tag)               #otherwise print the tag










