module.exports = class Hello extends require('../../classes/command') {
    constructor(client) {
        super(client, {
            name: 'hello',
            description: 'Hello, World!',
            usage: 'hello',
            args: []
        })
    }

    /**
     * @param {import("discord.js").Message} message
     * @param {string[]} args
     */
    async exec(message, args) {
        return message.channel.send('world!')
    }
}