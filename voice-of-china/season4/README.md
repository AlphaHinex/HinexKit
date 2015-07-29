中国好声音第四季专题歌曲下载
=======================


![](voice4.jpg)


专题页面
--------

[http://y.qq.com/topic/voice4/index.html](http://y.qq.com/topic/voice4/index.html)


python2.x 脚本
--------------

1. `voice_s4.py` 中，修改 `path` 为下载文件保存路径，之后保存脚本
2. `python voice_s4.py 1` 执行脚本，其中 `1` 为要下载的期的索引，如下载第一期为 `1`，下载第二期为 `2` 等。请耐心等待下载完毕
3. 除下载学员演唱的版本外，还会自动下载原唱版本
3. 若要下载指定歌曲，需先通过 `python voice_s4.py 1` 在 `console` 中输出的内容中找到歌曲的 `id` ，输出内容格式为 `prepare to download singer - song (id) ...`，在执行脚本时将要下载歌曲的 `id` 传入即可，如：

    python voice_s4.py 1 id1 id2 ...