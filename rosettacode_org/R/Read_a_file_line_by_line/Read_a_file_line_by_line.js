
var fs = require("fs");

var readFile = function(path) {
    return fs.readFileSync(path).toString();
};

console.log(readFile("Read_a_file_line_by_line.js"));
