import cookielib;
import urllib2, urllib;
import json;
import time;

lasts = 0;
while True:
    try:
        homeUrl = "http://best.zhaopin.com";
        cj = cookielib.CookieJar();
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj));
        urllib2.install_opener(opener);
        resp = urllib2.urlopen(homeUrl, timeout=4);
        print 'response from home'
        time.sleep(1);

        voteUrl = "http://best.zhaopin.com/API/Vote.ashx";
        postData = "bestid=1093&source=best";
        req = urllib2.Request(voteUrl, postData);
        req.add_header('Referer', 'http://best.zhaopin.com/');
        resp = urllib2.urlopen(req, timeout=4);
        print 'vote:', resp.getcode(), ':', resp.read();
        time.sleep(2);

        scoreUrl = "http://best.zhaopin.com/API/ScoreCompany.ashx";
        postData = "bestid=1093&score=5%2C5%2C5%2C5%2C5%2C5&source=best";
        req = urllib2.Request(scoreUrl, postData);
        req.add_header('Referer', 'http://best.zhaopin.com/');
        resp = urllib2.urlopen(req, timeout=4);
        print 'score:', resp.getcode(), ':', resp.read();

        resultUrl = "http://best.zhaopin.com/API/getlayercompanyinfo.ashx";
        postData = "bestid=1093";
        req = urllib2.Request(resultUrl, postData);
        req.add_header('Referer', 'http://best.zhaopin.com/');
        resp = urllib2.urlopen(req, timeout=4);
        resJson = json.loads(resp.read());
        scores = resJson.get('data').get('score');
        s1 = scores.get('score1');
        s2 = scores.get('score2');
        s3 = scores.get('score3');
        s4 = scores.get('score4');
        s5 = scores.get('score5');
        s6 = scores.get('score6');
        s = s1+s2+s3+s4+s5+s6;
        print resp.getcode(), ':', s;
        if s == lasts:
            print 'hang up for 60s'
            time.sleep(60);
        else:
            lasts = s;
            time.sleep(5);
    except Exception, e:
        print 'timeout occurs, back to loop' 