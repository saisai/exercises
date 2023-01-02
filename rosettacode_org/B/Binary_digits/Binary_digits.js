
function toBinary(number)
{
    return Number(number)
        .toString(2);
}

var demoValues = [5, 50, 9000];
for (var i = 0; i < demoValues.length; ++i){
    console.log(toBinary(demoValues[i]));
}

