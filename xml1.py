import xml.etree.ElementTree as ET
data='''<person>
    <name>chuck</name>
    <phone type="intl">
        +1 85485390
    </phone>
    <email hide "yes"/>
</person>'''
tree=ET.fromstring(data)
print('name:',tree.find('name').text)
print('email:',tree.find('email').get('hide'))
