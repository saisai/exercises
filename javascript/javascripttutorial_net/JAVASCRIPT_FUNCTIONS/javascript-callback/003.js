function download(url, callback){
	setTimeout(() => {
		// script to download the picture here
        console.log(`Downloading ${url} ...`);
        // process the picture once it is completed
        callback(url);
	}, 3000);
}

let url = 'https://www.javascripttutorial.net/pic.jpg';

download(url, function(picture) {
	console.log(`Processing ${picture}`);
})