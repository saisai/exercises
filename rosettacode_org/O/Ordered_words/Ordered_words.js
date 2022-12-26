var fs = require('fs');
fs.readFile('../unixdict.txt', 'ascii', function (err, data) {
    var is_ordered = function(word){return word.split('').sort().join('') === word;},
        ordered_words = data.split('\n').filter(is_ordered).sort(function(a, b){return a.length - b.length}).reverse(),
        longest = [], curr = len = ordered_words[0].length, lcv = 0;
    while (curr === len){
        longest.push(ordered_words[lcv]);
        curr = ordered_words[++lcv].length;
    };
    console.log(longest.sort().join(', ') + '\n');
});