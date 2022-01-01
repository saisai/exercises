let server = {
    name: 'Server',
    restart() {
        console.log("The " + this.name + " is restarting...")
    },
    'starting up'() {
        console.log("The " + this.name + " is starting up!");
    }
};

server['starting up']();