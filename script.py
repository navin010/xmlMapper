from lxml import etree

#xpath_in = str(input("xpath: "))


tree = etree.parse(r'C:\PyCharm\Projects\XMLMapperenv2\input.xml')

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

x = tree.xpath("/root/child::*")
print(x)

