import urllib2
import json

date = '20150102'
path = '/Users/alphahinex/Desktop'
margin = 30000000

req = urllib2.Request("http://y.qq.com/m/act/iamsinger3/%s.json" %date)
response = urllib2.urlopen(req)
resp_str = response.read()
json_obj = json.loads(resp_str[15:-1])

for obj in json_obj:
	sids = [obj['track']['id'], obj['original_track']['id']]
	for sid in sids:
		req = urllib2.Request("http://115.231.20.59:80/%d.mp3" %(sid+margin))
		req.add_header('Host', 'stream19.qqmusic.qq.com')
		req.add_header('Cookie', 'qqmusic_uin=12345678; qqmusic_key=12345678; qqmusic_fromtag=30')
		response = urllib2.urlopen(req)
		print "prepare to download %d ..." %(sid+margin)
		by = response.read()
		open("%s/%d.mp3" %(path, sid+margin), "wb").write(by)
		print "download %d done" %(sid+margin)
