const Discord = require("discord.js");
const cmdHandler = require("./Handler/commandHandler.js");

const TOKEN = "MzQyMzU3NTI3NzY3NTQ3OTA4.DGUjzA.0jARq9uvrfhzoCUT2ZEsYe6liBI"; // CHANGE THIS TO ACTUAL TOKEN!!!

var bot = new Discord.Client();
var kaplan = "<@342357527767547908>"; // Representation for @KaplanBot
var count = 1;

bot.on("ready", function () {
    console.log('I am ready!');
});

bot.on("message", function (message) {
    if (message.author.equals(bot.user)) return; // Stops the bot from responding to itself.

    if (message.content === (kaplan + " Hello")) {
        message.channel.send("Hey it's Jeff from the Overwatch team!");
    } else if (message.content === (kaplan + " Last video")) {
        message.channel.send("https://www.youtube.com/watch?v=YPs__eUvtvU&t=2s");
    } else {
        var user = message.author.username;
        message.channel.send("Hi " + user + ", Looking at your profile, I’ve won approximately 800 more games than you have."+ "\n" +
            "That’s not counting the daily internal playtests I am in, the time I spent in Alpha and Beta.\n" +
            "\n" +
            "Did you have a specific question or are you just here trolling?");
    }

    console.log(message.content);
});

bot.login(TOKEN);

var FEED_URL = "https://www.youtube.com/feeds/videos.xml?channel_id=UClOf1XXinvZsy4wKPAkro2A";

jQuery.getFeed({
    url     : FEED_URL,
    success : function (feed) {
        console.log(feed.title);
        console.log(feed.success());
    }
});



