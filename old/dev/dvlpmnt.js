var $ = require("jQuery");
FEED_URL = "https://www.youtube.com/feeds/videos.xml?channel_id=UClOf1XXinvZsy4wKPAkro2A";

$(function() {
    var API_KEY = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxx';
    var DEV_PLAYLIST_ID = 'PLAYFVhxsaqDtdUmvSddqTXF2_6qqIXXt-'; //

    var GOOGLE_API_URL = 'https://www.googleapis.com/youtube/v3/playlistItems?part=id%2C+snippet%2C+contentDetails&playlistId='+DEV_PLAYLIST_ID+ '&key=' + API_KEY + '&callback=showVideos';

    $.ajax({
        url: GOOGLE_API_URL,
        dataType: 'jsonp',
        crossDomain: true
    });

    window.showVideos = function(data) {
        if (data.items && data.items.length > 0) {
            $("#video").html('<iframe width="504" height="283" src="http://www.youtube.com/embed/'+data.items[0].contentDetails.videoId+'" frameborder="0" allowfullscreen></iframe>');
        }
    }
});