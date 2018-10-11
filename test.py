import re, collections
from lxml import etree

xml = '''\
<data>
    <timestamp>not important</timestamp>
    <people>
        <person name="Blue" given="John">
            <occupation>not important</occupation>
            <age>not important</age>
        </person>
        <person name="Green" given="Peter">
            <occupation>not important</occupation>
            <age>not important</age>
            <degree />
        </person>
        <person name="Red" given="Angela" maiden="Orange">
            <occupation fulltime="yes">not important</occupation>
            <age>not important</age>
            <birthday>not important</birthday>
            <degree />
            <siblings >
                <brother attrib1="no" attrib2="yes">not important</brother>
                <brother attrib1="yes">not important</brother>
                <sister>not important</sister>
            </siblings>
        </person>
    </people>
    <cities>
        <city name="Tokyo">
            <country>not important</country>
            <continent>not important</continent>
            <capital />
        </city>
        <city name="Atlanta">
            <country>not important</country>
            <continent>not important</continent>
            <olympics count="1">
                <year>1996</year>
                <season>summer</season>
            </olympics>
        </city>
    </cities>
</data>
'''

xml_root = etree.fromstring(xml)
raw_tree = etree.ElementTree(xml_root)
nice_tree = collections.OrderedDict()

for tag in xml_root.iter():
    #print(tag)
    #print(raw_tree.getpath(tag))
    path = re.sub('\[[0-9]+\]', '', raw_tree.getpath(tag))      #removes the [1] array values from the path
    #print(path)
    if path not in nice_tree:
        nice_tree[path] = []
        #print(nice_tree)
    if len(tag.keys()) > 0:
        nice_tree[path].extend(attrib for attrib in tag.keys() if attrib not in nice_tree[path])


for path, attribs in nice_tree.items():
    print(path)
    print(attribs)


query_in = str(input("xpath: "))
query_in_formatted = re.sub('\[(.* ?)\]', '', query_in)         #remove attributes
print(query_in)
print(query_in_formatted)

for path, attribs in nice_tree.items():
    if query_in_formatted == path:
        print(attribs)
        exit()
    elif query_in_formatted in path:
        print(path)











