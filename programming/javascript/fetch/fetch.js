!async function(){
let data = await fetch("https://raw.githubusercontent.com/IbrahimTanyalcin/LEXICON/master/lexiconLogo.png")
    .then((response) => response.blob())
    .then(data => {
        return data;
    })
    .catch(error => {
        console.error(error);
    });

console.log(data);
}();

const data = (async function(){
	let data = await fetch("https://raw.githubusercontent.com/IbrahimTanyalcin/LEXICON/master/lexiconLogo.png")
    .then((response) => response.blob())
    .then(data => {
        return data;
    })
    .catch(error => {
        console.error(error);
    });

console.log(data);
}());


var getSheetId = function() {
      var url = 'https://raw.githubusercontent.com/IbrahimTanyalcin/LEXICON/master/lexiconLogo.png'
      return fetch(url)
        .then(response => response.blob())
		.then(data => {
			return data;
		})		
        .then(object => {
          //console.log(object.SheetID) // The correct value of object.SheetID prints to the console, as expected.
          return object;
        })
};

var test ;

getSheetId().then(rr => {
	console.log("rr "+ rr.size);
	test = rr.size;
});  


function getConfig() {  
  return fetch("https://raw.githubusercontent.com/IbrahimTanyalcin/LEXICON/master/lexiconLogo.png");
}

var dd = getConfig().then( data => {return data});

console.log("dd " + dd);

const address = fetch("https://jsonplaceholder.typicode.com/users/1")
  .then((response) => response.json())
  .then((user) => {
    return user.address;
  });

console.log(address);

const printAddress = () => {
  address.then((a) => {
    console.log(a);
	return a;
  });
};

var ee = printAddress();

console.log("ee "+ ee);


var obj;

fetch('https://jsonplaceholder.typicode.com/posts/1')
  .then(res => res.json())
  .then(data => {
    obj = data;
   })
  .then(() => {
    console.log(obj);
   });

setTimeout(function() {
	console.log("obj " + JSON.stringify(obj));
}, 900);