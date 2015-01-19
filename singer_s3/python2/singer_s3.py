import urllib2

sid    =   136913
margin =  30000000

req = urllib2.Request("http://115.231.20.59:80/%d.mp3" %(sid+margin))
req.add_header('Host', 'stream19.qqmusic.qq.com')
req.add_header('Cookie', 'qqmusic_uin=12345678; qqmusic_key=12345678; qqmusic_fromtag=30')
response = urllib2.urlopen(req)
by = response.read()
open("/Users/alphahinex/Desktop/%d.mp3" %(sid+margin), "wb").write(by)
