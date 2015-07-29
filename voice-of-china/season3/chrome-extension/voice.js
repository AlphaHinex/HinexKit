$('.tabCon ul li [data-song]').click(function() {
	song_id = $(this).attr('data-song').split('&')[0].replace('song_id=','');
	code = CRC32(song_id);
	result = $.ajax({
		url: "http://ting.hotchanson.com/website/ting?song_id=" + song_id + "&code=" + code,
		async: false,
		dataType: "json"
	});
	songInfo = getSongInfo(result.responseText);
	$(this).attr('href', songInfo.url);
});

function CRC32(e){
	var t,r,n,a=new Array(256);
	for(t=0;256>t;t++){
		for(n=t,r=0;8>r;r++)
			n=1&n?n>>1&2147483647^3988292384:n>>1&2147483647;
		a[t]=n
	}
	for("string"!=typeof e&&(e=""+e),n=4294967295,t=0;t<e.length;t++)
		n=n>>8&16777215^a[255&n^e.charCodeAt(t)];
	return n^=4294967295,(n>>3).toString(16);
}

function getSongInfo(text) {
	var json = eval("("+text+")");
	var song = {};
	song.nm = json.data[0].song_name;
	song.url = json.data[0].url_list[2].url;
	song.format = json.data[0].url_list[2].format;
	return song;
}