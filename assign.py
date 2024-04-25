from urllib.request import urlopen
from bs4 import BeautifulSoup

url=input("enter-")
html=urllib.request.urlopen(url).read()
soup=BeautifulSoup(html,"html.parser")
tags=soup('span')
a=0
for tag in tags:
    b=span.contents[0]
    a=a+int(b)
print("sum:",a)
