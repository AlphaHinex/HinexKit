import urllib2
import json
import threading
import sys
import os

reload(sys)
sys.setdefaultencoding( "utf-8" )

# http://y.qq.com/topic/voice4/index.html
path = '/Users/alphahinex/Desktop/voice4/20150724'
margin = 30000000

class download(threading.Thread):
    def __init__(self, sid, file_name):
        threading.Thread.__init__(self)
        self.sid = sid
        self.file_name = file_name

    def run(self):
        print 'prepare to download %s(%d) ...' %(self.file_name, self.sid)
        os.system('mkdir -p %s' %path)
        os.system('curl -H "Host:stream19.qqmusic.qq.com" -H "Cookie:qqmusic_uin=12345678; qqmusic_key=12345678; qqmusic_fromtag=30" http://stream19.qqmusic.qq.com/%d.mp3 -o %s/"%s.mp3" &' %(self.sid+margin, path, self.file_name))

def main(args):
    req = urllib2.Request('http://y.qq.com/m/act/voice4/2%s.json' %args[1])
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