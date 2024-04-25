
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")
b=soup('span')
a=0
count=0
for tag in b:
    a=a+int(tag.contents[0])
    count=count+1
print("Count ",count)
print("Sum",a)
