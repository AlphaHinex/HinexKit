$('li[sound_id] div a.playBtn').click(function() {
	var liEle = $(this).parent().parent();
	var soundId = liEle.attr('sound_id');
	var result = $.ajax({
		url: 'http://www.ximalaya.com/tracks/' + soundId + '.json',
		async: false,
		dataType: 'json'
	});
	var songPath = getSongPath(result.responseText);
	$(this).attr('href', 'http://fdfs.xmcdn.com/' + songPath);
});

function getSongPath(text) {
	var json = eval("("+text+")");
	var song = {};
	song.path128 = json.play_path_128;
	song.path64 = json.play_path_64;
	song.path32 = json.play_path_32;
	song.path = json.play_path;
	return song.path128!==null ? song.path128 : (song.path64!==null ? song.path64 : (song.path32!==null ? song.path32 : song.path));
}