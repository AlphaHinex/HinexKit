我是歌手第三季专题歌曲下载
=======================


![](iamsinger3.png)


专题页面
--------

[http://y.qq.com/topic/iamsinger3/index.html](http://y.qq.com/topic/iamsinger3/index.html)


python2.x 脚本
--------------

1. `python2/singer_s3.py` 中，修改 `date` 为要下载的竞演场次播放日期，修改 `path` 为下载文件保存路径，之后保存脚本
2. `python singer_s3.py` 执行脚本，等待下载完毕
3. 若要下载指定歌曲，需先通过 `python singer_s3.py` 在 `console` 中输出的内容中找到歌曲的 `id` ，输出内容格式为 `prepare to download singer - song (id) ...`，在执行脚本时将要下载歌曲的 `id` 传入即可，如：

    python singer_s3.py id1 id2 ...