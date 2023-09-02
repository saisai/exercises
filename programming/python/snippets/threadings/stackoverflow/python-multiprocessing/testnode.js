var spawn = require('child_process').spawn;

var child = spawn('python', ['-u', 'ipc.py']);
child.stdout.on('data', function(data){console.log("stdout: " + data)});

var i = 0;
setInterval(function(){
    console.log(i);
    child.stdin.write("i = " + i++ + "\n");
}, 1000);
//https://stackoverflow.com/questions/28917323/bidrectional-node-python-communication/28917416#28917416