class Command {
    /**
     * @typedef {Array<{arg_name: string, arg_type: string | boolean | number | 'user' | 'channel'}>} typedef_args
     * @typedef {{name: string, description: string, usage: string, args?: typedef_args}} data
     * @param {import('./client')} client 
     * @param {data} data 
     */
    constructor(client, data) {
        this.client = client
        this.data = data
    }
}

module.exports = Command