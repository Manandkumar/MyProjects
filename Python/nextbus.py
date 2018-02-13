import urllib.request
u = urllib.request.urlopen('http://tfstta.int.thomson.com:8080/tfs/DefaultCollection/SmartOnline/_CustomBoards')
data =u.read()
from xml.etree.ElementTree import XML
doc = XML(data)

for pt in doc.findall('.//pt'):
    print (pt.text)
