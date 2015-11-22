# by Shomiron Ghose
# This looks like a url hopping game

# Lets use the wonderful requests library with cookies

import requests,json
cookiejar = {}
max_jumps = 1000

request_url = 'https://www.letsrevolutionizetesting.com/challenge.json'
found_one = False

for attempt in range(max_jumps):
    req = requests.get(request_url,cookies=cookiejar)
    nexturl = json.loads(req.text)
    if 'challenge' not in nexturl:
        print 'this one is weird: ',req.text
        found_one = True
        break
    else: # this is not needed - but it makes the code more understandable
        nexturl=nexturl['follow'].replace('challenge','challenge.json')
        print 'next jumping to: ',nexturl
    request_url = nexturl

if not found_one:
    print 'well we just did {} jumps and nothing'.format(max_jumps)