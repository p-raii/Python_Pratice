import urllib.request

sock = urllib.request.urlopen("http://diveintopython.org/")
htmlSource = sock.read()
sock.close()
print (htmlSource)
