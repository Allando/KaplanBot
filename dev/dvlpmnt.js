var $ = require("jQuery");
FEED_URL = "https://www.youtube.com/feeds/videos.xml?channel_id=UClOf1XXinvZsy4wKPAkro2A";

$.get(FEED_URL, function (data) {
    $(data).find("entry").each(function () { // or "item" or whatever suits your feed
        var el = $(this);

        // console.log("----------------------------------------");
        console.log("title       : " + el.find("title").text());
        console.log("text        : " + el.find("text").text());
        // console.log("Last Updated: " + el.find("LastUpdated").text());
    });
});