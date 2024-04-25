import urllib.request, urllib.parse, urllib.error
import json
import ssl

api_key = False


serviceurl = 'https://firms.modaps.eosdis.nasa.gov/api/area/csv/[MAP_KEY]/[SOURCE]/[AREA_COORDINATES]/[DAY_RANGE]'

address = input('Enter location: ')

# parms = dict()
# parms['address'] = address
# if api_key is not False: parms['key'] = api_key
url = serviceurl + urllib.parse.urlencode(parms)
print('Retrieving', url)
uh = urllib.request.urlopen(url)
data = uh.read().decode()
print('Retrieved', len(data), 'characters')

try:
    js = json.loads(data)
except:
    js = None

if not js or 'status' not in js or js['status'] != 'OK':
    print('==== Failure To Retrieve ====')
    print(data)
    exit()
pid = js['results'][0]['place_id']
print("Place id",pid)
