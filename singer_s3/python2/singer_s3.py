import urllib2
import json
import threading
import sys

date = '20150123'
path = '/Users/alphahinex/Desktop'
margin = 30000000

class download(threading.Thread):
    def __init__(self, sid, file_name):
        threading.Thread.__init__(self)
        self.sid = sid
        self.file_name = file_name

    def run(self):
        req = urllib2.Request('http://115.231.20.59:80/%d.mp3' %(self.sid+margin))
        req.add_header('Host', 'stream19.qqmusic.qq.com')
        req.add_header('Cookie', 'qqmusic_uin=12345678; qqmusic_key=12345678; qqmusic_fromtag=30')
        response = urllib2.urlopen(req)
        print 'prepare to download %s(%d) ...' %(self.file_name, self.sid)
        by = response.read()
        open('%s/%s.mp3' %(path, self.file_name), 'wb').write(by)
        print 'download %s done' %self.file_name

def main(args):
    req = urllib2.Request('http://y.qq.com/m/act/iamsinger3/%s.json' %date)
    response = urllib2.urlopen(req)
    resp_str = response.read()
    json_obj = json.loads(resp_str[15:-1])
    select_song = args[1:]
    prefixes = ['', 'original_']

    for obj in json_obj:
        for prefix in prefixes:
            if((select_song and str(obj['%strack' %prefix]['id']) in select_song) or not select_song):
                download(obj['%strack' %prefix]['id'], "%s - %s" %(obj['%ssinger' %prefix]['name'], obj['%strack' %prefix]['name'])).start()

if __name__ == '__main__':
    main(sys.argv)
