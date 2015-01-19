import urllib2

sid    =   136913
margin =  30000000

req = urllib2.Request("http://115.231.20.59:80/%d.mp3" %(sid+margin))
# req.add_header('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36')
# req.add_header('Referer', 'http://y.qq.com/topic/iamsinger3/index.html')
# req.add_header('Range', 'bytes=0-')
# req.add_header('Pragma', 'no-cache')
req.add_header('Host', 'stream19.qqmusic.qq.com')
# req.add_header('Connection', 'keep-alive')
# req.add_header('Cache-Control', 'no-cache')
# req.add_header('Accept-Encoding', 'identity;q=1, *;q=0')
# req.add_header('Accept', '*/*')
req.add_header('Cookie', 'qqmusic_uin=12345678; qqmusic_key=12345678; qqmusic_fromtag=30')
response = urllib2.urlopen(req)
by = response.read()
open("/Users/alphahinex/Desktop/%d.mp3" %(sid+margin), "wb").write(by)
