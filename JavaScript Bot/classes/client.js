class Community extends require("discord.js").Client {
    constructor() {
        super()
        this.config = require('../config.js') //config.js.example 
        /**
         * @type {import("discord.js").Collection<string, import("./command")>}
         */
        this.commands = new (require('discord.js')).Collection()
        this.chalk = require('chalk')
    }
    
    loadCommands() {
        for(let subdir of require('fs').readdirSync('./commands')) {
            for(let cmdFile of require('fs').readdirSync('./commands/'+subdir)) {
                let command = require(`./commands/${subdir}/${cmdFile}`)
                /**
                 * @type {import("./command")}
                 */                
                let cmd = new command(this)
                this.commands.set(cmd.data.name, command)
                console.info(this.chalk.green('[COMMANDS] > ') + `Loaded ${cmd.data.name} into Command Collection;`)
            }
        }
    }
}

module.exports = Community