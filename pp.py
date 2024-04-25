
import urllib.request, urllib.parse, urllib.errors
sock = urllib.request.urlopen("http://diveintopython.org/")
htmlSource = sock.read()
sock.close()
print (htmlSource)
