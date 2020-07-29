module.exports = {
    type: 'once',
    run: (client) => {
        let chalk = require('chalk')
        console.info(`${chalk.green("[Drago's Community Bot - Javascript] >")} Ready!`)
    }
}