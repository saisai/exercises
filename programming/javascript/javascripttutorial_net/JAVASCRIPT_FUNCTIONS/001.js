
function test_callback(url, options) {

    
	return function(data) {
		
		
        console.log(data)
        console.log(url)
        console.log(options)		

        console.log('ajax call')
		
		return 'test'

    }
}

var t = test_callback('url', 'options')('data');
console.log(`returning values ${t}`);

