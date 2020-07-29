(async function() {
    let Discord = require('discord.js')
    let Client = new (require('./classes/client'))()

    // Event Handler
    for(let event of require('fs').readdirSync('./events/')) {
        let eventFile = require('./events/'+event)
        let name = eventFile.name || event.split(".")[0]
        let once = eventFile.type == "once" ? true : false

        Client[once ? "once" : "on"](name, (...args) => eventFile.run(Client, ...args))
    }

    // Login using Token
    Client.login(Client.config["keys"].discord_token)
})