import urllib.request
ur="https://www.py4e.com/code3/mbox.txt"
uh=urllib.request.urlopen(ur)
up=uh.read()
print(up[1])
