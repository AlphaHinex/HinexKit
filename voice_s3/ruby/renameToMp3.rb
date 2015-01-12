require 'taglib'

path = '/Users/alphahinex/Desktop/voice/8.22'
# Load an ID3v2 tag from a file
Dir.foreach(path) do |file|
  if file.end_with? '.mp3'
    TagLib::MPEG::File.open("#{path}/#{file}") do |mp3|
      tag = mp3.id3v2_tag
      File.rename mp3.name, "#{path}/#{tag.artist} - #{tag.title}.mp3"
    end
  end
end
