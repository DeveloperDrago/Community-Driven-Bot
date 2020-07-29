class Community extends require("discord.js").Client {
    constructor() {
        super()
        this.config = require('../config.js') //config.js.example 
    }  
}

module.exports = Community