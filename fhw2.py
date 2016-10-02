import re
import urllib

url='http://www.iskconbangalore.org/'

pattern=re.compile('<img src="([^">]+)"')
a=urllib.urlopen(url)
b=a.read()
a.close()
c=re.findall(pattern,b)
d=open('output.txt',"w")
#d.append(c)


for i in c:
    d.write(url + i + '\n')


d.close()    