import urllib.request
import json
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter location: ')
print('Retrieving', url)
uh = urllib.request.urlopen(url, context=ctx)
data = uh.read()
print('Retrieved', len(data), 'characters')
total = 0
count = 0
info = json.loads(data)

for item in info['comments']:
    total = total + int(item['count'])
    count = count + 1

print('Count:',count)
print('Sum:',total)
