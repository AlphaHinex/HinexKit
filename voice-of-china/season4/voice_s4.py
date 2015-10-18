import urllib2
import json
import threading
import sys
import os
import string

reload(sys)
sys.setdefaultencoding( "utf-8" )

# http://y.qq.com/topic/voice4/index.html
path = '/Users/alphahinex/Desktop/voice4/20151007'
margin = 30000000

class download(threading.Thread):
    def __init__(self, sid, file_name):
        threading.Thread.__init__(self)
        self.sid = sid
        self.file_name = file_name

    def run(self):
        if (isinstance(self.sid, int)):
            print 'prepare to download %s ...' %self.file_name
            os.system('mkdir -p %s' %path)
            # os.system('curl -H "Host:stream19.qqmusic.qq.com" -H "Cookie:qqmusic_uin=12345678; qqmusic_key=12345678; qqmusic_fromtag=30" http://stream19.qqmusic.qq.com/%d.mp3 -o %s/"%s.mp3" &' %(self.sid+margin, path, self.file_name))
            req = urllib2.Request('http://stream19.qqmusic.qq.com/%d.mp3' %(self.sid+margin))
            req.add_header('Host', 'stream19.qqmusic.qq.com')
            req.add_header('Cookie', 'qqmusic_uin=12345678; qqmusic_key=12345678; qqmusic_fromtag=30')
            while True:
                try:
                    response = urllib2.urlopen(req)
                    cl = string.atoi(response.info()['Content-Length'])
                    while True:
                        data = response.read()
                        if len(data) == cl:
                            break
                        else:
                            print 'read %d bytes, while content length is %d, reloading %s again ...' %(len(data), cl, self.file_name)
                    
                    open('%s/%s.mp3' %(path, self.file_name), 'wb').write(data)
                    print 'download %s done.' %self.file_name
                except Exception, e:
                    print 'exception occurs, try to reload %s again' %self.file_name
                    continue
                else:
                    break

def main(args):
    req = urllib2.Request('http://y.qq.com/m/act/voice4/%d.json' %(20 + string.atoi(args[1])))
    req.add_header('Host', 'y.qq.com')
    response = urllib2.urlopen(req)
    resp_str = response.read()
    json_obj = json.loads(resp_str[15:-1])
    songs = json_obj['songs']
    select_song = args[2:]

    for obj in songs:
        if((select_song and str(obj['Ftrack_id']) in select_song) or not select_song):
            download(obj['Ftrack_id'], "%s - %s(%s)" %(obj['Fsinger_name'], obj['Ftrack_name'], obj['Ftrack_id'])).start()
        if ((select_song and str(obj['Foriginal_track_id']) in select_song) or not select_song):
            download(obj['Foriginal_track_id'], "%s(%s)" %(obj['Ftrack_name'], obj['Foriginal_track_id'])).start()


if __name__ == '__main__':
    main(sys.argv)
