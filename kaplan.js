const Discord = require("Discord.js");
const TOKEN = "123abc"; // CHANGE THIS TO ACTUAL TOKEN!!!

var bot = new Discord.Client();

bot.on("ready", function () {
    
});

bot.on("message", function (message) {
    console.log(message.content);
});

bot.login(TOKEN);


