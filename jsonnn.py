import urllib.request,urllib.parse,urllib.error
import json
url=input("Enter location: ")
print("Retrieving ",url)
op=urllib.request.urlopen(url)
data=op.read().decode()
print("Retrieved ",len(data)," characters")
js=json.loads(data)
sum=0
c=0
for item in js['comments']:
    count=int(item['count'])
    c=c+1
    sum=sum+count
print("Count: ",c)
print("Sum: ",sum)
