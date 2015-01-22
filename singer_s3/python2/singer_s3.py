import urllib2
import json
import thread

date = '20150116'
path = '/Users/alphahinex/Desktop'
margin = 30000000

def download_mp3(sid, file_name):
    req = urllib2.Request("http://115.231.20.59:80/%d.mp3" %(sid+margin))
    req.add_header('Host', 'stream19.qqmusic.qq.com')
    req.add_header('Cookie', 'qqmusic_uin=12345678; qqmusic_key=12345678; qqmusic_fromtag=30')
    response = urllib2.urlopen(req)
    print "prepare to download %d ..." %(sid+margin)
    by = response.read()
    open("%s/%s.mp3" %(path, file_name), "wb").write(by)
    print "download %s done" %file_name

def main():
    req = urllib2.Request("http://y.qq.com/m/act/iamsinger3/%s.json" %date)
    response = urllib2.urlopen(req)
    resp_str = response.read()
    json_obj = json.loads(resp_str[15:-1])

    for obj in json_obj:
        thread.start_new_thread(download_mp3, (obj['track']['id'], "%s - %s" %(obj['singer']['name'], obj['track']['name'])))
        thread.start_new_thread(download_mp3, (obj['original_track']['id'], "%s - %s" %(obj['original_singer']['name'], obj['original_track']['name'])))

if __name__ == '__main__':
    main()