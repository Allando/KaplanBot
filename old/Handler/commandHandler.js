const Discord = require("discord.js");

// TODO: Takes input from discord users and respond accordingly.

var bot = new Discord.Client();

function CommandClass() {
    this.kaplan = "<@342357527767547908>";
}

CommandClass.prototype.talk = function()
{
    if (bot.message.content === (this.kaplan + " Hello Kaplan"))
    {
        bot.on("message", function (message)
        {
            message.channel.send("Hey it's Jeff from the Overwatch team!");
            console.log(message.content);
        });
    }
    else
    {
        bot.message.channel.send("Hey... it seems like you   fucked up. Please try again if you wanna get to Platinum.");
    }
};



