import urllib2

sids = [101824312, 5016169, 101824306, 465340, 101824313, 2530780]
margin = 30000000
path = '/Users/alphahinex/Desktop'

for sid in sids:
	req = urllib2.Request("http://115.231.20.59:80/%d.mp3" %(sid+margin))
	req.add_header('Host', 'stream19.qqmusic.qq.com')
	req.add_header('Cookie', 'qqmusic_uin=12345678; qqmusic_key=12345678; qqmusic_fromtag=30')
	response = urllib2.urlopen(req)
	by = response.read()
	open("%s/%d.mp3" %(path, sid+margin), "wb").write(by)
