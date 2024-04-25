import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
URL = input('Enter URL : ')
p=input('Enter position : ')
pp=int(p)
c=input('Enter count : ')
cc=int(c)
position=0
count=0
while(count<=cc):
        print("retrieving:",URL)
        html = urllib.request.urlopen(URL, context=ctx).read()
        soup = BeautifulSoup(html,'html.parser')
        tags = soup('a')
        for tag in tags:
            position=position+1
            if (position==pp):
                URL=tag.get('href')
                break
        position=0
        count=count+1
