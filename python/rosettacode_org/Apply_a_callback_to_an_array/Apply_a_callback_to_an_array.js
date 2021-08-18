function map(a, func) {
    var ret = [];
    for(var i=0; i < a.length; i++) {
        ret[i] = func(a[i]);
    }
    return ret;
}

var t = '';
t  = map([1, 2, 3, 4], function(v) {return v * v;});
console.log(t);
