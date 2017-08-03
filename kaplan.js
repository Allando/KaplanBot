const Discord = require("discord.js");
const cmdHandler = require("./Handler/commandHandler.js");

const TOKEN = "abc123"; // CHANGE THIS TO ACTUAL TOKEN!!!

var bot = new Discord.Client();
var kaplan = "<@342357527767547908>"; // Representation for @KaplanBot
var count = 1;

bot.on("ready", function () {
    console.log('I am ready!');
});

bot.on("message", function (message) {
    if (message.author.equals(bot.user)) return; // Stops bot from responding to itself.

    if (message.content === (kaplan + " Hello")) {
        message.channel.send("Hey it's Jeff from the Overwatch team!");
    } else if (message.content === (kaplan + " Last video")) {
        message.channel.send("https://www.youtube.com/watch?v=YPs__eUvtvU&t=2s");
    } else {
        message.channel.send("you suck " + count);
        count++;
    }


    console.log(message.content);
});

bot.login(TOKEN);


