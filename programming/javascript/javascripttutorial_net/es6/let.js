
for(var i=0; i < 5; i++) {
    setTimeout(function() {
        console.log(i);
    },1000);
}

for(var i=0; i < 5; i++) {
    (function (j){
        setTimeout(function(){
            console.log(j);
        }, 2000);
    })(i);
}

for(let i=0; i < 5; i++) {
    setTimeout(function(){
        console.log(i);
    }, 1000);
}

for(let i=0; i < 5; i++) {
    setTimeout(() => console.log(i), 1000 );
}