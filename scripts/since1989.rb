require 'rss'
require 'open-uri'

def download(uri, folder, n)
  nWeeksAgo = Time.now - 7*24*60*60 * n
  rss = RSS::Parser.parse(uri, false)
  rss.items.each do |item|
    if item.pubDate > nWeeksAgo
      url = item.enclosure.url.reverse
      postfix = url[0..url.index('.')].reverse
        open("#{item.title}#{postfix}", 'wb') do |file|
puts item.enclosure.url
          file << open(item.enclosure.url).read
          puts "download #{folder}/#{item.title}#{postfix} end"
        end
    end
  end
end

download('http://since1989.org/feed/wasai', 'wasai', 1)
# download('http://teahour.fm/feed.xml', 'teahour', 5)
